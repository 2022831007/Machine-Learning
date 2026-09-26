import pandas as pd
#read data from csv file into a dataframe
df = pd.read_csv("sales_data_sample.csv",encoding="latin1")
print(df)
df1= pd.read_excel("SampleSuperstore.xlsx")
print(df1)
df2 = pd.read_json("sample_Data.json")
print(df2)