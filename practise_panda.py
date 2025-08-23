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
    'score': [85,90,78.0,None,88,76],
    'age': [20,21,19,None,20,23]
}
df=pd.DataFrame(data)
print(df.head()) 
print(df.head(3))  # first 3 rows


# dataframe tail() function
print(df.tail())  # last 5 rows


# dataframe info() function
print(df.info())


# dataframe describe() function
print(df.describe())

# dataframe columns function(column names)
print(df.columns) 

# dataframe shape function (rows and columns)
print(df.shape)


# dataframe loc function (access rows and columns by labels)
print(df.loc[2])  # row with index 2
print(df.loc[:,['Name','score']]) 

# dataframe iloc function (access rows and columns by integer position)
print(df.iloc[0])  # row at position 2
print(df.iloc[1,0])  # row 1, column 0
print(df.iloc[:, 0:2])  # all rows, columns 0 and 1

# dataframe isnull() function (check for missing values)
print(df.isnull())

# dataframe dropna() function (remove rows with missing values)
print(df.dropna())  # remove rows with any missing values

