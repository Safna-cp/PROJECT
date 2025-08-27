import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd



# Histogram + KDE
df=sns.load_dataset('tips')
sns.histplot(df['total_bill'], bins=20, kde=True , color='blue')
plt.title("Histogram + KDE using Seaborn")
plt.show()


# BAR PLOT
data=pd.DataFrame({
    'Category':['A','B','C','D'],
    'Values':[23,45,56,78]
})
sns.barplot(x='Category', y='Values', data=data)
plt.title("Bar plot using Seaborn")
plt.show()



# count plot
df=sns.load_dataset('tips')
sns.countplot(x='day', data=df, palette='Set2')
plt.title("Count plot using Seaborn")
plt.show()



# Box plot
df=sns.load_dataset('tips')
sns.boxplot(x='day', y='total_bill', data=df, palette='pastel')
plt.title("Box plot using Seaborn")
plt.show()



# scatter plot
df=sns.load_dataset('tips')
sns.scatterplot(x='total_bill', y='tip', data=df, hue='sex', style='time')
plt.title("Scatter plot using Seaborn")
plt.show()

