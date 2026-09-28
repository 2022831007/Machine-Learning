import matplotlib.pyplot as plt
product = ['A','B','C','D']
sales = [100,1500,800,1200]
plt.bar(product,sales,color='orange',label='Sales 2025')
plt.xlabel('prodcut')
plt.ylabel('Sales')
plt.title('Product Sales ')
plt.show()