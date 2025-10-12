from src.services.http_client import post_json
from src.services.polling import poll_job
from src.config.constants import OCR_CHECK_AND_INFER_ID
from src.config.settings import MOCK


def extract(image_b64: str) -> str:
	if MOCK:
		return "Label: Fertilizer 50kg\nUse as directed"
	payload = {"imageContent": image_b64}
	path = f"ocr/{OCR_CHECK_AND_INFER_ID}/checkOcrStatusAndInfer"
	data = post_json(path, payload)
	if "jobId" in data:
		status_path = f"ocr/{OCR_CHECK_AND_INFER_ID}/status"
		done = poll_job(status_path, data["jobId"])
		return done.get("extractedText") or done.get("text") or ""
	return data.get("extractedText") or data.get("text") or ""