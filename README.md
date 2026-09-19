# TruthLens — Evidence-Based AI Claim Verification Platform

**TruthLens** is an evidence-first claim verification platform engineered to replace opaque "True/False" verdicts with verifiable scientific and empirical grounding.

---

## Key Features

1. **Evidence-Based Claim Verification**:
   - Deconstructs claims into core empirical propositions.
   - Discovers authoritative literature, scientific papers, and fact-checking registries.
   - Partitions findings strictly into **Supporting Evidence** and **Contradicting Evidence**.
2. **Transparent, Explainable Verdicts**:
   - Never returns an unexplained binary answer.
   - Provides an **Executive Synthesis** and in-depth **Verification Rationale**.
   - Computes a calibrated **Confidence Gauge** (0–100%).
3. **Primary Source Lineage**:
   - Displays source domain, credibility tier, excerpt snippet, publication date, and outbound links to primary sources.
4. **Hackathon & Production Ready Architecture**:
   - Clean separation of frontend UI, backend API, search retrieval services, and AI reasoning synthesis.
   - Built-in heuristic knowledge engine runs out-of-the-box before external API keys are configured.
   - Pluggable connectors for **Tavily**, **Serper (Google)**, and **Google Gemini 1.5/2.0**.

---

## Project Structure

```
devangers/
├── backend/
│   ├── app/
│   │   ├── main.py                # FastAPI endpoints (/api/verify, /api/health, /api/sample-claims)
│   │   ├── config.py              # Environment variable loader
│   │   ├── models/
│   │   │   └── schemas.py         # Pydantic contracts (VerificationResponse, EvidenceItem, etc.)
│   │   ├── services/
│   │   │   ├── verifier.py        # Master pipeline orchestrator
│   │   │   ├── search_service.py  # Evidence discovery (Tavily, Serper, Heuristic Fallback)
│   │   │   └── llm_service.py     # AI stance & verdict synthesis (Gemini, OpenAI, Heuristics)
│   │   └── data/
│   │       └── sample_claims.py   # Benchmark factual claims with peer-reviewed citations
│   ├── requirements.txt           # Python dependencies (fastapi, uvicorn, pydantic, httpx)
│   ├── .env.example               # Template for API keys
│   └── run_backend.py             # Quick backend runner
│
├── frontend/
│   ├── index.html                 # App shell with Inter & JetBrains Mono typography
│   ├── vite.config.js             # Vite config with /api proxy to backend:8000
│   ├── package.json               # React 18 + Vite dependencies
│   └── src/
│       ├── main.jsx               # React DOM entry
│       ├── App.jsx                # Main coordinator & state management
│       ├── index.css              # Custom Vanilla CSS design system (dark slate aesthetic)
│       ├── api/
│       │   └── client.js          # API client wrapper
│       └── components/
│           ├── Header.jsx         # TruthLens branding & live engine status
│           ├── ClaimInput.jsx     # Input textarea, character counter & sample claim chips
│           ├── VerificationProgress.jsx # Multi-stage investigation stepper loading state
│           ├── VerdictCard.jsx    # Verdict badge, SVG confidence gauge, executive summary
│           ├── EvidenceSection.jsx# Side-by-side Supporting vs Contradicting evidence cards
│           ├── SourcesList.jsx    # Index of consulted authoritative publications
│           └── ErrorBanner.jsx    # Error handling & retry trigger
│
└── README.md
```

---

## How to Run

### 1. Backend Setup

```bash
# Navigate to backend
cd backend

# Activate virtual environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# (If setting up fresh venv)
# python -m venv .venv
# .\.venv\Scripts\pip install -r requirements.txt

# Run FastAPI backend
python run_backend.py
# Backend starts at: http://127.0.0.1:8000
# Interactive OpenAPI documentation: http://127.0.0.1:8000/docs
```

### 2. Frontend Setup

```bash
# In a separate terminal, navigate to frontend
cd frontend

# Install dependencies (if not already installed)
npm install

# Start Vite dev server
npm run dev
# Frontend starts at: http://localhost:5174
```

---

## Where to Plug In External APIs

TruthLens is designed so you can add real API keys with zero architectural rework:

1. **Evidence Search Retrieval**:
   - File: [`backend/app/services/search_service.py`](file:///c:/Users/Mithun/Documents/SNPSU%20FILES/devangers/backend/app/services/search_service.py)
   - Keys: Set `TAVILY_API_KEY` or `SERPER_API_KEY` in `backend/.env`.
   - The service automatically detects active keys and routes queries to live web search.
2. **AI & LLM Reasoning Synthesis**:
   - File: [`backend/app/services/llm_service.py`](file:///c:/Users/Mithun/Documents/SNPSU%20FILES/devangers/backend/app/services/llm_service.py)
   - Keys: Set `GEMINI_API_KEY` in `backend/.env`.
   - The service will automatically prompt Gemini for nuanced stance classification and narrative explanations.

---

## Roadmap & Next Iterations

- [ ] **Multi-Hop Claim Decomposition**: Break compound sentences into independent sub-claims verified in parallel.
- [ ] **Direct Excerpt Highlighting**: Visual citation highlights showing exact sentences in source documents.
- [ ] **PDF / Article URL Ingestion**: Allow users to paste a URL or upload a PDF document for full-text fact-checking.
- [ ] **Historical Audit Log**: Local storage or database persistence of past claim verifications.
