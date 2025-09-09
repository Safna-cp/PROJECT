import pandas as pd
data =pd.read_csv(r'C:\Users\pc42\Desktop\DATA SCIENCE\PROJECT\MISSING_DATASET_HANDLING.csv',encoding='latin1')
# print(data.isnull().sum())

# drop function
data=data.drop(columns=["ADDRESSLINE2"])
print(data.isnull().sum())

# dropna function
data=data.dropna(subset=['ORDERDATE','PRODUCTLINE'])
print(data.isnull().sum())

# fillna function
data['MSRP']=data['MSRP'].fillna(data['MSRP'].median())
data['YEAR_ID']=data['YEAR_ID'].fillna(data['YEAR_ID'].mode()[0])
print(data.isnull().sum())

# in another case we can use,
data['STATUS'].fillna(data['STATUS'].mode()[0],inplace=True)
print(data.isnull().sum())

# in another case we can use,
data["PHONE"].fillna("UNKNOWN", inplace=True)
print(data.isnull().sum())




