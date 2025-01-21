import pandas as pd

# 讀取 CSV 文件
df = pd.read_csv("diabetes.csv")

# 計算相關係數矩陣
correlation_matrix = df.corr()

# 顯示相關係數矩陣
print(correlation_matrix)

import seaborn as sns
import matplotlib.pyplot as plt

# 繪製相關係數熱圖
plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix of Diabetes Dataset")
plt.show()