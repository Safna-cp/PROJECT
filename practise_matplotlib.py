import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

x=np.linspace(0,10,100)
y=np.sin(x)
plt.plot(x,y, color='red',linestyle='--', marker='o')
plt.title("Line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()




# Scatter plot
x=np.random.rand(50)    
y=np.random.rand(50)
plt.scatter(x,y, color='blue', marker='x')
plt.title("Scatter plot")
plt.show()


#  vertical Bar plot
categories=['A','B','C',]
values=[10,15,7,]
plt.bar(categories, values, color=['green','red','blue'])
plt.title("Bar plot")
plt.show()



# Horizontal Bar plot
categories=['A','B','C',]
values=[10,15,7,]
plt.barh(categories, values, color=['green','red','blue'])
plt.title("Horizontal Bar plot")
plt.show()


# Histogram
data=np.random.randn(1000)
plt.hist(data, bins=30, color='red', edgecolor='green')
plt.title("Histogram")
plt.show()


# Pie chart
labels=['A','B','C','D']
plt.pie([30,50,20,25], labels=labels, autopct='%1.1f%%', colors=['yellow','blue','green','red'],startangle=90)
plt.title("Pie chart")
plt.show()

# stack area plot
days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]
plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','k'], labels=['sleep','eat','work','play'])
plt.legend(loc='upper left')
plt.title("Stack area plot")
plt.show()