🌱 AI-Powered LCA (Life Cycle Assessment) Tool

An AI-driven platform to calculate Carbon Footprint and generate Sustainability Reports for products and projects. The tool uses Machine Learning & Backend APIs to process lifecycle data and provides real-time CO₂ emission analysis with a modern frontend dashboard.

🚀 Deployed on: Vercel (Frontend)
 & Railway (Backend)

📂 Project Structure
LCA-Project/
│
├── frontend/               # React + Vite frontend
│   ├── src/
│   │   ├── Pages/          # All page components
│   │   │   ├── Dashboard.jsx
│   │   │   ├── PredictionForm.tsx
│   │   │   ├── Reports.jsx
│   │   │   └── About.jsx
│   │   ├── components/     # Reusable UI components (Button, Card, Footer, Navbar etc.)
│   │   ├── assets/         # Images, icons, illustrations
│   │   ├── styles/         # Global styles, Tailwind configs
│   │   ├── services/       # API call logic (fetch requests to backend)
│   │   ├── utils/          # Helpers, constants
│   │   ├── app.jsx         # Root App component
│   │   ├── main.jsx        # Entry file
│   │   └── config.js       # Backend API URL (hardcoded / .env)
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
├── backend/                # Python backend (FastAPI / Flask)
│   ├── main.py             # Entry point API server
│   ├── requirements.txt    # Dependencies
│   ├── lca_model.pkl       # Trained ML model (if applicable)
│   ├── utils/              # Helper functions for calculations
│   └── Dockerfile          # Deployment config
│
├── README.md               # Documentation (this file)
└── LICENSE

⚡ Features

🌿 AI-Powered LCA – Analyze lifecycle stages of a product.

📊 Real-time Carbon Footprint – Instant CO₂ emission calculations.

📑 Smart Reports – Export detailed sustainability reports.

📡 Backend API – REST API for lifecycle prediction & report generation.

🎨 Modern UI – Built with React, TailwindCSS, and Framer Motion.

☁️ Deployed – Frontend (Vercel) + Backend (Railway).

🛠️ Tech Stack

Frontend

React.js + Vite

Tailwind CSS + shadcn/ui

Framer Motion (animations)

Lucide React (icons)

Backend

Python 3.12

FastAPI / Flask

Scikit-learn (ML models)

Pandas / NumPy (data processing)

Deployment

Vercel → Frontend

Railway → Backend

⚙️ How It Works

User Input (Frontend)

Fill lifecycle details in Prediction Form:

Material

Route

Quantity

Energy (MWh)

Transport Distance (km)

End of Life Process

Stage-wise Energy

Request Sent to Backend

Frontend sends JSON payload to backend API:

{
  "material": "Steel",
  "route": "Air",
  "quantity": 100,
  "energy_mwh": 50,
  "transport_km": 200,
  "end_of_life": "Recycle",
  "process_stage1_energy": 20
}


Backend Processing

Parses input

Runs ML/Rule-based model for emission calculations

Returns prediction response:

{
  "carbon_emission": 1420.5,
  "stage_breakdown": {
    "production": 700,
    "transport": 450,
    "end_of_life": 270.5
  }
}


Frontend Visualization

Results shown in dashboard charts, graphs, and reports.

🚀 Deployment Steps
🔹 Backend (Railway)

Push backend code to GitHub.

Go to Railway
 → Create New Project → Deploy from GitHub.

Add environment variables (if needed).

Deploy → Copy backend URL (e.g., https://lca-backend-production-729a.up.railway.app).

🔹 Frontend (Vercel)

Push frontend code to GitHub.

Go to Vercel
 → New Project → Import GitHub repo.

Add VITE_BACKEND_URL in Vercel Environment Variables:

VITE_BACKEND_URL=https://lca-backend-production-729a.up.railway.app


Deploy → Get live link.

📸 Screenshots
Landing Page<img width="1340" height="624" alt="image" src="https://github.com/user-attachments/assets/0876e057-79ea-4144-82fe-ff7914805211" />



(Modern UI with hero section, features, impact stats)

Prediction Form

(User fills lifecycle data and hits Predict)

Dashboard

(Displays CO₂ emissions, reports, and charts)

📖 Usage
# Clone repository
git clone https://github.com/yourusername/lca-project.git
cd lca-project

# Setup Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# Setup Frontend
cd ../frontend
npm install
npm run dev


Visit: http://localhost:5173

🤝 Contributing

Fork the repo

Create a new branch (feature-new)

Commit changes

Push and create PR

📜 License

MIT License © 2025 Tarun Juneja
