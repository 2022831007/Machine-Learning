# %%
import matplotlib.pyplot as plt
#to draw line graph ->plt.plot(x,y)
months = [1,2,3,4]
sales = [1000,5000,3000,4000]
plt.plot(months,sales,color='blue',linestyle='--',linewidth=2,marker = 'o',label='2025 sales data')
plt.xlabel('months')
plt.ylabel('sales per month')
plt.title("2025 sales")
plt.legend() #shows  small box which title of data we are showing with very samll box
# plt.legend(loc='upper left',fontsize=12) with customised
plt.grid()#without customized
# plt.grid(color='gray',linestyle=':',linewidth=1)#can customize 
plt.xlim(1,4)
plt.ylim(0,2000)
plt.show()
# %%
