
from src.services.http_client import post_json
from src.config.constants import TTS_GENERATE_ID
from src.config.settings import MOCK


def synthesize(text: str, lang="te"):
	if MOCK:
		# Return a tiny 0.1s 8-bit PCM WAV (very short beep/silence) encoded in base64
		# Generated minimal WAV header + data for a short silent clip. This is small and safe for demo.
		sample_b64 = (
			"UklGRiQAAABXQVZFZm10IBAAAAABAAEAESsAACJWAAACABAAZGF0YQAAAAA="
		)
		return sample_b64, 'audio/wav'
	payload = {"text": text, "language": lang, "audioFormat": "wav"}
	path = f"tts/{TTS_GENERATE_ID}/generate"
	data = post_json(path, payload)
	audio_b64 = data.get("audioContent") or data.get("audioBase64") or ""
	mime = data.get("mimeType", "audio/wav")
	return audio_b64, mime

