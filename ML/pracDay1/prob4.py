# Problem 6: Apply Both Scalers
# Easy

# data = {    'StudyHours': [2, 4, 6, 8, 10],    'Marks': [30, 40, 50, 60, 70]}df = pd.DataFrame(data)



# Tasks:
# 1. Apply StandardScaler to both columns.
# 2. Store the result in a DataFrame with the original column names.
# 3. Apply MinMaxScaler to the same original data.
# 4. Print both results.
# 5. State the expected range of values after Min-Max scaling.
# Hint: Use fit_transform(df) and pass the column names when creating the output DataFrame.
import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler
data = {
    'Age': [18, 25, 35, 50, 60],
    'Salary': [15000, 25000, 50000, 80000, 120000],
    'Experience': [0, 2, 5, 10, 15]
}

df = pd.DataFrame(data)
standard_scaler = StandardScaler.fit_transform(df)
standard_scaled = standard_scaler