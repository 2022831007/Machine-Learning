# pd.merge(df1,df2,on="Column_Name",how="type of join")
import pandas as pd
df_customers = pd.DataFrame({
    'CustomerId':[1,2,3],
    'Name':["ramesh","shuresh","kalpaesh"]

})
#order dataframe
df_orders=pd.DataFrame({
    'CustomerId':[1,2,4],
    'OrderAmount':[250,450,350]
    
})
df_merged = pd.merge(df_customers,df_orders,on="CustomerId",how="inner")
print("inner join ")
print(df_merged)
df_merged = pd.merge(df_customers,df_orders,on="CustomerId",how="outer")
print("outer join ") #merge every row,fill with null values with Nan

print(df_merged)
df_merged = pd.merge(df_customers,df_orders,on="CustomerId",how="left")
print("left join ") #keep the left side values
print(df_merged)
df_merged = pd.merge(df_customers,df_orders,on="CustomerId",how="right")
print("right join ") #keep the right side values
print(df_merged)
#cross join
df_merged = pd.merge(df_customers,df_orders,how="cross")
print("cross join ") #df1=n rows,df2=m rows,cross join return=m*n rows
print(df_merged)