from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os

# Initialize FastAPI app
app = FastAPI(title="Iris Classifier API")

# Load model (we'll add the model file later)
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Define request/response schema
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Prediction endpoint
@app.post("/predict")
async def predict(features: IrisFeatures):
    features_array = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]]
    prediction = model.predict(features_array)[0]
    return {"prediction": int(prediction)}
