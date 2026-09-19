import React from 'react';

export default function ClaimBreakdown({ breakdown = [] }) {
  if (!breakdown || breakdown.length === 0) return null;

  const getAssessmentClass = (assessment) => {
    switch (assessment) {
      case 'Supported':
        return 'assessment-supported';
      case 'Contradicted':
      case 'Refuted':
        return 'assessment-contradicted';
      case 'Partially Supported':
        return 'assessment-partial';
      case 'Insufficient Evidence':
      default:
        return 'assessment-insufficient';
    }
  };

  return (
    <section className="explanation-card" aria-label="Deconstructed Claim Propositions">
      <h3 className="section-heading">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2">
          <rect x="3" y="3" width="7" height="7" />
          <rect x="14" y="3" width="7" height="7" />
          <rect x="14" y="14" width="7" height="7" />
          <rect x="3" y="14" width="7" height="7" />
        </svg>
        Claim Breakdown & Sub-Proposition Assessments ({breakdown.length})
      </h3>

      <div className="breakdown-list">
        {breakdown.map((item, index) => (
          <div key={index} className="breakdown-item-card">
            <div className="breakdown-top-row">
              <span className="sub-claim-index">Component {index + 1}</span>
              <div className="breakdown-badges">
                <span className={`assessment-pill ${getAssessmentClass(item.assessment)}`}>
                  {item.assessment}
                </span>
                <span className="confidence-chip">{item.confidence}% confidence</span>
              </div>
            </div>

            <h4 className="sub-claim-text">"{item.sub_claim}"</h4>

            {item.rationale && (
              <p className="sub-claim-rationale">
                <strong>Analysis:</strong> {item.rationale}
              </p>
            )}
          </div>
        ))}
      </div>
    </section>
  );
}
