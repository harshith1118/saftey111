import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file if it exists (local development)
env_path = Path('.') / '.env'
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

# On Streamlit Cloud, keys are available directly in os.environ
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def validate_config():
    """
    Checks if all required environment variables are set.
    """
    missing = []
    # Re-check os.environ in case they were set after module load
    vt_key = os.getenv("VIRUSTOTAL_API_KEY")
    gemini_key = os.getenv("GEMINI_API_KEY")
    
    if not vt_key:
        missing.append("VIRUSTOTAL_API_KEY")
    if not gemini_key:
        missing.append("GEMINI_API_KEY")
    
    return missing
