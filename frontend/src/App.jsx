import React, { useState, useEffect, useRef } from 'react';
import Header from './components/Header';
import ClaimInput from './components/ClaimInput';
import VerificationProgress from './components/VerificationProgress';
import VerdictCard from './components/VerdictCard';
import ClaimBreakdown from './components/ClaimBreakdown';
import EvidenceSection from './components/EvidenceSection';
import LimitationsCard from './components/LimitationsCard';
import SourcesList from './components/SourcesList';
import HistoryDrawer from './components/HistoryDrawer';
import ErrorBanner from './components/ErrorBanner';
import {
  verifyClaimApi,
  getSampleClaimsApi,
  checkHealthApi,
  getHistoryApi,
  getHistoryDetailApi,
  clearHistoryApi,
} from './api/client';

export default function App() {
  const [claim, setClaim] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [sampleClaims, setSampleClaims] = useState([]);
  const [backendStatus, setBackendStatus] = useState(null);
  const [history, setHistory] = useState([]);
  const [isHistoryOpen, setIsHistoryOpen] = useState(false);

  const resultsRef = useRef(null);

  // Load initial backend state, samples, and verification history
  useEffect(() => {
    async function init() {
      try {
        const [health, samples, hist] = await Promise.all([
          checkHealthApi(),
          getSampleClaimsApi(),
          getHistoryApi(),
        ]);
        setBackendStatus(health);
        setSampleClaims(samples);
        setHistory(hist);
      } catch (err) {
        console.error('Failed to load initial data:', err);
      }
    }
    init();
  }, []);

  const handleVerify = async () => {
    const trimmed = claim.trim();
    if (trimmed.length < 5) {
      setError('Please provide a factual claim with at least 5 characters for evidence evaluation.');
      return;
    }

    setError(null);
    setIsLoading(true);
    setResult(null);

    try {
      const data = await verifyClaimApi(trimmed);
      setResult(data);

      // Refresh history list after new verification
      const updatedHistory = await getHistoryApi();
      setHistory(updatedHistory);

      // Smooth scroll down to results
      setTimeout(() => {
        resultsRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 100);
    } catch (err) {
      setError(err.message || 'An unexpected error occurred during verification.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleSelectSample = (sampleText) => {
    setClaim(sampleText);
    setError(null);
  };

  const handleSelectHistory = async (claimId) => {
    try {
      const record = await getHistoryDetailApi(claimId);
      if (record) {
        setResult(record);
        setClaim(record.claim);
        setIsHistoryOpen(false);
        setTimeout(() => {
          resultsRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 100);
      }
    } catch (err) {
      setError('Failed to reopen the historical claim record.');
    }
  };

  const handleClearHistory = async () => {
    const ok = await clearHistoryApi();
    if (ok) {
      setHistory([]);
    }
  };

  const handleReset = () => {
    setResult(null);
    setClaim('');
    setError(null);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="app-container">
      <Header
        backendStatus={backendStatus}
        historyCount={history.length}
        onOpenHistory={() => setIsHistoryOpen(true)}
      />

      <main>
        {/* Main Brand Hero Presentation */}
        <section className="hero-section">
          <h2 className="hero-title">
            AI-Powered Evidence-Based Claim Verification
          </h2>
          <p className="hero-subtitle">
            TruthLens deconstructs claims, retrieves peer-reviewed and authoritative empirical evidence,
            partitions supporting versus contradicting citations, and synthesizes explainable assessments.
          </p>
        </section>

        {/* Error Notification */}
        {error && (
          <ErrorBanner
            error={error}
            onRetry={handleVerify}
            onDismiss={() => setError(null)}
          />
        )}

        {/* Claim Input Card */}
        <ClaimInput
          claim={claim}
          setClaim={setClaim}
          onVerify={handleVerify}
          isLoading={isLoading}
          sampleClaims={sampleClaims}
          onSelectSample={handleSelectSample}
        />

        {/* Loading / Pipeline State */}
        {isLoading && <VerificationProgress />}

        {/* Verification Results Section */}
        {result && !isLoading && (
          <div ref={resultsRef} className="results-container">
            {/* 1. Verdict & Confidence & Explanation */}
            <VerdictCard result={result} />

            {/* 5. Claim Breakdown into Sub-Propositions */}
            <ClaimBreakdown breakdown={result.claim_breakdown} />

            {/* 6 & 7. Supporting and Contradicting Evidence */}
            <EvidenceSection
              supporting={result.supporting_evidence}
              contradicting={result.contradicting_evidence}
            />

            {/* 9. Limitations & Uncertainty */}
            <LimitationsCard limitations={result.limitations_and_uncertainty} />

            {/* 8. Sources Consulted */}
            <SourcesList sources={result.sources} />

            {/* Reset / Verification Action Row */}
            <div className="reset-action-row">
              <button type="button" className="reset-btn" onClick={handleReset}>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <polyline points="1 4 1 10 7 10" />
                  <path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10" />
                </svg>
                Verify Another Claim
              </button>
            </div>
          </div>
        )}
      </main>

      {/* History Drawer Modal */}
      <HistoryDrawer
        isOpen={isHistoryOpen}
        onClose={() => setIsHistoryOpen(false)}
        history={history}
        onSelectHistory={handleSelectHistory}
        onClearHistory={handleClearHistory}
      />

      <footer className="app-footer">
        <p>
          TruthLens Evidence Engine • AI That Doesn't Just Give An Answer — It Shows The Evidence Behind It
        </p>
      </footer>
    </div>
  );
}
