# 🌾 AgriMitra – Multilingual AI Translator using Bhashini APIs

AgriMitra is a multilingual AI translation web app that integrates **Bhashini’s ASR, MT, TTS, and OCR** models via **AnuvaadHub APIs**.  
It enables **speech-to-speech, text-to-text, and image-to-text translation** across major Indian languages such as **Telugu, Hindi, Tamil, and English** — tailored for **agriculture, healthcare, and tourism** scenarios.

---

## 🧩 Features
✅ **Speech Translator (ASR → MT → TTS)**  
Convert spoken language into translated text and speech output.

✅ **Document/Image Translator (OCR → MT)**  
Upload an image or scanned document and get the extracted and translated text instantly.

✅ **Text Translator (MT → optional TTS)**  
Translate typed or pasted text between supported languages.

✅ **Multi-language Support**  
Supports Telugu (te), Hindi (hi), Tamil (ta), and English (en).

✅ **Clean UI with Three Tabs**  
Voice, Document, and Text modes for quick switching.

✅ **Ready-to-Deploy Backend (Flask)** and **Frontend (React + Vite)**

---

## 🏗️ Architecture Overview

**Tech Stack**
- **Frontend:** React (Vite + TypeScript)
- **Backend:** Python (Flask, Flask-CORS)
- **APIs:** Bhashini / AnuvaadHub (ASR, MT, TTS, OCR)
- **Deployment:** Localhost

**Flowchart**

---

## 🚀 Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/agribasha.git
cd agribasha
BHASHINI_API_KEY=your_key_here
BHASHINI_BASE_URL=https://canvas.iiit.ac.in/sandbox/beprod
PORT=5000
cd backend
python -m venv .venv
# Activate virtual environment
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
python app.py
cd frontend
npm install
npm run dev
