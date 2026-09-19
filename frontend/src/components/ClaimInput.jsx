import React from 'react';

export default function ClaimInput({
  claim,
  setClaim,
  onVerify,
  isLoading,
  sampleClaims,
  onSelectSample,
}) {
  const handleKeyDown = (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      e.preventDefault();
      if (!isLoading && claim.trim().length >= 5) {
        onVerify();
      }
    }
  };

  const charCount = claim.length;
  const isTooShort = charCount > 0 && charCount < 5;

  return (
    <section className="claim-card">
      <div className="claim-input-label-row">
        <label htmlFor="claim-input" className="claim-input-label">
          <svg
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
          >
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
            <polyline points="14 2 14 8 20 8" />
            <line x1="16" y1="13" x2="8" y2="13" />
            <line x1="16" y1="17" x2="8" y2="17" />
          </svg>
          Claim Verification Input
        </label>

        <span className="char-counter">
          {charCount} / 2000 chars {isTooShort && '(min 5 chars)'}
        </span>
      </div>

      <textarea
        id="claim-input"
        className="claim-textarea"
        placeholder="Enter a claim you want to verify..."
        value={claim}
        onChange={(e) => setClaim(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={isLoading}
        rows={4}
      />

      {/* Example Claims */}
      {sampleClaims && sampleClaims.length > 0 && (
        <div className="presets-container">
          <span className="presets-label">
            Clickable Example Claims:
          </span>

          <div className="presets-chips">
            {sampleClaims.map((item) => (
              <button
                key={item.id}
                type="button"
                className="preset-chip-btn"
                onClick={() => onSelectSample(item.claim)}
                disabled={isLoading}
                title={item.description}
              >
                <span className="chip-tag">
                  {item.category}
                </span>

                <span>
                  {item.claim.length > 52
                    ? `${item.claim.slice(0, 52)}...`
                    : item.claim}
                </span>
              </button>
            ))}
          </div>
        </div>
      )}

      <div className="claim-actions-row">
        <div className="shortcut-tip">
          <span>Pro tip: Press</span>
          <kbd>Ctrl</kbd> + <kbd>Enter</kbd>
          <span>to submit</span>
        </div>

        <div className="claim-btn-group">
          {claim.trim().length > 0 && (
            <button
              type="button"
              className="clear-btn"
              onClick={() => setClaim('')}
              disabled={isLoading}
            >
              Clear
            </button>
          )}

          <button
            type="button"
            id="verify-claim-button"
            className="verify-button"
            onClick={onVerify}
            disabled={isLoading || claim.trim().length < 5}
          >
            {isLoading ? (
              <>
                <span className="spinner" />
                <span>Evaluating Evidence...</span>
              </>
            ) : (
              <>
                <svg
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2.5"
                >
                  <circle cx="11" cy="11" r="8" />
                  <line
                    x1="21"
                    y1="21"
                    x2="16.65"
                    y2="16.65"
                  />
                  <polyline points="11 8 13 11 9 11" />
                </svg>

                <span>Verify Claim</span>
              </>
            )}
          </button>
        </div>
      </div>
    </section>
  );
}