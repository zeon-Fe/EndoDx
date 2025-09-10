from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np
from utils.helpers import load_model_artifacts, map_symptoms_to_vector
import logging
from fastapi.middleware.cors import CORSMiddleware

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="EndoDx API",
    description="API for endometriosis prediction based on symptoms",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model artifacts once at startup
try:
    model, scaler, features = load_model_artifacts()
    logger.info("Model artifacts loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model artifacts: {str(e)}")
    raise e

class SymptomsRequest(BaseModel):
    symptoms: List[str]

class PredictionResponse(BaseModel):
    prediction: int
    probability: float
    risk_level: str
    message: str

@app.get("/")
async def root():
    return {"message": "EndoDx API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionResponse)
async def predict_endometriosis(request: SymptomsRequest):
    try:
        if not request.symptoms:
            return PredictionResponse(
                prediction=0,
                probability=0.0,
                risk_level="unknown",
                message="No symptoms selected. Please select at least one symptom for prediction."
            )

        # Build input vector
        feature_vec = map_symptoms_to_vector(request.symptoms, features)
        scaled = scaler.transform(feature_vec)

        pred = model.predict(scaled)[0]
        proba = (model.predict_proba(scaled)[0][1]
                 if hasattr(model, "predict_proba")
                 else float(model.decision_function(scaled)[0]))

        # Risk levels
        if proba >= 0.7:
            risk_level = "high"
        elif proba >= 0.4:
            risk_level = "moderate"
        else:
            risk_level = "low"

        message = f"Based on your symptoms, there is a {proba:.1%} likelihood of endometriosis association."

        return PredictionResponse(
            prediction=int(pred),
            probability=float(proba),
            risk_level=risk_level,
            message=message
        )

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)