# main.py
import matplotlib
matplotlib.use("Agg")  # Use non-GUI backend
import matplotlib.pyplot as plt

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import FileResponse
import pickle
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import uuid
import io
from PIL import Image

# ---------------------------
# Load the extended model
with open("lca_model_extended.pkl", "rb") as f:
    model = pickle.load(f)

# ---------------------------
# FastAPI instance
app = FastAPI(title="AI-powered LCA Extended API with Reports")

# ---------------------------
# Configure CORS for Lovable sandbox
origins = [
    "https://*.lovable.dev",  # allows all lovable.dev subdomains
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔥 for testing; replace with origins list in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# Input schema for extended model
class LCAInput(BaseModel):
    material: str
    route: str
    quantity: float
    energy_mwh: float
    transport_km: float
    end_of_life: str
    process_stage1_energy: float = 0
    process_stage2_energy: float = 0
    process_stage3_energy: float = 0

# ---------------------------
# Home route
@app.get("/")
def home():
    return {"message": "Welcome to the AI-powered Extended LCA Prototype API with Reports!"}

# ---------------------------
# Predict endpoint
@app.post("/predict")
def predict(data: LCAInput):
    try:
        X = pd.DataFrame([data.dict()])
        prediction = model.predict(X)[0]

        result = {
            "co2_kg": round(prediction[0], 2),
            "water_l": round(prediction[1], 2),
            "waste_kg": round(prediction[2], 2),
            "recycled_content": round(prediction[3], 2),
            "resource_efficiency": round(prediction[4], 2),
            "extended_life": round(prediction[5], 2),
            "reuse_potential": round(prediction[6], 2)
        }
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ---------------------------
# Report generation endpoint
@app.post("/report")
def generate_report(data: LCAInput):
    try:
        X = pd.DataFrame([data.dict()])
        prediction = model.predict(X)[0]
        co2, water, waste, recycled, efficiency, life, reuse = prediction

        # Unique filename
        filename = f"lca_report_{uuid.uuid4().hex[:8]}.pdf"

        # Initialize PDF
        c = canvas.Canvas(filename, pagesize=A4)
        width, height = A4

        # Title
        c.setFont("Helvetica-Bold", 18)
        c.drawString(50, height - 50, "Life Cycle Assessment (LCA) Report")

        # Input details
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, height - 90, "Input Details:")
        c.setFont("Helvetica", 12)
        y_pos = height - 110
        for key, value in data.dict().items():
            c.drawString(60, y_pos, f"{key.replace('_',' ').title()}: {value}")
            y_pos -= 20

        # Output details
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y_pos-10, "Predicted Environmental & Circularity Indicators:")
        c.setFont("Helvetica", 12)
        y_pos -= 30
        outputs = {
            "CO2 Emissions (kg)": co2,
            "Water Consumption (L)": water,
            "Waste Generated (kg)": waste,
            "Recycled Content (%)": recycled,
            "Resource Efficiency": efficiency,
            "Extended Product Life (years)": life,
            "Reuse Potential (%)": reuse
        }
        for key, value in outputs.items():
            c.drawString(60, y_pos, f"{key}: {round(value,2)}")
            y_pos -= 20

        # ------------------------------
        # Bar chart for environmental outputs
        plt.figure(figsize=(4,3))
        plt.bar(["CO2","Water","Waste"], [co2, water, waste], color=["red","blue","green"])
        plt.title("Environmental Indicators")
        buf = io.BytesIO()
        plt.savefig(buf, format='PNG', bbox_inches='tight')
        plt.close()
        buf.seek(0)
        img = Image.open(buf)
        c.drawInlineImage(img, 350, height - 250, width=200, height=150)
        buf.close()

        # Pie chart for recycled content
        plt.figure(figsize=(4,4))
        plt.pie([recycled, 100-recycled], labels=["Recycled","Non-Recycled"], autopct='%1.1f%%', colors=["gold","lightgrey"])
        plt.title("Recycled Content")
        buf2 = io.BytesIO()
        plt.savefig(buf2, format='PNG', bbox_inches='tight')
        plt.close()
        buf2.seek(0)
        img2 = Image.open(buf2)
        c.drawInlineImage(img2, 350, height - 450, width=200, height=150)
        buf2.close()

        # Recommendations
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y_pos-10, "Recommendations:")
        c.setFont("Helvetica", 12)
        y_pos -= 30
        if recycled < 50:
            c.drawString(60, y_pos, "- Increase recycled content to reduce emissions.")
            y_pos -= 20
        if co2 > 5000:
            c.drawString(60, y_pos, "- Consider renewable energy sources to cut CO2.")
            y_pos -= 20
        if waste > 200:
            c.drawString(60, y_pos, "- Optimize process to minimize waste generation.")
            y_pos -= 20
        if efficiency < 50:
            c.drawString(60, y_pos, "- Improve resource efficiency by optimizing stages.")
            y_pos -= 20

        # Save PDF
        c.save()

        return FileResponse(filename, media_type="application/pdf", filename=filename)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
