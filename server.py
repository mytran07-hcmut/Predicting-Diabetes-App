from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

# Load model and scaler
with open("model.pkl", "rb") as f:
    model, scaler = pickle.load(f)


# Input schema
class PatientData(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float


@app.get("/")
def root():
    return {"message": "Diabetes Prediction API is running"}


@app.post("/predict")
def predict(data: PatientData):
    features = [[
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]]

    scaled_features = scaler.transform(features)
    prediction = int(model.predict(scaled_features)[0])

    return {"prediction": prediction}