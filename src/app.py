from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from src.predict import predict_fraud


app = FastAPI(
    title="Fraud Detection API",
    description="API for detecting fraudulent transactions using XGBoost",
    version="1.0.0"
)


# Servir les fichiers HTML/CSS/JS
app.mount("/static", StaticFiles(directory="static"), name="static")


class Transaction(BaseModel):
    step: int
    type: str
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/predict")
def predict(transaction: Transaction):

    result = predict_fraud(
        step=transaction.step,
        type=transaction.type,
        amount=transaction.amount,
        oldbalanceOrg=transaction.oldbalanceOrg,
        newbalanceOrig=transaction.newbalanceOrig,
        oldbalanceDest=transaction.oldbalanceDest,
        newbalanceDest=transaction.newbalanceDest
    )

    return result