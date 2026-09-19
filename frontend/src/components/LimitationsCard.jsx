import React from 'react';

export default function LimitationsCard({ limitations }) {
  if (!limitations) return null;

  return (
    <section className="limitations-card" aria-label="Evidence Limitations and Epistemic Uncertainty">
      <div className="limitations-header">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2">
          <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z" />
          <line x1="12" y1="9" x2="12" y2="13" />
          <line x1="12" y1="17" x2="12.01" y2="17" />
        </svg>
        <span>Evidence Limitations & Epistemic Uncertainty</span>
      </div>

      <p className="limitations-text">
        {limitations}
      </p>

      <div className="limitations-note">
        <em>
          Note: TruthLens provides evidence-based evaluations grounded in retrieved scientific, governmental,
          and fact-checking repositories. It communicates confidence and uncertainty rather than asserting absolute truth.
        </em>
      </div>
    </section>
  );
}
