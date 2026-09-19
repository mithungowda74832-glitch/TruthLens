"""
TruthLens Configuration Module.
Loads environment variables from .env file and provides structured settings with live reloading.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

# Initial load
load_dotenv(ENV_FILE, override=True)


class Settings:
    PROJECT_NAME: str = "TruthLens"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Evidence-Based AI Claim Verification Platform"
    
    # Server configuration
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", "8000"))
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # Allowed CORS origins
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
    
    def reload_env(self) -> None:
        """Reloads the .env file from disk."""
        load_dotenv(ENV_FILE, override=True)
    
    # Dynamic properties ensuring fresh reads when .env changes
    @property
    def TAVILY_API_KEY(self) -> str:
        self.reload_env()
        return os.getenv("TAVILY_API_KEY", "").strip()

    @property
    def SERPER_API_KEY(self) -> str:
        self.reload_env()
        return os.getenv("SERPER_API_KEY", "").strip()

    @property
    def GOOGLE_SEARCH_API_KEY(self) -> str:
        self.reload_env()
        return os.getenv("GOOGLE_SEARCH_API_KEY", "").strip()

    @property
    def GOOGLE_SEARCH_ENGINE_ID(self) -> str:
        self.reload_env()
        return os.getenv("GOOGLE_SEARCH_ENGINE_ID", "").strip()

    @property
    def GEMINI_API_KEY(self) -> str:
        self.reload_env()
        return os.getenv("GEMINI_API_KEY", "").strip()

    @property
    def OPENAI_API_KEY(self) -> str:
        self.reload_env()
        return os.getenv("OPENAI_API_KEY", "").strip()
    
    @property
    def has_search_provider(self) -> bool:
        """Returns True if any live search API key is configured."""
        return bool(self.TAVILY_API_KEY or self.SERPER_API_KEY or (self.GOOGLE_SEARCH_API_KEY and self.GOOGLE_SEARCH_ENGINE_ID))

    @property
    def has_llm_provider(self) -> bool:
        """Returns True if any live LLM API key is configured."""
        return bool(self.GEMINI_API_KEY or self.OPENAI_API_KEY)


settings = Settings()
