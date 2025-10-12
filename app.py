from flask import Flask
from flask_cors import CORS
from src.routes.health_routes import health_bp
from src.routes.asr_routes import asr_bp
from src.routes.mt_routes import mt_bp
from src.routes.tts_routes import tts_bp
from src.routes.ocr_routes import ocr_bp
from src.config.settings import PORT, MOCK
from src.config.settings import BHASHINI_BASE_URL
import os

app = Flask(__name__)
CORS(app)

app.register_blueprint(health_bp)
app.register_blueprint(asr_bp)
app.register_blueprint(mt_bp)
app.register_blueprint(tts_bp)
app.register_blueprint(ocr_bp)

if __name__ == "__main__":
	# developer-friendly startup info
	verify_ssl = os.getenv("BHASHINI_VERIFY_SSL", "true")
	key_present = bool(os.getenv("BHASHINI_API_KEY"))
	print(f"[startup] MOCK={MOCK}, BHASHINI_BASE_URL={BHASHINI_BASE_URL}, BHASHINI_VERIFY_SSL={verify_ssl}, BHASHINI_API_KEY_present={key_present}")
	app.run(host="0.0.0.0", port=PORT, debug=True)