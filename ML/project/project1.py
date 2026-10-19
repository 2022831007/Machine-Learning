import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
import numpy as np
data = pd.read_csv("ML/student.csv")
X = data[['Hours']]
y = data[["Score"]]
model = LinearRegression()
model.fit(X,y)
predicted_score = model.predict(X)
#evaluate
mae = mean_absolute_error(y,predicted_score)
mse = mean_squared_error(y,predicted_score)
rmse = np.sqrt(mse)

print("Mean Abosulte Error(MAE):",mae)
print("Mean Squared Error(MSE):",mse)
print(" Root Mean Squared Error(RMSE):",rmse)

# new_hour = float(input("enter a hour = "))
# new_pred = model.predict(new_hour)
# print(f"Prediction for {new_hour} is score ={new_pred}")

new_prediction = model.predict([[7]])
print(f"Prediction Score 7 hour",new_prediction)
