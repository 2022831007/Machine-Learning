
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data = {
    'Age': [25, 30, 35, 40, 45, 50],
    'Income': [30000, 40000, 50000, 60000, 70000, 80000],
    'Spending': [70, 60, 50, 40, 30, 20],
    'Savings': [1000, 5000, 8000, 10000, 15000, 20000]
}

df = pd.DataFrame(data)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_data)

pca_df = pd.DataFrame(pca_result, columns=['PCA1', 'PCA2'])

explained_varianc = pca.explained_variance_ratio_

print("Variance captured by PCA Components")
print(np.round(explained_varianc * 100, 2))

plt.figure(figsize=(8, 6))
plt.scatter(pca_df['PCA1'], pca_df['PCA2'], color='black', s=80)
plt.title("PCA Projection (2D View)")
plt.xlabel('PCA1 Main Pattern')
plt.ylabel('PCA2 Main Pattern')
plt.grid(True)
plt.show()

print("New data with 2 features PCA1 and PCA2")
print(pca_df)
