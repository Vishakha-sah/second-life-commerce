# 🛍️ Second Life Commerce — AI Circular Economy Engine

Second Life Commerce is an AI-driven platform designed to facilitate the circular economy by automating the grading, valuation, and routing of used products. Developed for the **Amazon Build On Hackathon (June 2026)**, it leverages Google Gemini's multi-modal capabilities to assess product condition from images and provide intelligent routing decisions (Resell, Refurbish, Donate, Recycle).

## 🚀 Live Demo
- **Frontend:** [https://second-life-commerce.vercel.app/](https://second-life-commerce.vercel.app/)
- **Backend API:** [https://second-life-commerce-gamma.vercel.app/](https://second-life-commerce-gamma.vercel.app/)

## 🛠️ Technology Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) + Python 3.11
- **Frontend:** [React.js](https://reactjs.org/) + Vite + [Tailwind CSS](https://tailwindcss.com/)
- **AI/ML:** [Google Gemini 1.5 Flash API](https://ai.google.dev/)
- **Data Storage:** Lightweight JSON persistence
- **Image Handling:** Python Pillow (Backend) + HTML Canvas (Frontend for annotations)

## 📂 Project Structure

- `backend/`: FastAPI source code, Gemini AI logic, and mock database.
- `frontend/`: React + TypeScript web application.
- `conductor/`: Project planning and tracks documentation.

## ✨ Key Features

- ✅ **AI Image Quality Check:** Rejects poor quality photos (blur, bad lighting) before assessment.
- ✅ **AI Condition Grader:** Gemini-based grading with damage list and confidence scoring.
- ✅ **Dynamic Questionnaire:** AI-generated follow-up questions tailored to detected product damage.
- ✅ **Intelligent Routing:** Decision engine to route items for Resale, Refurbishment, Donation, or Recycling.
- ✅ **Return Regret Predictor:** Predicts cognitive dissonance in returns to encourage keeping items.
- ✅ **CO2 Impact Display:** Shows environmental savings (kg CO2 saved) for every circular action.
- ✅ **Green Points System:** Rewards sustainable choices with redeemable points.
- ✅ **Damage Annotation:** Visual highlights of detected damage directly on product photos.

## 🛠️ Local Setup

### Backend
1. Navigate to the `backend` directory.
2. Create a virtual environment: `python -m venv venv`.
3. Activate the environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux).
4. Install dependencies: `pip install -r requirements.txt`.
5. Set your `GEMINI_API_KEY` in a `.env` file.
6. Start the server: `uvicorn main:app --reload`.

### Frontend
1. Navigate to the `frontend` directory.
2. Install dependencies: `npm install`.
3. Start the development server: `npm run dev`.

## 🌐 Production Deployment Notes

This project is optimized for deployment on **Vercel**:

- **Backend (FastAPI)**: Configured with explicit Pydantic schema generation fixes (`Dict[str, Any]`, `ConfigDict`) to ensure compatibility with serverless environments.
- **Frontend (React)**: Optimized build pipeline with resolved TypeScript dependency and unused variable checks for clean production builds.
- **API Configuration**: The frontend is configured to automatically point to the hosted production API endpoint.

## 📜 License
This project is developed for hackathon purposes. All rights reserved.
