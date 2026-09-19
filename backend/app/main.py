"""
TruthLens FastAPI Application Entrypoint.

Provides evidence verification endpoints, verification history, benchmark claim catalogues, and health checks.
"""

import logging
from typing import List
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import settings
from app.models.schemas import (
    VerificationRequest,
    VerificationResponse,
    SampleClaimItem,
    HistoryItem,
    HealthResponse
)
from app.services.verification.verifier import ClaimVerifier
from app.database.db import (
    init_db,
    get_recent_history,
    get_record_by_id,
    clear_all_history
)
from app.data.sample_claims import SAMPLE_PRESETS

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logger = logging.getLogger("truthlens.main")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initializes the database schema on startup."""
    init_db()
    logger.info("TruthLens database and services ready.")
    yield


# Initialize FastAPI application with lifespan
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="TruthLens — Evidence-Based AI Claim Verification Platform",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Instantiate verifier
verifier = ClaimVerifier()


@app.get("/", tags=["General"])
async def root():
    """Root overview endpoint."""
    return {
        "service": "TruthLens",
        "tagline": "AI that doesn't just give an answer — it shows the evidence behind it.",
        "version": settings.VERSION,
        "status": "operational",
        "endpoints": {
            "verify": "POST /api/verify",
            "history": "GET /api/history",
            "history_detail": "GET /api/history/{id}",
            "sample_claims": "GET /api/sample-claims",
            "health": "GET /api/health",
            "docs": "/docs"
        }
    }


@app.get("/api/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """System health and search/AI provider connection status."""
    return HealthResponse(
        status="healthy",
        service=settings.PROJECT_NAME,
        version=settings.VERSION,
        search_provider_active=settings.has_search_provider,
        llm_provider_active=settings.has_llm_provider
    )


@app.get("/api/sample-claims", response_model=List[SampleClaimItem], tags=["Samples"])
async def get_sample_claims():
    """Returns preset claims for rapid testing and demonstrations."""
    return [SampleClaimItem(**item) for item in SAMPLE_PRESETS]


@app.post(
    "/api/verify",
    response_model=VerificationResponse,
    status_code=status.HTTP_200_OK,
    tags=["Verification"]
)
async def verify_claim_endpoint(request: VerificationRequest):
    """
    Submits a factual claim for full evidence-based verification.
    
    Pipeline:
    1. Understand/decompose the claim.
    2. Retrieve relevant evidence from reliable sources.
    3. Analyze and filter retrieved evidence.
    4. Categorize into supporting vs. contradicting evidence.
    5. Determine an evidence-based assessment with confidence rating.
    6. Explain WHY the assessment was reached and communicate limitations.
    7. Persist to SQLite history and return structured response.
    """
    cleaned_claim = request.claim.strip()
    if len(cleaned_claim) < 5:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Claim must contain at least 5 characters to be evaluated."
        )

    try:
        result = await verifier.verify(request)
        return result
    except Exception as e:
        logger.error(f"Verification pipeline failed: {str(e)}", exc_info=True)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error": "VerificationPipelineError",
                "message": "An unexpected error occurred while evaluating the claim.",
                "detail": str(e)
            }
        )


@app.get("/api/history", response_model=List[HistoryItem], tags=["History"])
async def get_history_endpoint(limit: int = 20):
    """Returns previously verified claims from SQLite database."""
    history_records = get_recent_history(limit=limit)
    return [HistoryItem(**rec) for rec in history_records]


@app.get("/api/history/{claim_id}", tags=["History"])
async def get_history_item_endpoint(claim_id: str):
    """Retrieves full serialized verification payload to reopen a past analysis."""
    record = get_record_by_id(claim_id)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Verification record with ID '{claim_id}' not found."
        )
    return record


@app.delete("/api/history", tags=["History"])
async def clear_history_endpoint():
    """Clears all verification history."""
    success = clear_all_history()
    return {"status": "cleared" if success else "failed"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=True)
