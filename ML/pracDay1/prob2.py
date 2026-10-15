
# Problem 4: Encode Multiple Categorical Columns
# Intermediate

# data = {    'Name': ['Rafi', 'Nila', 'Siam', 'Mitu'],    'City': ['Dhaka', 'Khulna', 'Dhaka', 'Rajshahi'],    'Course': ['Python', 'Java', 'Python', 'C++'],    'Marks': [80, 75, 90, 85]}df = pd.DataFrame(data)



# Tasks:
# 1. Apply One-Hot Encoding to both City and Course.
# 2. Keep Name and Marks unchanged.
# 3. Display the complete encoded DataFrame.
# 4. Count the total number of columns after encoding.
# Hint: Pass a list of column names to columns.
import pandas as pd
from sklearn.preprocessing import LabelEncoder
data = {
    'Name': ['Rafi', 'Nila', 'Siam', 'Mitu'],
    'City': ['Dhaka', 'Khulna', 'Dhaka', 'Rajshahi'],
    'Course': ['Python', 'Java', 'Python', 'C++'],
    'Marks': [80, 75, 90, 85]
}

df = pd.DataFrame(data)
df_label = df.copy()
le = LabelEncoder()
df_encoded = pd.get_dummies(df_label,columns=['City','Course'])
print('\n One-Hot Encoded data (City)(Course)')
print(df_encoded)