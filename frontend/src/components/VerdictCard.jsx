import React from 'react';

export default function VerdictCard({ result }) {
  if (!result) return null;

  const {
    verdict,
    confidence,
    confidence_label,
    claim,
    explanation,
    detailed_rationale,
    processing_time_ms,
    retrieval_mode,
    reasoning_mode,
    created_at,
  } = result;

  // Format verdict presentation details according to exact TruthLens specification
  const getVerdictDetails = (v) => {
    switch (v) {
      case 'Supported':
        return {
          label: 'Supported',
          icon: '✓',
          cssClass: 'verdict-supported',
          color: 'var(--verdict-supported)',
        };
      case 'Partially Supported':
        return {
          label: 'Partially Supported',
          icon: '⚠',
          cssClass: 'verdict-partial',
          color: 'var(--verdict-partial)',
        };
      case 'Contradicted':
      case 'Refuted':
        return {
          label: 'Contradicted',
          icon: '✕',
          cssClass: 'verdict-refuted',
          color: 'var(--verdict-refuted)',
        };
      case 'Insufficient Evidence':
      default:
        return {
          label: 'Insufficient Evidence',
          icon: '?',
          cssClass: 'verdict-insufficient',
          color: 'var(--verdict-inconclusive)',
        };
    }
  };

  const details = getVerdictDetails(verdict);

  // SVG Gauge calculations
  const radius = 24;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (confidence / 100) * circumference;

  return (
    <div className={`verdict-hero-card ${details.cssClass}`}>
      <div className="verdict-top-row">
        <div className="verdict-badge-block">
          <div className="gauge-label">Evidence-Based Verdict</div>
          <div className={`verdict-pill ${details.cssClass}`}>
            <span>{details.icon}</span>
            <span>{details.label}</span>
          </div>
        </div>

        {/* Confidence Gauge Widget */}
        <div className="confidence-gauge-box">
          <div className="gauge-svg-container">
            <svg width="58" height="58" viewBox="0 0 58 58">
              <circle
                cx="29"
                cy="29"
                r={radius}
                fill="transparent"
                stroke="rgba(255, 255, 255, 0.08)"
                strokeWidth="5"
              />
              <circle
                cx="29"
                cy="29"
                r={radius}
                fill="transparent"
                stroke={details.color}
                strokeWidth="5"
                strokeDasharray={circumference}
                strokeDashoffset={strokeDashoffset}
                strokeLinecap="round"
                transform="rotate(-90 29 29)"
                style={{ transition: 'stroke-dashoffset 0.8s ease-in-out' }}
              />
            </svg>
            <span className="gauge-score-text">{confidence}%</span>
          </div>
          <div className="gauge-meta">
            <span className="gauge-label">Confidence Rating</span>
            <span className="gauge-confidence-tag">{confidence_label || `${confidence}% Calibrated`}</span>
          </div>
        </div>
      </div>

      {/* 1. ORIGINAL CLAIM */}
      <div className="claim-quote-box">
        <div className="claim-quote-label">Original Evaluated Claim</div>
        <p className="claim-quote-text">"{claim}"</p>
      </div>

      {/* 4. EXPLANATION */}
      <div className="executive-summary-box">
        <div className="summary-title">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
            <circle cx="12" cy="12" r="10" />
            <line x1="12" y1="16" x2="12" y2="12" />
            <line x1="12" y1="8" x2="12.01" y2="8" />
          </svg>
          Assessment Explanation
        </div>
        <p className="summary-text">{explanation}</p>
      </div>

      {/* In-Depth Reasoning Rationale */}
      {detailed_rationale && (
        <div className="detailed-rationale-box">
          <h4 className="rationale-heading">
            Detailed Verification Rationale & Evidence Cross-Examination:
          </h4>
          <p className="rationale-body">
            {detailed_rationale}
          </p>
        </div>
      )}

      {/* Meta Audit Trail Badges */}
      <div className="meta-badges-row">
        <span className="meta-badge">
          ⏱ Latency: {processing_time_ms} ms
        </span>
        <span className="meta-badge">
          🔍 Evidence Acquisition: {retrieval_mode?.replace('_', ' ').toUpperCase()}
        </span>
        <span className="meta-badge">
          🧠 Synthesis Mode: {reasoning_mode?.replace('_', ' ').toUpperCase()}
        </span>
        {created_at && (
          <span className="meta-badge">
            📅 {new Date(created_at).toLocaleDateString()} {new Date(created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
          </span>
        )}
      </div>
    </div>
  );
}
