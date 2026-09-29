import os
import joblib
import pandas as pd


# Chemin vers le modèle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "fraud_detection_xgb.pkl"
)


# Charger le modèle et le threshold
artifact = joblib.load(MODEL_PATH)

model = artifact["model"]
threshold = artifact["threshold"]


def predict_fraud(
    step,
    type,
    amount,
    oldbalanceOrg,
    newbalanceOrig,
    oldbalanceDest,
    newbalanceDest
):
    
    transaction = pd.DataFrame([{
        "step": step,
        "type": type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    probability = model.predict_proba(transaction)[0, 1]

    prediction = (
        "FRAUD"
        if probability >= threshold
        else "NORMAL"
    )

    return {
        "prediction": prediction,
        "probability": float(probability),
        "threshold": float(threshold)
    }


if __name__ == "__main__":

    result = predict_fraud(
        step=461,
        type="CASH_OUT",
        amount=6273660.45,
        oldbalanceOrg=6273660.45,
        newbalanceOrig=0,
        oldbalanceDest=763912.31,
        newbalanceDest=7037572.76
    )

    print(result)