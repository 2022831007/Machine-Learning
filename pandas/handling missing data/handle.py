import pandas as pd
data={
    "name":["rina",None,"rima","lamine","ruhi","Shiro","Tiro","merrie"],
    "age":[20,22,23,21,27,24,30,40],
    "salary":[50000,60000,42000,70000,60000,30000,48000,58000],
    "performance-score":[85,None,78,92,88,89,67,76]

}
df= pd.DataFrame(data)
print(df)
#1 way:removing missing value
df.dropna(inplace=True)
print(df)


