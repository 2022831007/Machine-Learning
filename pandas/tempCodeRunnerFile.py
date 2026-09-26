import pandas as pd
data={
    "Name":['Fatema','Saima','Mahi'],
    "Age":[22,21,22],
    "City":["Sherpur","Mymenshing","Ctg"]
}
df = pd.DataFrame(data)
print(df)
#passing file name
df.to_csv("output.csv",index=False)
#make it excel
df.to_excel("output.xlsx",index=False)
