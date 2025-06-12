"""
Configuration file for Bibliography Checker
"""

import os
from typing import Dict, List

# =============================================================================
# API KEYS (Set these to enable premium database access)
# =============================================================================

# Scopus API (Elsevier) - Get from https://dev.elsevier.com
SCOPUS_API_KEY = os.getenv("SCOPUS_API_KEY", "")

# IEEE Xplore API - Get from https://developer.ieee.org  
IEEE_API_KEY = os.getenv("IEEE_API_KEY", "")

# Semantic Scholar API - Get from https://api.semanticscholar.org
SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY", "")

# =============================================================================
# DATABASE CONFIGURATION
# =============================================================================

# Free databases (no API key required)
FREE_DATABASES = {
    "crossref": {
        "name": "CrossRef",
        "base_url": "https://api.crossref.org/works",
        "description": "DOI and metadata for 130M+ scholarly works",
        "rate_limit": 50,  # requests per second
        "enabled": True
    },
    "pubmed": {
        "name": "PubMed",
        "base_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils",
        "description": "35M+ biomedical literature citations", 
        "rate_limit": 3,   # requests per second
        "enabled": True
    },
    "arxiv": {
        "name": "arXiv",
        "base_url": "http://export.arxiv.org/api/query",
        "description": "2M+ preprints in physics, math, CS, etc.",
        "rate_limit": 3,   # requests per second  
        "enabled": True
    }
}

# Premium databases (API key required)
PREMIUM_DATABASES = {
    "scopus": {
        "name": "Scopus",
        "base_url": "https://api.elsevier.com/content/search/scopus",
        "description": "80M+ documents from 7000+ publishers",
        "rate_limit": 9,   # requests per second for non-institutional
        "enabled": bool(SCOPUS_API_KEY),
        "api_key": SCOPUS_API_KEY
    },
    "ieee": {
        "name": "IEEE Xplore",
        "base_url": "https://ieeexploreapi.ieee.org/api/v1/search/articles",
        "description": "5M+ technical documents from IEEE",
        "rate_limit": 200, # requests per day for basic plan
        "enabled": bool(IEEE_API_KEY),
        "api_key": IEEE_API_KEY
    }
}

# =============================================================================
# PARSING CONFIGURATION
# =============================================================================

# Citation style patterns
CITATION_PATTERNS = {
    "apa": [
        r'([A-Z][a-z]+(?:,\s[A-Z][a-z]+)*,?\s\([0-9]{4}\))',
        r'([A-Z][a-z]+,\s[A-Z]\.(?:\s[A-Z]\.)*\s\([0-9]{4}\)\.?\s[^.]+\.)',
    ],
    "mla": [
        r'([A-Z][a-z]+,\s[A-Z][a-z]+\.?\s"[^"]+"\s[^,]+,\s[0-9]{4})',
    ],
    "chicago": [
        r'([A-Z][a-z]+,\s[A-Z][a-z]+\.?\s"[^"]+,"\s[^(]+\([0-9]{4}\))',
    ],
    "vancouver": [
        r'([0-9]+\.\s[A-Z][a-z]+\s[A-Z]\.?\s[^.]+\.\s[^.]+\.\s[0-9]{4})',
    ],
    "ieee": [
        r'(\[[0-9]+\]\s[A-Z][a-z]+.*?[0-9]{4})',
    ]
}

# Bibliography section identifiers
BIBLIOGRAPHY_PATTERNS = [
    r'(?i)references?\s*\n',
    r'(?i)bibliography\s*\n',
    r'(?i)works?\s+cited\s*\n', 
    r'(?i)literature\s+cited\s*\n',
    r'(?i)riferimenti\s+bibliografici?\s*\n',
    r'(?i)bibliografia\s*\n',
    r'(?i)bibliographie\s*\n',
    r'(?i)literatur\s*\n'
]

# =============================================================================
# MATCHING CONFIGURATION
# =============================================================================

# Similarity thresholds for matching
SIMILARITY_THRESHOLDS = {
    "title_similarity": 0.8,      # Minimum title similarity score
    "author_similarity": 0.7,     # Minimum author similarity score  
    "year_tolerance": 1,           # Years difference tolerance
    "overall_match": 0.75,         # Minimum overall match score
    "minimum_confidence": 0.6      # Minimum confidence for uncertain matches
}

# Weights for calculating overall similarity score
SIMILARITY_WEIGHTS = {
    "title": 0.4,     # Title similarity weight
    "authors": 0.3,   # Author similarity weight
    "year": 0.2,      # Year similarity weight
    "doi": 0.1        # DOI similarity weight
}

# Error classification
ERROR_TYPES = {
    "NOT_FOUND": "Citation not found in any database",
    "TITLE_MISMATCH": "Title differs from database record",
    "AUTHOR_MISMATCH": "Author(s) differ from database record", 
    "YEAR_MISMATCH": "Publication year differs from database record",
    "JOURNAL_MISMATCH": "Journal/venue differs from database record",
    "DOI_INVALID": "DOI not found or invalid",
    "FORMAT_ERROR": "Citation format not recognized",
    "INCOMPLETE": "Citation missing required information"
}

# =============================================================================
# APPLICATION CONFIGURATION  
# =============================================================================

