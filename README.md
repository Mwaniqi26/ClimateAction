# ClimateAction
🌍 AI for Sustainable Development: CO₂ Emissions Predictor
Theme: Machine Learning Meets the UN Sustainable Development Goals (SDGs)
SDG Focus: SDG 13 – Climate Action
Goal: Build a supervised machine learning model that forecasts CO₂ emissions to support climate policy and sustainability initiatives.

📌 Project Overview
This project demonstrates how AI and machine learning can help address climate change by forecasting carbon dioxide (CO₂) emissions using real-world historical data. The model uses Linear Regression to analyze trends and predict future emissions for a given country or globally.

🧰 Tools & Technologies
Tool	Purpose
Python	Programming language
Google Colab	Development and testing platform
pandas	Data loading and manipulation
scikit-learn	Model training and evaluation
matplotlib	Data visualization
OurWorldInData	Source of CO₂ emissions data

📊 Dataset
Source: Our World in Data - CO₂ and Greenhouse Gas Emissions
Format: CSV
Features Used:

year

co2 (total emissions in million tonnes)

co2_per_capita (for modeling emissions based on population behavior)

🧠 Machine Learning Model
Type: Supervised Learning (Regression)

Model: Linear Regression

Target: Predict co2 based on co2_per_capita or other factors

✅ Project Workflow
Import libraries and load CO₂ dataset

Clean and filter data (e.g., select a country like Kenya or USA)

Select features and target variable

Train/test split

Train Linear Regression model

Predict CO₂ emissions and evaluate performance (MAE, RMSE)

Visualize actual vs predicted trends

Reflect on social impact and ethical risks

📈 Sample Output
MAE: 0.22

RMSE: 0.31

Insights: Emissions rising steadily post-2010; predictive model shows consistent forecasting power with minimal error.

⚖️ Ethical Reflection
Data is richer for developed countries, potentially underrepresenting developing nations.

A single variable (like per capita emissions) may oversimplify policy decisions.

Models should be used to support—not replace—human climate policy action.

🔍 How to Run This Notebook
Open Google Colab

Upload the notebook and CSV file

Run all cells (Shift + Enter)

Explore predictions and visualizations

Modify country filters or features for new insights

📝 License & Credits
Data by Our World in Data

Project for educational use under MIT License

🙌 Acknowledgments
Thanks to the UN SDG AI challenge team for encouraging meaningful innovation through machine learning and sustainability.

