# AgriMitra - Local demo

## Setup

### Backend
```bash
cd backend
python -m venv .venv
# On Windows use: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
cp ../.env.example .env
# edit backend/.env to add BHASHINI_API_KEY
python app.py
