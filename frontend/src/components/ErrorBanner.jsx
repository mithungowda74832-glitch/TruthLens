import React from 'react';

export default function ErrorBanner({ error, onRetry, onDismiss }) {
  if (!error) return null;

  return (
    <div className="error-banner" role="alert">
      <div className="error-icon">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2">
          <circle cx="12" cy="12" r="10" />
          <line x1="12" y1="8" x2="12" y2="12" />
          <line x1="12" y1="16" x2="12.01" y2="16" />
        </svg>
      </div>

      <div className="error-content" style={{ flex: 1 }}>
        <h4>Verification Request Issue</h4>
        <p>{error}</p>
      </div>

      <div style={{ display: 'flex', gap: '0.5rem', alignSelf: 'center' }}>
        {onRetry && (
          <button
            type="button"
            className="reset-btn"
            style={{ padding: '0.4rem 0.8rem', fontSize: '0.78rem' }}
            onClick={onRetry}
          >
            Retry
          </button>
        )}
        {onDismiss && (
          <button
            type="button"
            className="reset-btn"
            style={{ padding: '0.4rem 0.6rem', fontSize: '0.78rem' }}
            onClick={onDismiss}
            aria-label="Dismiss error"
          >
            ✕
          </button>
        )}
      </div>
    </div>
  );
}