# File upload limits
MAX_FILE_SIZE_MB = 50              # Maximum file size in MB
SUPPORTED_FORMATS = [".pdf", ".docx"]  # Supported document formats
MAX_CITATIONS_DEFAULT = 50         # Default max citations to process
MAX_CITATIONS_LIMIT = 200          # Hard limit for citations

# Processing configuration
DEFAULT_RATE_LIMIT_DELAY = 1.0     # Delay between API calls (seconds)
REQUEST_TIMEOUT = 30               # API request timeout (seconds)
MAX_RETRIES = 3                    # Max retries for failed requests

# UI Configuration
APP_TITLE = "📚 Bibliography Checker"
APP_DESCRIPTION = "Verifica automatica e accurata delle tue bibliografie accademiche"
SIDEBAR_INFO = """
**Come funziona:**
1. Carica il tuo PDF o DOCX
2. Il sistema estrae automaticamente le citazioni  
3. Ogni citazione viene verificata su database accademici
4. Ricevi un report dettagliato con errori e suggerimenti
"""

# Visualization colors
COLORS = {
    "verified": "#38a169",     # Green
    "error": "#e53e3e",        # Red  
    "not_found": "#d69e2e",    # Orange
    "uncertain": "#805ad5",    # Purple
    "primary": "#667eea",      # Blue
    "secondary": "#764ba2"     # Purple
}

# =============================================================================
# ADVANCED CONFIGURATION
# =============================================================================

# Cache configuration (if implementing caching)
CACHE_ENABLED = True
CACHE_TTL_HOURS = 24               # Cache time-to-live in hours
CACHE_MAX_SIZE = 1000              # Max number of cached results

# Logging configuration
LOG_LEVEL = "INFO"                 # DEBUG, INFO, WARNING, ERROR
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Feature flags
FEATURES = {
    "enable_ml_similarity": False,     # Use ML models for similarity (requires additional deps)
    "enable_batch_processing": False,  # Allow multiple file uploads
    "enable_user_auth": False,         # User authentication (future feature)
    "enable_analytics": False,         # Usage analytics (future feature)
    "enable_pdf_ocr": False           # OCR for scanned PDFs (requires tesseract)
}

# Development settings
DEBUG_MODE = os.getenv("DEBUG", "False").lower() == "true"
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")  # development, staging, production

# =============================================================================
# VALIDATION FUNCTIONS
# =============================================================================

def validate_config() -> List[str]:
    """Validate configuration and return list of warnings/errors"""
    warnings = []
    
    # Check API keys
    if not SCOPUS_API_KEY:
        warnings.append("Scopus API key not configured - premium database access disabled")
    
    if not IEEE_API_KEY:
        warnings.append("IEEE API key not configured - IEEE Xplore access disabled")
    
    # Check thresholds
    if SIMILARITY_THRESHOLDS["overall_match"] > 1.0 or SIMILARITY_THRESHOLDS["overall_match"] < 0.0:
        warnings.append("Invalid overall_match threshold - should be between 0.0 and 1.0")
    
    # Check weights sum to 1.0
    total_weight = sum(SIMILARITY_WEIGHTS.values())
    if abs(total_weight - 1.0) > 0.01:
        warnings.append(f"Similarity weights sum to {total_weight}, should sum to 1.0")
    
    return warnings

def get_enabled_databases() -> Dict:
    """Get dictionary of enabled databases"""
    enabled = {}
    
    # Add free databases
    for db_id, config in FREE_DATABASES.items():
        if config["enabled"]:
            enabled[db_id] = config
    
    # Add premium databases (only if API key available)
    for db_id, config in PREMIUM_DATABASES.items():
        if config["enabled"]:
            enabled[db_id] = config
    
    return enabled

def get_database_info() -> str:
    """Get formatted string of available databases"""
    enabled_dbs = get_enabled_databases()
    
    info = "**Database disponibili:**\n"
    for db_id, config in enabled_dbs.items():
        info += f"- **{config['name']}**: {config['description']}\n"
    
    if len(enabled_dbs) < len(FREE_DATABASES) + len(PREMIUM_DATABASES):
        info += "\n*Configura API keys per accedere a più database*"
    
    return info

# =============================================================================
# EXPORT CONFIGURATION SUMMARY
# =============================================================================

def print_config_summary():
    """Print configuration summary for debugging"""
    print("=" * 50)
    print("BIBLIOGRAPHY CHECKER CONFIGURATION")
    print("=" * 50)
    
    print(f"Environment: {ENVIRONMENT}")
    print(f"Debug Mode: {DEBUG_MODE}")
    print(f"Max File Size: {MAX_FILE_SIZE_MB}MB")
    print(f"Supported Formats: {', '.join(SUPPORTED_FORMATS)}")
    
    print("\nEnabled Databases:")
    for db_id, config in get_enabled_databases().items():
        print(f"  - {config['name']}")
    
    print(f"\nSimilarity Thresholds:")
    for key, value in SIMILARITY_THRESHOLDS.items():
        print(f"  - {key}: {value}")
    
    warnings = validate_config()
    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"  ⚠️  {warning}")
    
    print("=" * 50)

if __name__ == "__main__":
    print_config_summary()
