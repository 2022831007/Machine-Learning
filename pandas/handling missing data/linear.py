import pandas as pd
data = {
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}
df=pd.DataFrame(data)
print('Before interpolation: ')
print(df)
print('After interpolation: ')
df['Value'] = df['Value'].interpolate(method="linear")
print(df)
"""
when to use interpolation?
1-time series data
2-neumeric data with trends
3-avoid dropping rows
4-cant work with catagorical data
"""
