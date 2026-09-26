import pandas as pd
data={
    "name":["rina","tina","rima","lamine","ruhi","Shiro","Tiro","merrie"],
    "age":[20,22,23,21,27,24,30,40],
    "salary":[50000,60000,42000,70000,60000,30000,48000,58000],
    "performance-score":[85,90,78,92,88,89,67,76]

}
df= pd.DataFrame(data)
print(df)
#df.drop(columns=["ColumnName"],inplace=True)
df.drop(columns=["performance-score","age"],inplace=True)
print(df)

