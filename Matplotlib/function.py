#%%
import matplotlib.pyplot as plt

months = [1, 2, 3, 4]
sales = [1000, 5000, 3000, 4000]

plt.plot(months, sales, color='blue',
         linestyle='--',
         linewidth=2,
         marker='o',
         label='2025 sales data')

plt.xlabel('months')
plt.ylabel('sales per month')
plt.title('2025 sales')

plt.legend()
plt.grid()

plt.xlim(1, 4)
plt.ylim(0, 6000)
plt.xticks([1,2,3,4],['m1','m2','m3','m4'])
plt.show()
# %%
