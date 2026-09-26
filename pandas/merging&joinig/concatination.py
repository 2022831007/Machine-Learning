"""
vertically(row-wise)
horizontally(column wise)
pd.concate([df1,df2],axis=0,ignore_index=True)
[df1,df2]= axis=1,ignore_index=True
"""
import pandas as pd
df_Region1 = pd.DataFrame({
    'CustomerId':[1,2],
    'name':['rajesh','shuresh']
})
df_Region2 = pd.DataFrame({
    'CustomerId':[3,4],
    'name':['raj','kalpesh']
})
#concate vertically
df_concat = pd.concat([df_Region1,df_Region2],ignore_index=True)
print(df_concat)
#concate horizonattly
df_concat = pd.concat([df_Region1,df_Region2],axis=1,ignore_index=True)
print(df_concat)

