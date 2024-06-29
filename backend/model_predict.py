import joblib
import pandas as pd
from flask import Flask, request, jsonify
import os

# Check current working directory
print("Current Working Directory:", os.getcwd())

# Load the trained model
model_path = 'battery_degradation_model.pkl'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"{model_path} not found. Please ensure the file exists and the path is correct.")

model = joblib.load(model_path)

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(df)
    return jsonify({'degradation': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
