import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn

# ─── Load Dataset ─────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "heart_preprocessing", "heart_preprocessing.csv")

df = pd.read_csv(DATA_PATH)

# ─── Preprocessing ────────────────────────────────────────────────────────────
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ─── Training ─────────────────────────────────────────────────────────────────
mlflow.set_experiment("heart-classification")
mlflow.sklearn.autolog()

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy:.4f}")
