import pandas as pd
data = {
    'Name' :["Fatema","Tanha","choiti","Mahi","Abdur"],
    'Age' : [23,24,None,44,20],
    'Salary':[50000,60000,70000,None,None]
    }

df = pd.DataFrame(data)
print("original DataFrame")
print(df)
print(df.isnull().sum())
df_drop = df.dropna()
print(df_drop)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print(df)
print(df.isnull().mean()*100)