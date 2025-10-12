import os

from dotenv import load_dotenv

load_dotenv()

# Try to load .env from the project root (backend) in case the process was started
# from a different working directory. This ensures local development works when
# running `python app.py` from outside the backend folder.
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parents[2]
dotenv_path = BASE_DIR / '.env'
if dotenv_path.exists():
	# second, explicit load to ensure values are available
	load_dotenv(dotenv_path=str(dotenv_path))

BHASHINI_API_KEY = os.getenv("BHASHINI_API_KEY")

BHASHINI_BASE_URL = os.getenv("BHASHINI_BASE_URL", "https://canvas.iiit.ac.in/sandbox/beprod")

import re

# parse PORT robustly: allow invisible chars by extracting the first run of digits
_port_raw = os.getenv("PORT", "5000") or "5000"
m = re.search(r"(\d+)", _port_raw)
if m:
	PORT = int(m.group(1))
else:
	try:
		PORT = int(_port_raw.strip())
	except Exception:
		raise ValueError(f"Invalid PORT value: {_port_raw!r}")

# Determine mock mode early so we only require the API key when running live
MOCK = os.getenv("MOCK", "false").lower() in ("1", "true", "yes")
if MOCK:
    print("[config] RUNNING IN MOCK MODE: external API calls will be simulated")

# Only require BHASHINI_API_KEY when not running in mock mode
if not MOCK and not BHASHINI_API_KEY:
	raise RuntimeError(
		"BHASHINI_API_KEY missing in env. Add your key to backend/.env (BHASHINI_API_KEY=sk_...) or set it in PowerShell before starting the server:\n"
		"$env:BHASHINI_API_KEY='sk_XXXXXXXX' ; python app.py"
	)

print(f"[config] BHASHINI_BASE_URL={BHASHINI_BASE_URL}, PORT={PORT}")