#adding columns
import pandas as pd
data={
    "name":["rina","tina","rima","lamine","ruhi","Shiro","Tiro","merrie"],
    "age":[20,22,23,21,27,24,30,40],
    "salary":[50000,60000,42000,70000,60000,30000,48000,58000],
    "performance-score":[85,90,78,92,88,89,67,76]

}
df= pd.DataFrame(data)
#square brackets df["Column_Name"] = some_Data
print(df)
#adding bonus column
df["Bonus"] = df['salary']*0.1#have to add in the end,can't add in the first or middle
print(df)
#using insert()
#df.insert(loc,"Column_Name",some_data)
#freedom of adding column anywhere,firts,last,middle,anywhere
df.insert(0,"Employess ID",[10,20,30,40,50,60,70,80])
print(df)



