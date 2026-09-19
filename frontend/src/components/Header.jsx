import React from 'react';

export default function Header({ backendStatus, historyCount = 0, onOpenHistory }) {
  const isHealthy = backendStatus?.status === 'healthy';
  const statusLabel = isHealthy ? 'Engine Online' : 'Connecting Engine...';
  const modeLabel = backendStatus?.search_provider_active
    ? 'Live Search Active'
    : 'Heuristic Knowledge Active';

  return (
    <header className="header-wrapper">
      <div className="header-top">
        <div className="brand-badge-container">
          <div className="brand-logo-icon" aria-label="TruthLens Prism Logo">
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2.2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <circle cx="11" cy="11" r="8" />
              <line x1="21" y1="21" x2="16.65" y2="16.65" />
              <polygon points="11 7 13 11 9 11" fill="currentColor" opacity="0.35" />
              <circle cx="11" cy="11" r="2" fill="currentColor" />
            </svg>
          </div>
          <div className="brand-title-group">
            <h1>TruthLens</h1>
            <span className="brand-tagline">
              Evidence-based claim verification
            </span>
          </div>
        </div>

        <div className="header-status-group">
          <div className="status-pill" title="Verification Pipeline State">
            <span className={`status-dot ${isHealthy ? 'pulse' : ''}`} />
            <span>{statusLabel}</span>
          </div>
          
          <div className="status-pill" title="Active Retrieval Mode">
            <span style={{ color: 'var(--brand-cyan)' }}>◈</span>
            <span>{modeLabel}</span>
          </div>

          <button
            type="button"
            className="history-trigger-btn"
            onClick={onOpenHistory}
            title="Open Verification History"
          >
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2">
              <circle cx="12" cy="12" r="10" />
              <polyline points="12 6 12 12 16 14" />
            </svg>
            <span>History</span>
            {historyCount > 0 && <span className="history-count-badge">{historyCount}</span>}
          </button>
        </div>
      </div>
    </header>
  );
}
