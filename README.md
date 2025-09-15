
# 🛡️ FraudShield  
AI-powered system to detect, analyze, and combat misinformation & fraud across text, images, and video.

---

## 🚀 Overview  
FraudShield is a **multi-modal misinformation defense platform** that helps users verify the authenticity of online content in real-time.  
It combines **NLP-based fake news detection**, **deepfake analysis**, and **cross-platform verification** into a single accessible dashboard.

---

## ✨ Features  
- 🔍 **Text Analyzer** – Detects misleading or manipulative text  
- 🎥 **Media Analyzer** – Flags deepfakes & altered audio/video  
- 🌐 **Cross Verification** – Confirms claims against trusted data sources  
- 📊 **Real-time Dashboard** – Shows live trends of misinformation spread  
- ⚡ **API-first design** – FastAPI backend with REST endpoints  
- 🎨 **Modern UI** – React (Vite + Tailwind) frontend  

---

## 🏗️ Project Structure  
```
fraudshield/
├── backend/               # FastAPI app
│   ├── app/
│   │   ├── api/           # API endpoints
│   │   ├── core/          # Config & settings
│   │   ├── services/      # NLP/Deepfake analyzers
│   │   └── main.py        # App entry
│   ├── data_ingestion/    # Feed aggregation scripts
│   ├── requirements.txt   # Backend deps
│   └── .env.example
│
├── frontend/              # React + Vite frontend
│   ├── src/
│   │   ├── components/    # Reusable UI blocks
│   │   ├── pages/         # Analyzer & Dashboard
│   │   └── services/      # API wrapper
│   └── package.json
│
├── .github/workflows/     # CI pipelines
├── README.md
└── LICENSE
```

---

## ⚙️ Getting Started  

### 1️⃣ Clone the repo  
```bash
git clone https://github.com/<your-username>/fraudshield.git
cd fraudshield
```

### 2️⃣ Backend Setup (FastAPI)  
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env   # add your NEWSAPI_KEY etc.
uvicorn app.main:app --reload --port 8000
```
📍 API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 3️⃣ Frontend Setup (React + Vite)  
```bash
cd frontend
npm install
cp .env.example .env   # optional: set VITE_API_BASE
npm run dev
```
📍 Frontend runs at: [http://localhost:5173](http://localhost:5173)

---

## 🔑 Environment Variables  
Create `.env` files for both backend & frontend:

**Backend (`backend/.env`)**
```
NEWSAPI_KEY=your_key_here
DATABASE_URL=sqlite:///./fraudshield.db
```

**Frontend (`frontend/.env`)**
```
VITE_API_BASE=http://localhost:8000/api
```

---

## 🤖 API Endpoints (Backend)  
- `POST /api/verify/text` → Verify text/article claims  
- `POST /api/verify/media` → Verify images/videos (deepfake check)  
- `GET  /api/dashboard/feed` → Get aggregated misinformation trends  
- `GET  /healthz` → Health check  

---

## 🛠️ Tech Stack  
- **Backend**: FastAPI, Python  
- **Frontend**: React (Vite), TailwindCSS  
- **CI/CD**: GitHub Actions  
- **Data**: RSS feeds, NewsAPI, custom scrapers  
- **ML/NLP**: HuggingFace transformers (planned), Deepfake detection models (planned)  

---

## ✅ Roadmap  
- [ ] Add pretrained NLP model for fake news detection  
- [ ] Integrate deepfake detection for images/video  
- [ ] Enhance cross-verification logic with fact-check APIs  
- [ ] Dockerize backend & frontend for easier deployment  
- [ ] Deploy demo (Render + Netlify/Vercel)  

---
## 🔗 [View User Workflow](https://claude.site/public/artifacts/58f59450-c1f0-47cb-a5ec-45d9210056c8/embed)
---


## 🤝 Contributing  
We welcome contributions!  
1. Fork the repo  
2. Create a branch (`git checkout -b feat/your-feature`)  
3. Commit your changes (`git commit -m "feat: add new feature"`)  
4. Push to your fork and open a PR 🎉  

---

## 📜 License  
MIT License © 2025 FraudShield Team
