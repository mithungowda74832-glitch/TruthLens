import React, { useState } from 'react';

function EvidenceCard({ item, stanceColor, stanceLabel }) {
  const [isExpanded, setIsExpanded] = useState(false);
  const snippet = item.snippet || '';
  const isLong = snippet.length > 220;
  const displayText = isLong && !isExpanded ? `${snippet.slice(0, 220)}...` : snippet;

  return (
    <article className="evidence-card" id={item.id}>
      <div className="evidence-meta-row">
        <div className="evidence-tags-group">
          <span className="source-domain-pill">{item.source}</span>
          <span className={`stance-badge ${item.stance}`}>{stanceLabel}</span>
        </div>
        <div className="credibility-meter-pill">
          <span className="credibility-dot" style={{ backgroundColor: stanceColor }} />
          <span>Reliability: {item.credibility_score}%</span>
        </div>
      </div>

      <h4 className="evidence-title">{item.title}</h4>

      <div className="evidence-snippet-box">
        <p className="evidence-snippet-text">"{displayText}"</p>
        {isLong && (
          <button
            type="button"
            className="snippet-expand-btn"
            onClick={() => setIsExpanded(!isExpanded)}
          >
            {isExpanded ? 'Show less ▴' : 'Show full excerpt ▾'}
          </button>
        )}
      </div>

      <div className="evidence-footer">
        <span className="evidence-date">
          {item.published_date ? `Published: ${item.published_date}` : 'Verified Reference'}
        </span>
        {item.url && (
          <a
            href={item.url}
            target="_blank"
            rel="noopener noreferrer"
            className="source-link-action"
            title={`View primary source document at ${item.source}`}
          >
            <span>Direct Source</span>
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2">
              <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
              <polyline points="15 3 21 3 21 9" />
              <line x1="10" y1="14" x2="21" y2="3" />
            </svg>
          </a>
        )}
      </div>
    </article>
  );
}

export default function EvidenceSection({ supporting = [], contradicting = [] }) {
  return (
    <section className="evidence-container" aria-label="Supporting and Contradicting Evidence">
      {/* 6. SUPPORTING EVIDENCE */}
      <div className="evidence-column supporting">
        <div className="evidence-column-header">
          <h3 className="evidence-column-title">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
              <polyline points="20 6 9 17 4 12" />
            </svg>
            Supporting Evidence
          </h3>
          <span className="count-badge">{supporting.length} documented</span>
        </div>

        {supporting.length === 0 ? (
          <div className="empty-evidence-message">
            <p>No peer-reviewed or authoritative evidence was found supporting this claim.</p>
          </div>
        ) : (
          supporting.map((item) => (
            <EvidenceCard
              key={item.id}
              item={item}
              stanceColor="var(--verdict-supported)"
              stanceLabel="Stance: Supporting"
            />
          ))
        )}
      </div>

      {/* 7. CONTRADICTING EVIDENCE */}
      <div className="evidence-column contradicting">
        <div className="evidence-column-header">
          <h3 className="evidence-column-title">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
              <line x1="18" y1="6" x2="6" y2="18" />
              <line x1="6" y1="6" x2="18" y2="18" />
            </svg>
            Contradicting Evidence
          </h3>
          <span className="count-badge">{contradicting.length} documented</span>
        </div>

        {contradicting.length === 0 ? (
          <div className="empty-evidence-message">
            <p>No verified empirical counter-evidence or contradictory findings were found.</p>
          </div>
        ) : (
          contradicting.map((item) => (
            <EvidenceCard
              key={item.id}
              item={item}
              stanceColor="var(--verdict-refuted)"
              stanceLabel="Stance: Contradicting"
            />
          ))
        )}
      </div>
    </section>
  );
}
