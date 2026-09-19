"""
Pydantic schemas defining the API contracts for TruthLens claim verification.
Strictly adheres to:
Verdicts: 'Supported', 'Partially Supported', 'Contradicted', 'Insufficient Evidence'.
"""

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field


class VerdictType(str, Enum):
    """The four official TruthLens verification verdicts."""
    SUPPORTED = "Supported"
    PARTIALLY_SUPPORTED = "Partially Supported"
    CONTRADICTED = "Contradicted"
    INSUFFICIENT_EVIDENCE = "Insufficient Evidence"


class StanceType(str, Enum):
    """The stance of an individual piece of evidence towards the claim."""
    SUPPORTING = "supporting"
    CONTRADICTING = "contradicting"
    NEUTRAL = "neutral"


class EvidenceItem(BaseModel):
    """An individual piece of retrieved factual evidence."""
    id: str = Field(..., description="Unique identifier for evidence item")
    title: str = Field(..., description="Headline or paper title")
    url: str = Field(..., description="URL link to primary source")
    snippet: str = Field(..., description="Key excerpt or citation quote directly relevant to the claim")
    source: str = Field(..., description="Publishing body or journal name (e.g. Nature, WHO, Reuters)")
    domain: Optional[str] = Field(None, description="Domain hostname (e.g. nih.gov, who.int)")
    stance: StanceType = Field(..., description="Whether evidence supports or contradicts the claim")
    credibility_score: int = Field(90, ge=0, le=100, description="Source credibility index (0-100)")
    published_date: Optional[str] = Field(None, description="Publication or review date")


class SourceReference(BaseModel):
    """High-level summary of an authoritative source consulted."""
    title: str
    source_name: str
    domain: str
    url: str
    category: str = Field("Verified Registry", description="Category of the source organization")
    reliability_tier: str = Field("High", description="High, Moderate, or Contextual")


class SubClaimAssessment(BaseModel):
    """Component breakdown of individual sub-claims within a complex statement."""
    sub_claim: str = Field(..., description="Specific proposition or predicate")
    assessment: str = Field(..., description="Supported, Contradicted, or Insufficient Evidence")
    confidence: int = Field(..., ge=0, le=100, description="Confidence in this specific sub-claim")
    rationale: str = Field(..., description="Concise explanation for this sub-claim's assessment")


class VerificationRequest(BaseModel):
    """Request payload for claim verification."""
    claim: str = Field(
        ...,
        min_length=5,
        max_length=2000,
        description="The factual claim to verify"
    )


class VerificationResponse(BaseModel):
    """Full explainable claim verification assessment payload matching TruthLens spec."""
    id: str
    claim: str
    verdict: VerdictType
    confidence: int = Field(..., ge=0, le=100, description="Verification confidence percentage (0-100)")
    confidence_label: str = Field(..., description="e.g. Very High, High, Moderate, Uncertain")
    explanation: str = Field(..., description="Concise human-readable explanation of why the result was reached")
    detailed_rationale: Optional[str] = Field(None, description="In-depth step-by-step reasoning with citations")
    claim_breakdown: List[SubClaimAssessment] = Field(
        default_factory=list,
        description="Decomposed components with individual assessments"
    )
    supporting_evidence: List[EvidenceItem] = Field(
        default_factory=list,
        description="Empirical items supporting the claim"
    )
    contradicting_evidence: List[EvidenceItem] = Field(
        default_factory=list,
        description="Empirical items contradicting or refuting the claim"
    )
    sources: List[SourceReference] = Field(
        default_factory=list,
        description="Clickable authoritative source references used"
    )
    limitations_and_uncertainty: str = Field(
        ...,
        description="Explicit caveats regarding data freshness, conflicting methodologies, or evidence gaps"
    )
    created_at: str
    processing_time_ms: int
    retrieval_mode: str = Field("benchmark_dataset", description="Mode of evidence acquisition")
    reasoning_mode: str = Field("structured_evidence_analysis", description="AI / synthesis engine")


class HistoryItem(BaseModel):
    """Summary item for past verification history."""
    id: str
    claim: str
    verdict: str
    confidence: int
    explanation: str
    created_at: str


class SampleClaimItem(BaseModel):
    """Preset factual claim for quick evaluation."""
    id: str
    category: str
    claim: str
    expected_verdict: str
    description: str


class HealthResponse(BaseModel):
    """API health and service configuration status."""
    status: str
    service: str
    version: str
    search_provider_active: bool
    llm_provider_active: bool
