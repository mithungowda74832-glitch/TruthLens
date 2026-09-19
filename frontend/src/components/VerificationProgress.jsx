import React, { useState, useEffect } from 'react';

const PIPELINE_STEPS = [
  {
    id: 1,
    title: 'Deconstructing Claim Propositions',
    desc: 'Extracting key predicates, entities, and empirical assertions from input...',
  },
  {
    id: 2,
    title: 'Querying Authoritative Evidence',
    desc: 'Searching peer-reviewed publications, health agencies, and verified registries...',
  },
  {
    id: 3,
    title: 'Cross-Examining Evidence Stance',
    desc: 'Categorizing citations into supporting vs contradicting evidence and weighting credibility...',
  },
  {
    id: 4,
    title: 'Synthesizing Explainable Verdict',
    desc: 'Calibrating confidence score and generating transparent narrative rationale...',
  },
];

export default function VerificationProgress() {
  const [currentStep, setCurrentStep] = useState(1);

  useEffect(() => {
    const timer1 = setTimeout(() => setCurrentStep(2), 650);
    const timer2 = setTimeout(() => setCurrentStep(3), 1400);
    const timer3 = setTimeout(() => setCurrentStep(4), 2100);

    return () => {
      clearTimeout(timer1);
      clearTimeout(timer2);
      clearTimeout(timer3);
    };
  }, []);

  return (
    <div className="verification-progress-card" role="status" aria-live="polite">
      <div className="progress-header">
        <h3 className="progress-title">Verification Pipeline In Progress</h3>
        <p className="progress-subtitle">
          TruthLens is conducting multi-source cross-examination across scientific and empirical databases.
        </p>
      </div>

      <div className="stepper-list">
        {PIPELINE_STEPS.map((step) => {
          let statusClass = 'pending';
          if (step.id < currentStep) statusClass = 'completed';
          else if (step.id === currentStep) statusClass = 'active';

          return (
            <div key={step.id} className={`step-item ${statusClass}`}>
              <div className="step-icon">
                {statusClass === 'completed' ? (
                  '✓'
                ) : statusClass === 'active' ? (
                  <span className="spinner" style={{ width: '14px', height: '14px', borderWidth: '2px' }} />
                ) : (
                  step.id
                )}
              </div>
              <div className="step-content">
                <div className="step-label">{step.title}</div>
                <div className="step-subtext">{step.desc}</div>
              </div>
            </div>
          );
        })}
      </div>

      <div style={{ display: 'inline-flex', alignItems: 'center', gap: '0.6rem', color: 'var(--text-muted)', fontSize: '0.8rem' }}>
        <span className="status-dot pulse" />
        <span>Evaluating citations with calibrated confidence models...</span>
      </div>
    </div>
  );
}
