#fillna(value,inplace=True)
import pandas as pd
data={
    "name":["rina",None,"rima","lamine","ruhi","Shiro","Tiro","merrie"],
    "age":[20,22,23,21,27,24,30,40],
    "salary":[50000,60000,42000,70000,60000,30000,48000,58000],
    "performance-score":[85,None,78,92,88,89,67,76]

}
df= pd.DataFrame(data)
print(df)
# df.fillna(0,inplace=True)
# print(df)
df['performance-score']=df['performance-score'].fillna(df['performance-score'].mean(),inplace=True)
print(df)
