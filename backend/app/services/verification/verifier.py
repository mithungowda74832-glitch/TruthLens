"""
TruthLens Master Verification Pipeline Coordinator.

Orchestrates:
1. User Claim Ingestion & Normalization
2. Evidence Retrieval (via EvidenceRetriever)
3. Evidence Filtering & Stance Partitioning
4. AI Cross-Examination & Assessment (via AIEvidenceAnalyzer)
5. Verdict + Calibrated Confidence Rating
6. Explanation + Source Lineage + Limitations Assembly
7. SQLite Database Persistence for Verification History
"""

import time
import uuid
import logging
from datetime import datetime, timezone
from typing import List

from app.models.schemas import (
    VerificationRequest,
    VerificationResponse,
    EvidenceItem,
    StanceType
)
from app.services.evidence.retriever import EvidenceRetriever
from app.services.ai.analyzer import AIEvidenceAnalyzer
from app.database.db import save_verification_record

logger = logging.getLogger("truthlens.verification")


class ClaimVerifier:
    """Core verification engine."""

    def __init__(self):
        self.retriever = EvidenceRetriever()
        self.analyzer = AIEvidenceAnalyzer()

    async def verify(self, request: VerificationRequest) -> VerificationResponse:
        start_time = time.perf_counter()
        raw_claim = request.claim.strip()
        logger.info(f"Starting verification pipeline for claim: '{raw_claim[:60]}...'")

        # -------------------------------------------------------------
        # Stage 1 & 2: Evidence Retrieval
        # -------------------------------------------------------------
        raw_evidence, sources, retrieval_mode = await self.retriever.retrieve_evidence(raw_claim)

        # -------------------------------------------------------------
        # Stage 3: Evidence Filtering & Stance Separation
        # -------------------------------------------------------------
        supporting_evidence: List[EvidenceItem] = []
        contradicting_evidence: List[EvidenceItem] = []

        for item in raw_evidence:
            if item.stance == StanceType.SUPPORTING:
                supporting_evidence.append(item)
            elif item.stance == StanceType.CONTRADICTING:
                contradicting_evidence.append(item)
            else:
                # Assign based on score orientation
                if item.credibility_score > 75:
                    supporting_evidence.append(item)
                else:
                    contradicting_evidence.append(item)

        supporting_evidence.sort(key=lambda x: x.credibility_score, reverse=True)
        contradicting_evidence.sort(key=lambda x: x.credibility_score, reverse=True)

        # -------------------------------------------------------------
        # Stage 4: AI Cross-Examination & Verdict Determination
        # -------------------------------------------------------------
        (
            verdict,
            confidence,
            explanation,
            detailed_rationale,
            claim_breakdown,
            limitations_and_uncertainty,
            reasoning_mode
        ) = await self.analyzer.analyze(
            claim=raw_claim,
            supporting_evidence=supporting_evidence,
            contradicting_evidence=contradicting_evidence
        )

        # -------------------------------------------------------------
        # Stage 5: Response Assembly & Confidence Calibration
        # -------------------------------------------------------------
        confidence_label = self._compute_confidence_label(confidence)
        elapsed_ms = int((time.perf_counter() - start_time) * 1000)
        claim_id = f"tl-{uuid.uuid4().hex[:10]}"
        created_at = datetime.now(timezone.utc).isoformat()

        response = VerificationResponse(
            id=claim_id,
            claim=raw_claim,
            verdict=verdict,
            confidence=confidence,
            confidence_label=confidence_label,
            explanation=explanation,
            detailed_rationale=detailed_rationale,
            claim_breakdown=claim_breakdown,
            supporting_evidence=supporting_evidence,
            contradicting_evidence=contradicting_evidence,
            sources=sources,
            limitations_and_uncertainty=limitations_and_uncertainty,
            created_at=created_at,
            processing_time_ms=elapsed_ms,
            retrieval_mode=retrieval_mode,
            reasoning_mode=reasoning_mode
        )

        # -------------------------------------------------------------
        # Stage 6: Database Persistence for History
        # -------------------------------------------------------------
        try:
            save_verification_record(response.model_dump())
        except Exception as e:
            logger.warning(f"Failed to record history to SQLite: {e}")

        logger.info(
            f"Pipeline completed in {elapsed_ms}ms: Verdict='{verdict.value}', Confidence={confidence}%"
        )
        return response

    def _compute_confidence_label(self, score: int) -> str:
        if score >= 90:
            return "Very High Confidence"
        elif score >= 75:
            return "High Confidence"
        elif score >= 60:
            return "Moderate Confidence"
        else:
            return "Uncertain / Insufficient Evidence"
