import joblib
import pandas as pd

# Load the trained model
model_path = 'battery_degradation_model.pkl'
model = joblib.load(model_path)

# Example input data
data = {
    "temperature": 25.0,  # Replace with actual value
    "voltage": 3.7,       # Replace with actual value
    "current": 1.5        # Replace with actual value
}

# Convert the data to a DataFrame
df = pd.DataFrame(data, index=[0])

# Make a prediction
prediction = model.predict(df)

# Print the prediction
print(f"Degradation Prediction: {prediction[0]}")
