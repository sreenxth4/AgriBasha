from src.services.http_client import post_json
from src.services.polling import poll_job
from src.config.constants import MT_CHECK_AND_INFER_ID
from src.config.settings import MOCK


def translate(text: str, source="te", target="en") -> str:
	if MOCK:
		# small demo phrase map so the UI can show realistic sample translations
		_phrase_map_raw = {
			('en', 'te'): {
				"what is pesticides?": "పెస్టిసైడ్లు అంటే ఏమిటి?",
				"what are pesticides?": "పెస్టిసైడ్లు అంటే ఏమిటి?",
				"what is pesticide?": "పెస్టిసైడ్లు అంటే ఏమిటి?",
				"what is pesticides": "పెస్టిసైడ్లు అంటే ఏమిటి?",
			},
			('en', 'hi'): {
				"what is pesticides?": "कीटनाशक क्या हैं?",
			},
		}

		# normalize helper: lowercase, remove punctuation, collapse spaces
		import re
		def norm(s: str) -> str:
			if not s:
				return ''
			s2 = s.lower()
			s2 = re.sub(r"[^a-z0-9\s]", "", s2)
			s2 = re.sub(r"\s+", " ", s2).strip()
			return s2

		# build normalized phrase map for fast matching
		_phrase_map = {}
		for k, d in _phrase_map_raw.items():
			_phrase_map[k] = {norm(k2): v for k2, v in d.items()}

		k = (source.lower(), target.lower())
		normalized = norm(text)
		# direct match
		if k in _phrase_map and normalized in _phrase_map[k]:
			return _phrase_map[k][normalized]
		# simple singular fallback: try removing trailing 's' from the last token
		parts = normalized.split()
		if parts:
			last = parts[-1]
			if last.endswith('s'):
				parts[-1] = last[:-1]
				candidate = ' '.join(parts)
				if k in _phrase_map and candidate in _phrase_map[k]:
					return _phrase_map[k][candidate]
		# default mock behavior: tag the text so it's obvious it's simulated
		return f"[mock-{source}->{target}] " + text
	payload = {"text": text, "source": source, "target": target}
	path = f"mt/{MT_CHECK_AND_INFER_ID}/checkModelStatusAndInfer"
	data = post_json(path, payload)
	if "jobId" in data:
		status_path = f"mt/{MT_CHECK_AND_INFER_ID}/status"
		done = poll_job(status_path, data["jobId"])
		return done.get("translatedText") or done.get("output") or ""
	return data.get("translatedText") or data.get("output") or ""