import numpy as np
import matplotlib.pyplot as plt
from  sklearn.linear_model import LinearRegression
import pandas as pd

#house(x) = size in square feet
#price(y) = in dollars
x = np.array([500, 800, 1000, 1200, 1500]).reshape(-1, 1) 
y = np.array([150000, 200000, 230000, 260000, 300000]) 

model = LinearRegression()
model.fit(x, y)

#Model parametrs
print("intercept:(base price)", model.intercept_)  #This is the base price of the house, even when the size (square footage) is zero.
print("slope:(price per square feet)", model.coef_[0]) #This is the price added per square foot.


size = 1100
predicted_price = model.predict([[size]])
print(f"Predicted price for a house {size} square feet: ${predicted_price[0]:.2f}")