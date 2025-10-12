from flask import Blueprint, request, jsonify
from src.services.mt_service import translate as mt_translate

mt_bp = Blueprint("mt", __name__)


@mt_bp.post("/translate")
def translate_route():
	try:
		data = request.get_json(force=True)
		text = data.get("text", "")
		source = data.get("source", "te")
		target = data.get("target", "en")
		if not text:
			return jsonify({"error": "text required"}), 400
		translated = mt_translate(text, source, target)
		return jsonify({"translatedText": translated, "source": source, "target": target})
	except Exception as e:
		return jsonify({"error": str(e)}), 500