import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1) Create dataset (or load from CSV)
# Example dataset: GRE, TOEFL, CGPA, Research (0=No, 1=Yes), Admit (target)
data = {
    'GRE_Score': [320, 310, 305, 330, 340, 290, 300, 315, 325, 335],
    'TOEFL_Score': [110, 105, 102, 115, 120, 95, 100, 107, 112, 118],
    'CGPA': [8.7, 8.2, 7.9, 9.1, 9.5, 6.8, 7.2, 8.3, 8.9, 9.3],
    'Research': [1, 0, 0, 1, 1, 0, 0, 1, 1, 1],
    'Admit': [1, 0, 0, 1, 1, 0, 0, 1, 1, 1]  # Target column
}

df = pd.DataFrame(data)
print("Original Data:")
print(df.head())

# 2) Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# 3) Split features (X) and target (y)
X = df.drop("Admit", axis=1)
y = df["Admit"]

# 4) Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5) Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# 6) Predictions
y_pred = model.predict(X_test)

# 7) Evaluation
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
