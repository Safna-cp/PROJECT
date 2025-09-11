import pandas as pd  # for data manipulation
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression # for regression model
from sklearn.metrics import mean_squared_error, r2_score # for model evaluation
import matplotlib.pyplot as plt
import seaborn as sns


# 1) Load the dataset
data = pd.read_csv(r"C:\Users\pc42\Desktop\DATA SCIENCE\PROJECT\50_startups_sample (6).csv") 
print(data.head())

# data preparation
# Convert categorical column 'State' into dummy variables
data = pd.get_dummies(data, drop_first=True) 


# Features and Target
X = data.drop(columns=['Profit'])
y = data['Profit']


# Split into training & testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3) Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# 4) Model Evaluation
model.fit(X, y)
y_pred = model.predict(X)

print("R² Score:", r2_score(y, y_pred))
print("MSE:", mean_squared_error(y, y_pred))

# Scatter plot (Actual vs Predicted)
plt.figure(figsize=(6,5))
sns.scatterplot(x=y, y=y_pred)
plt.xlabel("Actual Profit")
plt.ylabel("Predicted Profit")
plt.title("Actual vs Predicted Profit")
plt.show()

# 5) Prediction with user input
print("\nStartup Profit Prediction")
RND = float(input("Enter R&D Spend: "))
Admin = float(input("Enter Administration Spend: "))
Marketing = float(input("Enter Marketing Spend: "))
State = input("Enter State (New York / California / Florida): ")

# Create a dataframe for prediction
user_data = {
    "R&D Spend": RND,
    "Administration": Admin,
    "Marketing Spend": Marketing,
    "State_Florida": 1 if State == "Florida" else 0,
    "State_New York": 1 if State == "New York" else 0
}
user_df = pd.DataFrame([user_data])
prediction = model.predict(user_df)
print(f"Predicted Profit: ${prediction[0]:.2f}")






