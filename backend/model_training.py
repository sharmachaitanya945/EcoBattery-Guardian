import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Generate synthetic data for demonstration
data = {
    'temperature': [20.5, 21.0, 22.1, 23.4, 24.8, 26.0, 27.3, 28.1],
    'voltage': [4.1, 4.0, 3.9, 3.8, 3.7, 3.6, 3.5, 3.4],
    'current': [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7],
    'degradation': [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08]
}
df = pd.DataFrame(data)

# Train-test split
X = df[['temperature', 'voltage', 'current']]
y = df['degradation']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'battery_degradation_model.pkl')
print("Model trained and saved.")
