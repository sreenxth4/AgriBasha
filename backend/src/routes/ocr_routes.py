import base64
from flask import Blueprint, request, jsonify
from src.services.ocr_service import extract
from src.services.mt_service import translate as mt_translate

ocr_bp = Blueprint("ocr", __name__)


@ocr_bp.post("/ocr")
def ocr_route():
	try:
		f = request.files.get("image")
		target = request.form.get("target")
		if not f:
			return jsonify({"error": "image missing"}), 400
		b64 = base64.b64encode(f.read()).decode("utf-8")
		text = extract(b64)
		out = {"extractedText": text}
		if target:
			# assume OCR returns English by default — adjust if OCR supports language param
			out["translatedText"] = mt_translate(text, "en", target)
		return jsonify(out)
	except Exception as e:
		return jsonify({"error": str(e)}), 500