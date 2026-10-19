from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error
import numpy as np
#real scores
real_scores = [90,60,80,100]
#model guess
predicted_scores = [85,70,70,95]
mae = mean_absolute_error(real_scores,predicted_scores)
mse = mean_squared_error(real_scores,predicted_scores)
rmse= np.sqrt(mse)
print("MAE: On average off by:",mae) #when we need simple answer we use it
print("MSE: SQUARED Mistake Value:",mse) #huge mistakes detect
print("RMSE: Final Realistic error:",rmse) #real units which error





