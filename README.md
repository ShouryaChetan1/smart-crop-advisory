# Smart Crop Advisory System for Indian Small & Marginal Farmers

A multilingual, voice-first mobile solution to empower small and marginal farmers in India with scientific crop decisions, pest/disease diagnosis, real-time weather/market data, and offline-first usability.

## 🚀 MVP Features
- Voice-driven registration & navigation (Hindi, Punjabi, English)
- Personalized crop recommendations (season/soil/weather)
- Weather and market price dashboard
- Offline-first UI, large icons, minimal text
- Pest/disease image diagnosis (coming soon)
- Feedback loop for user improvement

## 🛠️ Tech Stack
- **Frontend:** React Native (Android), PWA fallback
- **Backend:** FastAPI (Python), REST API
- **Database:** MongoDB Atlas, local device cache
- **AI/ML:** RandomForest crop adviser (Python), MobileNetV2 pest classifier (TF Lite)
- **APIs:** OpenWeatherMap, Agmarknet, Google Translate
- **Voice:** Android SpeechRecognizer, Web Speech API

## 📦 Structure

```
smart-crop-advisory/
│
├── backend/      # FastAPI app, REST endpoints, ML model services
├── frontend/     # React Native app, PWA fallback, voice modules, offline logic
├── ml/           # Crop recommender, pest classifier, training notebooks
├── docs/         # API docs, UX flow, wireframes, diagrams, pitch deck
└── README.md     # This file
```

## 🗂️ Docs
- See `docs/API.md` for REST endpoints.
- See `docs/UX.md` for user journey & wireframes.
- See `docs/pitch_deck/` for hackathon/demo slides.

---
For install and usage, see `backend/README.md` and `frontend/README.md`.