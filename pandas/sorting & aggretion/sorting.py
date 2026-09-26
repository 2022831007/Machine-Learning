#sorting data
#sorting data in 1 column sort_values()
#df.sort_values(by="Column Name",True/False,inplace=True)
import pandas as pd
data={
    "name":["rina","tina","rima","lamine","ruhi","Shiro","Tiro","merrie"],
    "age":[20,22,23,21,27,24,30,40],
    "salary":[50000,60000,42000,70000,60000,30000,48000,58000],
    "performance-score":[85,90,78,92,88,89,67,76]

}
df= pd.DataFrame(data)
#sort age in descending order
df.sort_values(by="age",ascending=False,inplace=True)
print(df)
#sort age in acescending order
df.sort_values(by="age",ascending=True,inplace=True)
print(df)

