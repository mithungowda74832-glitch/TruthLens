/**
 * TruthLens API Client
 * Connects frontend to FastAPI verification and history endpoints.
 */

const API_BASE = 'https://truthlens-backend-uj3z.onrender.com/api';

/**
 * Submits a factual claim to the verification pipeline.
 * @param {string} claim
 * @returns {Promise<Object>}
 */
export async function verifyClaimApi(claim) {
  const response = await fetch(`${API_BASE}/verify`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
    body: JSON.stringify({ claim }),
  });

  if (!response.ok) {
    let errorDetail = 'Verification failed. Please try again.';
    try {
      const errData = await response.json();
      errorDetail = errData.detail || errData.message || errorDetail;
    } catch {
      errorDetail = `Server error ${response.status}: ${response.statusText}`;
    }
    throw new Error(errorDetail);
  }

  return response.json();
}

/**
 * Fetches curated preset claims for demonstrations.
 * @returns {Promise<Array>}
 */
export async function getSampleClaimsApi() {
  try {
    const response = await fetch(`${API_BASE}/sample-claims`);
    if (!response.ok) return [];
    return response.json();
  } catch (err) {
    console.warn('Could not fetch sample claims:', err);
    return [];
  }
}

/**
 * Performs a health check against the backend service.
 * @returns {Promise<Object>}
 */
export async function checkHealthApi() {
  try {
    const response = await fetch(`${API_BASE}/health`);
    if (!response.ok) return { status: 'degraded' };
    return response.json();
  } catch {
    return { status: 'offline' };
  }
}

/**
 * Fetches recent claim verification history from SQLite database.
 * @returns {Promise<Array>}
 */
export async function getHistoryApi() {
  try {
    const response = await fetch(`${API_BASE}/history`);
    if (!response.ok) return [];
    return response.json();
  } catch (err) {
    console.warn('Could not fetch verification history:', err);
    return [];
  }
}

/**
 * Reopens a specific verification record by ID.
 * @param {string} claimId
 * @returns {Promise<Object>}
 */
export async function getHistoryDetailApi(claimId) {
  const response = await fetch(`${API_BASE}/history/${claimId}`);
  if (!response.ok) {
    throw new Error('Failed to retrieve history details.');
  }
  return response.json();
}

/**
 * Clears verification history.
 * @returns {Promise<boolean>}
 */
export async function clearHistoryApi() {
  try {
    const response = await fetch(`${API_BASE}/history`, { method: 'DELETE' });
    return response.ok;
  } catch {
    return false;
  }
}
