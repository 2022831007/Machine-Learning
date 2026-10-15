# Problem 1: Encode Gender and Department
# Easy

# Use the following dataset:
# import pandas as pddata = {    'Name': ['Rahim', 'Karim', 'Nila', 'Mitu', 'Hasan'],    'Gender': ['Male', 'Male', 'Female', 'Female', 'Male'],    'Department': ['CSE', 'EEE', 'CSE', 'BBA', 'EEE']}df = pd.DataFrame(data)



# Tasks:
# 1. Create a copy named df_label.
# 2. Use LabelEncoder to encode the Gender column.
# 3. Encode the Department column into a new column called Department_Encoded.
# 4. Print the original and encoded columns.
# Hint: Use LabelEncoder() and fit_transform().
from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = {
    'Name': ['Rahim', 'Karim', 'Nila', 'Mitu', 'Hasan'],
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Male'],
    'Department': ['CSE', 'EEE', 'CSE', 'BBA', 'EEE']
}

df = pd.DataFrame(data)
df_label = df.copy()
le = LabelEncoder()
df_label['Department_Encoded'] = le.fit_transform(df_label['Department'])
print('\nLabel Encoded data')
print(df_label[['Name','Gender','Department','Department_Encoded']])