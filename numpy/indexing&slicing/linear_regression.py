import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ==========================================
# 1. Download Dataset from Kaggle
# ==========================================

# # import kagglehub
# # 
# # print("Downloading dataset...")
# # 
# # path = kagglehub.dataset_download(
# #     "himanshunakrani/student-study-hours"
# # )

print("Dataset downloaded!")
print("Dataset path:", path)

# Show files inside dataset folder
files = os.listdir(path)
print("Files:", files)


# ==========================================
# 2. Find CSV File
# ==========================================

csv_files = [file for file in files if file.endswith(".csv")]

if len(csv_files) == 0:
    print("No CSV file found!")
    exit()

csv_file = csv_files[0]

print("CSV file:", csv_file)


# ==========================================
# 3. Load Dataset
# ==========================================

file_path = os.path.join(path, csv_file)

df = pd.read_csv(file_path)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nColumn Names:")
print(df.columns)


# ==========================================
# 4. Select X and Y
# ==========================================

X = df[["Hours"]]
y = df["Scores"]


# ==========================================
# 5. Create Linear Regression Model
# ==========================================

model = LinearRegression()

model.fit(X, y)


# ==========================================
# 6. Prediction
# ==========================================

y_pred = model.predict(X)


# ==========================================
# 7. Model Information
# ==========================================

slope = model.coef_[0]
intercept = model.intercept_
r2_score = model.score(X, y)

print("\n========== Linear Regression Results ==========")

print("Slope:", slope)
print("Intercept:", intercept)
print("R² Score:", r2_score)

print(
    f"\nRegression Equation: "
    f"Score = {intercept:.2f} + {slope:.2f} × Hours"
)


# ==========================================
# 8. Scatter Plot + Regression Line
# ==========================================

plt.figure(figsize=(8, 5))

# Actual data points
plt.scatter(
    X,
    y,
    label="Actual Data"
)

# Regression line
plt.plot(
    X,
    y_pred,
    label="Regression Line"
)

plt.xlabel("Hours Studied")
plt.ylabel("Scores")

plt.title(
    "Linear Regression: Study Hours vs Scores"
)

plt.legend()

plt.grid(True)

plt.show()