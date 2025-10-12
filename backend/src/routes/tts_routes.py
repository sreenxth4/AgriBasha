from flask import Blueprint, request, jsonify
from src.services.tts_service import synthesize

tts_bp = Blueprint("tts", __name__)


@tts_bp.post("/text-to-speech")
def tts_route():
	try:
		data = request.get_json(force=True)
		text = data.get("text", "")
		lang = data.get("lang", "te")
		if not text:
			return jsonify({"error": "text required"}), 400
		audio_b64, mime = synthesize(text, lang)
		return jsonify({"audioBase64": audio_b64, "mime": mime, "lang": lang})
	except Exception as e:
		return jsonify({"error": str(e)}), 500