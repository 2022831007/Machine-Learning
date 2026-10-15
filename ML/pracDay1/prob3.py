# Problem 5: Find and Fill Missing Values
# Easy

# data = {    'Name': ['A', 'B', 'C', 'D', 'E'],    'Age': [20, None, 25, None, 30],    'Salary': [20000, 30000, None, 40000, None]}df = pd.DataFrame(data)



# Tasks:
# 1. Display the original DataFrame.
# 2. Count missing values in each column using isnull().sum().
# 3. Create a new DataFrame after removing rows containing missing values.
# 4. Fill missing Age values with the mean age.
# 5. Fill missing Salary values with the mean salary.
# 6. Calculate the percentage of missing values in each column.
import pandas as pd
data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Age': [20, None, 25, None, 30],
    'Salary': [20000, 30000, None, 40000, None]
}

df = pd.DataFrame(data)
print('Original  DataFrame')
print(df)
print(df.isnull().sum())
print(df.isnull().mean()*100)
df_drop = df.dropna()
print(df_drop)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print(df)
