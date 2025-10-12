from src.services.http_client import post_json
from src.config.constants import ASR_INFER_ID
from src.config.settings import MOCK


def infer_asr(audio_b64: str, lang="te") -> str:
	if MOCK:
		# simple canned response for demo
		return "What a beautiful field"
	payload = {"audioContent": audio_b64, "language": lang}
	path = f"asr/{ASR_INFER_ID}/infer"
	data = post_json(path, payload)
	return data.get("output") or data.get("text") or ""

