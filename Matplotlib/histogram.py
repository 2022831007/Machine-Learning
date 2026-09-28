#%%
import matplotlib.pyplot as plt
scores = [45,57,89,78,88,92,68,90,45,69,77,89,34,54,77,86]
plt.hist(scores,bins=5,color ='purple',edgecolor='black')
plt.xlabel('Score Range')
plt.ylabel('Number of students')
plt.title('Score Distribution')
plt.show()
# %%
