from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

app = FastAPI()

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class Registration(BaseModel):
    phone: str
    location: Optional[str]
    language: str
    crops_of_interest: Optional[List[str]]

class CropAdvisoryRequest(BaseModel):
    location: str
    season: str
    soil_type: Optional[str]
    rainfall: Optional[float]
    past_crops: Optional[List[str]]

# Endpoints
@app.post("/register")
def register(data: Registration):
    # TODO: Store user registration data in DB
    return {"success": True, "message": "Registered successfully!"}

@app.post("/advisory")
def crop_advisory(data: CropAdvisoryRequest):
    # TODO: ML crop recommendation logic
    # For MVP, return mocked recommendations
    return {
        "recommended_crops": ["Wheat", "Mustard"],
        "sowing_window": "October - November",
        "fertilizer_plan": "DAP 50kg/acre",
        "irrigation_advice": "Irrigate every 10 days"
    }

@app.post("/pest-detect")
async def pest_detect(file: UploadFile = File(...)):
    # TODO: Run pest/disease image classifier
    # Return mock result
    return {
        "prediction": "Aphid infestation",
        "remedy": "Spray neem oil. Remove affected leaves.",
        "confidence": 0.89
    }

@app.get("/weather")
def get_weather(location: str):
    # TODO: Integrate OpenWeatherMap API
    # Mock response
    return {
        "forecast": [
            {"day": "Today", "temp": 32, "rain": "No", "humidity": 70},
            {"day": "Tomorrow", "temp": 31, "rain": "Yes", "humidity": 80}
        ],
        "alert": "Heavy rain expected tomorrow"
    }

@app.get("/market")
def get_market_prices(location: str):
    # TODO: Integrate Agmarknet API
    # Mock response
    return {
        "prices": [
            {"crop": "Wheat", "price": 2100, "unit": "quintal", "favourable": True},
            {"crop": "Mustard", "price": 4800, "unit": "quintal", "favourable": False}
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)