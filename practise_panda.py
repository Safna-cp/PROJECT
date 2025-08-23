import pandas as pd
# s= pd.Series([10,20,30,40])
# print(s)


# DataFrame(table like structure)
# data = {
#     "Name": ["Alice", "Bob"],
#     "Age": [25, 30]}
# df = pd.DataFrame(data)
# print(df)


# dataframe head() function
data ={
    'Name': ['alice','bob','charlie','david','eva','frank'],
    'score': [85,90,78,92,88,76]
}
df=pd.DataFrame(data)
print(df.head()) 
print(df.head(3))  # first 3 rows

