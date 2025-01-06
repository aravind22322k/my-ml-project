import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

def evaluate_model(model_path, test_data_path):
    model = joblib.load(model_path)
    data = pd.read_csv(test_data_path)
    X = data.drop("target", axis=1)
    y = data["target"]
    predictions = model.predict(X)
    accuracy = accuracy_score(y, predictions)
    print(f"Model Accuracy: {accuracy}")

if __name__ == "__main__":
    evaluate_model("model/model.pkl", "data/processed_data.csv")
