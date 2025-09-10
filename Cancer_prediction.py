import pandas as pd #for data manipulation
from sklearn.datasets import load_breast_cancer #importing breast cancer dataset
from sklearn.model_selection import train_test_split #for splitting the dataset into training and testing sets
from sklearn.linear_model import LogisticRegression # Using Logistic Regression for classification that is true or false
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix #for evaluating the model
import seaborn as sns   #for data visualization
import matplotlib.pyplot as plt #for data visualization

# 1) Data Preparation

# Load the breast cancer dataset
data = load_breast_cancer()     #loading the breast cancer dataset from sklearn
df=pd.DataFrame(data.data, columns=data.feature_names) #converting the dataset into a pandas dataframe
df['target'] = data.target #adding the target variable to the dataframe


# keep only 5 important features + target to predict that is malignant=0 or benign=1(positive/negative)
df_small = df[['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness', 'target']] 



# 2) Model Training/creation

# Split the dataset into features and target variable
X = df_small.drop(columns=['target']) #features
y = df_small['target'] #target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y) #stratify=y to maintain the same proportion of classes in train and test sets

# Initialize and train the Logistic Regression model
model = LogisticRegression() #initializing the model
model.fit(X_train, y_train) #training the model

# evaluation(Make predictions on the test set)
y_pred = model.predict(X_test)  # Predicted class labels (model is a variable)
y_prob = model.predict_proba(X_test)[:, 1]  # Probability estimates for the positive class
print("Model Accuracy:", accuracy_score(y_test, y_pred)) #accuracy of the model
print("\nClassification Report:\n", classification_report(y_test, y_pred)) #detailed classification report

# 3) Model Evaluation

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred) #confusion matrix
plt.figure(figsize=(5,4)) #setting the figure size
sns.heatmap(cm,cmap='Blues', xticklabels=['Malignant', 'Benign'], yticklabels=['Malignant', 'Benign']) #heatmap for confusion matrix
plt.xlabel('Predicted') #x-axis label
plt.ylabel('Actual') #y-axis label
plt.title('Confusion Matrix') #title of the plot
plt.show() #show the plot

# prediction
print("Breast Cancer Prediction Model")

mean_radius = float(input("Enter mean radius: ")) #taking input from the user
mean_texture = float(input("Enter mean texture: ")) #taking input from the user
mean_perimeter = float(input("Enter mean perimeter: ")) #taking input from the user
mean_area = float(input("Enter mean area: ")) #taking input from the user
mean_smoothness = float(input("Enter mean smoothness: ")) #taking input from the user

# create a dataframe for the input data
user_data={"mean radius":mean_radius, "mean texture":mean_texture, "mean perimeter":mean_perimeter, "mean area":mean_area, "mean smoothness":mean_smoothness}
user_df=pd.DataFrame([user_data]) #converting the input data into a dataframe


# make prediction
prediction = model.predict(user_df)[0]#predicting the class labelif prediction == 1:
if prediction == 1:
    print("The breast cancer is Benign (non-cancerous).")
else:
    print("The breast cancer is Malignant (cancerous).")

