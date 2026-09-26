import pandas  as pd
df = pd.read_json("/Users/macbook/Desktop/ML_Learning/sample_Data.json" )
print("displaying the info of data set")
print(df.info())