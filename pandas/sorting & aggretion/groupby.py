import pandas as pd
data={
    "name":["rina","tina","rima","lamine","ruhi","Shiro","Tiro","merrie","ina","mina","tika"],
    "age":[20,22,23,21,27,24,30,40,23,37,43],
    "salary":[50000,60000,42000,70000,60000,30000,48000,58000,67000,78000,87000],
    "performance-score":[85,90,78,92,88,89,67,76,89,67,95]

}
df= pd.DataFrame(data)
groupd = df.groupby("age")["salary"].sum()
print(groupd)