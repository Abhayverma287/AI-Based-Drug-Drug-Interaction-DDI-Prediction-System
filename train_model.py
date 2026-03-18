import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/ddi_dataset.csv")

X = df[['Drug_A','Drug_B']]
y = df['Interaction']

# Convert categorical to numeric
X = pd.get_dummies(X)

# Save feature names
joblib.dump(X.columns.tolist(), "models/feature_columns.pkl")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()

model.fit(X_train, y_train)

joblib.dump(model, "models/ddi_model.pkl")

print("Model trained successfully")