import joblib
import pandas as pd

model = joblib.load("models/ddi_model.pkl")
columns = joblib.load("models/feature_columns.pkl")

def predict_interaction(drug1, drug2):

    df = pd.DataFrame([[drug1, drug2]], columns=['Drug_A','Drug_B'])

    df = pd.get_dummies(df)

    # Align with training columns
    df = df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(df)

    if prediction[0] == 1:
        return "⚠️ Drug Interaction Detected"
    else:
        return "✅ Safe Combination"