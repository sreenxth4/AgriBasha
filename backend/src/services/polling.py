import time

from src.services.http_client import post_json

def poll_job(status_path: str, jobId: str, tries=10, delay=1.0):
	for _ in range(tries):
		data = post_json(status_path, {"jobId": jobId})
		st = data.get("status") or data.get("state")
		if st and st.upper() in ("COMPLETED", "SUCCESS", "DONE"):
			return data
		time.sleep(delay)
	return {"status": "TIMEOUT"}