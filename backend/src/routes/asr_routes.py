import base64
from flask import Blueprint, request, jsonify
from src.services.asr_service import infer_asr

asr_bp = Blueprint("asr", __name__)


@asr_bp.post("/speech-to-text")
def speech_to_text():
	try:
		f = request.files.get("audio")
		lang = request.form.get("lang") or request.args.get("lang") or "te"
		if not f:
			return jsonify({"error": "audio missing"}), 400
		b64 = base64.b64encode(f.read()).decode("utf-8")
		text = infer_asr(b64, lang)
		return jsonify({"text": text, "lang": lang})
	except Exception as e:
		return jsonify({"error": str(e)}), 500