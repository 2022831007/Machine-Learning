#head(),tail()
#head(n) -first n rows
#tail(n) last n rows
import pandas as pd
df=pd.read_csv("/Users/macbook/Desktop/ML_Learning/sales_data_sample.csv")
print("Display 10 rows of first")
print(df.head(10))
print("Display 10 rows of last")
print(df.tail(10))