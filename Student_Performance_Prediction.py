import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score 
from sklearn.preprocessing import LabelEncoder 

df = pd.read_csv("student-mat.csv", sep=";") 
print("Original Data:")
print(df.head())
print("\nMissing Values in Each Column:")
print(df.isnull().sum())
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == "object": 
        df[col] = le.fit_transform(df[col])
print("\nAfter Label Encoding:")
print(df.head())

# If G3 >= 10 → Pass (1), else Fail (0)
df["Performance"] = df["G3"].apply(lambda x: 1 if x >= 10 else 0)
X = df.drop(["G3", "Performance"], axis=1) 
y = df["Performance"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000)  
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))