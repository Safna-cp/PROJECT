import pandas as pd  # for data manipulation
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression # for regression model
from sklearn.metrics import classification_report ,accuracy_score# for model evaluation
from sklearn.preprocessing import LabelEncoder # for encoding categorical variables


# 1) Load the dataset
columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
df=pd.read_csv("car.data", names=columns)
print("Original Data:")
print(df.head())

# Data Preprocessing
print("\nMissing Values in Each Column:")

print(df.isnull().sum())
le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])

print("\nAfter Label Encoding:")
print(df.head())

# Split features (X) and target (y)
X = df.drop("class", axis=1)  # all columns except 'class'
y = df["class"]        # target column

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)

model=LogisticRegression()
model.fit(X_train, y_train)
y_pred=model.predict(X_test)


print("\naccuracy:",accuracy_score(y_test,y_pred))
print("\nclassification report:\n",classification_report(y_test,y_pred))


