import React from 'react';

export default function HistoryDrawer({
  isOpen,
  onClose,
  history = [],
  onSelectHistory,
  onClearHistory,
}) {
  if (!isOpen) return null;

  const getVerdictClass = (verdict) => {
    const value = String(verdict || '').toLowerCase();

    if (value.includes('supported') && !value.includes('contradicted')) {
      return 'history-pill-supported';
    }

    if (value.includes('contradicted')) {
      return 'history-pill-contradicted';
    }

    if (value.includes('partial')) {
      return 'history-pill-partial';
    }

    return 'history-pill-insufficient';
  };

  return (
    <div className="history-drawer-overlay" onClick={onClose}>
      <aside
        className="history-drawer-panel"
        onClick={(event) => event.stopPropagation()}
      >
        <div className="history-drawer-header">
          <div>
            <h3>Verification History</h3>
            <p>{history.length} saved verification{history.length === 1 ? '' : 's'}</p>
          </div>

          <button
            type="button"
            className="history-close-btn"
            onClick={onClose}
            aria-label="Close history"
          >
            ×
          </button>
        </div>

        <div className="history-drawer-body">
          {history.length === 0 ? (
            <div className="empty-history-box">
              <p>No verification history yet.</p>
              <span>Verified claims will appear here.</span>
            </div>
          ) : (
            <div className="history-items-list">
              {history.map((item, index) => {
                const claimId = item.id ?? item.claim_id ?? index;
                const verdict = item.verdict || 'Insufficient Evidence';
                const confidence = item.confidence;

                return (
                  <button
                    key={claimId}
                    type="button"
                    className="history-item-card"
                    onClick={() => onSelectHistory(claimId)}
                  >
                    <div className="history-item-top">
                      <span className={`history-verdict-pill ${getVerdictClass(verdict)}`}>
                        {verdict}
                      </span>

                      {confidence !== undefined && confidence !== null && (
                        <span className="history-confidence-tag">
                          {confidence}%
                        </span>
                      )}
                    </div>

                    <div className="history-claim-text">
                      {item.claim || 'Untitled claim'}
                    </div>

                    <div className="history-item-footer">
                      <span>Open verification →</span>
                    </div>
                  </button>
                );
              })}
            </div>
          )}
        </div>

        <div className="history-drawer-footer">
          {history.length > 0 && (
            <button
              type="button"
              className="reset-btn"
              onClick={onClearHistory}
            >
              Clear History
            </button>
          )}

          <button
            type="button"
            className="reset-btn"
            onClick={onClose}
          >
            Close
          </button>
        </div>
      </aside>
    </div>
  );
}
