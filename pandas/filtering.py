import pandas as pd
#step-1 sample data frame
data={
    "name":["rina","tina","rima","lamine","ruhi","Shiro","Tiro","merrie"],
    "age":[20,22,23,21,27,24,30,40],
    "salary":[50000,60000,42000,70000,60000,30000,48000,58000],
    "performance-score":[85,90,78,92,88,89,67,76]

}
df = pd.DataFrame(data)
high_salary = df[df['salary']>50000]
print("Empolyee with salary>50000")
print(high_salary)
#multuple condition 
filetred = df[(df['age']>30)&(df['salary']>50000)]
print(filetred)
#using or condition
filetredOr = df[(df['age']>30)|(df['salary']>50000)]
print(filetredOr)