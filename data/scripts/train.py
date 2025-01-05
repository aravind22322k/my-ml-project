from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import numpy as np
import pandas as pd


def train_model(data_path, model_path):
    data = pd.read_csv(data_path)
    X = data.drop("class", axis=1)
    y = data["class"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)

if __name__ == "__main__":
    train_model("data/processed_data.csv", "model/model.pkl")
