import os
import requests
import certifi
import logging

from src.config.settings import BHASHINI_BASE_URL, MOCK

log = logging.getLogger("http_client")


def _get_verify_setting():
	v = os.getenv("BHASHINI_VERIFY_SSL", "true").lower()
	if v in ("0", "false", "no"):
		return False
	return certifi.where()


def _build_headers():
	# Build headers at call-time to pick up any env changes
	api_key = os.getenv("BHASHINI_API_KEY")
	if not MOCK and not api_key:
		raise RuntimeError("BHASHINI_API_KEY missing in env (set BHASHINI_API_KEY in backend/.env or $env:BHASHINI_API_KEY)")
	headers = {"Content-Type": "application/json"}
	if api_key:
		headers["Authorization"] = f"Bearer {api_key}"
	return headers


def post_json(path: str, payload: dict, timeout: int = 60):
	url = f"{BHASHINI_BASE_URL.rstrip('/')}/{path.lstrip('/')}"
	verify = _get_verify_setting()
	headers = _build_headers()
	try:
		log.debug("POST %s (verify=%s)", url, bool(verify))
		r = requests.post(url, json=payload, headers=headers, timeout=timeout, verify=verify)
		r.raise_for_status()
		return r.json()
	except requests.exceptions.SSLError as e:
		log.exception("SSL error when calling %s: %s", url, e)
		raise
	except requests.exceptions.HTTPError as e:
		# Provide a helpful message including status and response text
		body = None
		try:
			body = r.text
		except Exception:
			body = '<unreadable body>'
		log.error("HTTP error %s when calling %s: %s", r.status_code if 'r' in locals() else '??', url, body)
		raise
	except Exception as e:
		log.exception("Error when calling %s: %s", url, e)
		raise

