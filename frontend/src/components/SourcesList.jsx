import React from 'react';

export default function SourcesList({ sources = [] }) {
  if (!sources || sources.length === 0) return null;

  return (
    <section className="sources-card" aria-label="Authoritative Sources Consulted">
      <h3 className="section-heading">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
          <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
        </svg>
        Authoritative Sources Consulted ({sources.length})
      </h3>

      <div className="sources-grid">
        {sources.map((source, index) => (
          <div key={`${source.domain}-${index}`} className="source-item-card">
            <div className="source-info">
              <h5>{source.title || source.source_name}</h5>
              <span className="source-category">
                {source.source_name} • {source.category || 'Peer-Reviewed Source'}
              </span>
            </div>

            <div className="source-actions-group">
              <span className="source-tier-badge">{source.reliability_tier || 'High'}</span>
              {source.url && (
                <a
                  href={source.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label={`Open source document for ${source.source_name}`}
                  className="source-link-action"
                >
                  <span>Visit</span>
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
                    <polyline points="15 3 21 3 21 9" />
                    <line x1="10" y1="14" x2="21" y2="3" />
                  </svg>
                </a>
              )}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
