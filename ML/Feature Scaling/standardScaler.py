#%%
from sklearn.preprocessing import StandardScaler,MinMaxScaler
scaler = StandardScaler()
x_scaled = scaler.fit_transform()
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform()

# %%
import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split
data = {
    'StudyHours':[1,2,3,4,5],
    'TestScore' : [40,50,60,70,80]
}
df = pd.DataFrame(data)
Standard_Scaler = StandardScaler()
Standard_Scaled = Standard_Scaler.fit_transform(df)
print("Standard Scaler Output:")
print(pd.DataFrame(Standard_Scaled,columns=['StudyHours','TestScore']))
minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(df)
print("\nMinMax Scaled output:")
print(pd.DataFrame(minmax_scaled , columns=['StudyHours','TestScore']))
X = df[['StudyHours']]
y = df[['TestScore']]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print("Traing Data")
print(X_train)
print("Test Data")
print(X_test)
print("Traing Data")
print(y_train)
print("Test Data")
print(y_test)

# %%
