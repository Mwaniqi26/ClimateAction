# 🧠 AI for Sustainable Development - Week 2 Starter Project
# 📊 Predicting CO₂ Emissions Using Linear Regression

# --- Step 1: Install & Import Libraries ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# --- Step 2: Load Sample Dataset ---
# Sample data: Replace this with a larger dataset for deeper analysis
data = {
    'Year': [2000, 2005, 2010, 2015, 2020],
    'Energy_Consumption': [120, 140, 170, 200, 230],  # Example energy data (TWh)
    'Industrial_Activity': [300, 340, 400, 460, 520],  # Industrial index
    'CO2_Emissions': [2.5, 2.8, 3.5, 4.2, 5.1]  # CO₂ emissions in gigatonnes
}
df = pd.DataFrame(data)

print("📊 Sample Data Preview:")
print(df)

# --- Step 3: Feature Selection ---
X = df[['Energy_Consumption', 'Industrial_Activity']]
y = df['CO2_Emissions']

# --- Step 4: Train/Test Split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Step 5: Train the Model ---
model = LinearRegression()
model.fit(X_train, y_train)

# --- Step 6: Make Predictions ---
y_pred = model.predict(X_test)

# --- Step 7: Evaluation ---
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"\n📈 Model Evaluation:")
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Root Mean Squared Error (RMSE): {rmse}")

# --- Step 8: Visualization ---
plt.figure(figsize=(8, 5))
plt.plot(df['Year'], df['CO2_Emissions'], marker='o', label='Actual CO₂ Emissions')
plt.plot(df['Year'][-len(y_pred):], y_pred, marker='x', linestyle='--', label='Predicted CO₂')
plt.xlabel("Year")
plt.ylabel("CO₂ Emissions (Gt)")
plt.title("Actual vs Predicted CO₂ Emissions")
plt.legend()
plt.grid(True)
plt.show()

# --- Step 9: Ethical Reflection (Markdown in report) ---
# Example: "This model is a simplification. For real-world accuracy,
# global datasets with more countries and variables should be used.
# Emission data should also include social and economic contexts."

https://colab.research.google.com/drive/1LbxEPfFflZHD2COxGrKZG7uU8ESheYeo?usp=sharing