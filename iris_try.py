import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical


# 加載鳶尾花數據集
iris = load_iris()

# 呼叫 iris 的資料跟欄位名稱
iris_data = iris.data
iris_columns = iris.feature_names
iris_target = iris.target
# print(iris_data[:5], iris_target[:5], iris_columns)


# 將數據集轉換為 DataFrame
df = pd.DataFrame(data=iris_data, columns=iris_columns)
# 新增 target 欄位, 將 iris_target 存在此欄位
df['target'] = iris_target


# 將數值型的標籤轉換為對應的類別名稱  不用就註解掉
# ==============================
df['target'] = df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
# 資料存入csv檔使用表格查看數據集 
# print(df.head())
df.to_csv('iris_data2.csv', index=False)
# ==============================

# print(df.isnull().sum())  # 檢查資料是否有缺失值


# 將 df 資料視覺化 不用就註解掉
# ==============================
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.pairplot(df, hue='target', diag_kind='kde', markers=["o", "s", "D"])
# """
# hue 此處放資料分類欄位，以鳶尾花為例 target 是分類花種的欄位，這樣就可以看三個不同花種的資料分布
# diag_kind 對角線的資料顯示方式， kde 是密度分布曲線圖
# markers 三種花的特徵資料用甚麼圖案區分  o、s、D ：分别表示圆形、方形和菱形的散点标记，用于区分不同品种的数据点。
# """
# plt.show()
# ==============================



# 資料預處理
# ==============================
iris_categorical_target = to_categorical(iris_target)
"""
0 -> [1. 0. 0.]
1 -> [0. 1. 0.]
2 -> [0. 0. 1.]
"""

# 分割資料為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_categorical_target, test_size=0.2, random_state=42)
print(len(X_train), len(X_test))
"""
train_test_split
第一個參數為特徵資料(花萼花瓣的長寬)
第二個參數為答案(花的種類)
第三個參數test_size 為切割測試資料的比例
random_state = 42 原因 https://blog.csdn.net/x5445687d/article/details/120258252
"""
# ==============================


# 構建類神經網路模型
# ==============================
model = Sequential()
# 添加輸入層和一個隱藏層，使用 ReLU 激活函數
model.add(Dense(units=32, input_shape=(4,), activation='relu'))
"""
輸入層就是 input_shape, 資料型態要是 tuple, (4,) 代表輸入層為4個神經元
Dense 後面的數字就是隱藏層的神經元數量
activation 激活函數
"""
# 如要添加新的隱藏層 就不需要 input_shape
model.add(Dense(units=16, activation='relu'))
# 添加輸出層，使用 softmax 激活函數進行多分類
model.add(Dense(3, activation='softmax'))
"""
這邊輸出層神經元數量為3是因為花種只有3個
會根據輸出的向量接近哪一種答案而決定花種
接近 [1. 0. 0.] -> 0
接近 [0. 1. 0.] -> 1
接近 [0. 0. 1.] -> 2
"""
# 編譯模型
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
"""
optimizer 優化器, 使用adam公式優化梯度下降計算
loss 損失函數
metrics 參數用於指定在訓練和評估過程中需要監控的指標。metrics=['accuracy'] 表示在訓練和評估模型時， Keras 會計算並輸出模型的準確率。
"""
# 顯示模型架構
model.summary()
# ==============================


# 模型訓練
# ==============================
history = model.fit(X_train, y_train, epochs=30, batch_size=10)
"""
把模型訓練過程的損失值、準確度、驗證集損失值、驗證集準確度統計下來存入 history
epochs ：設置訓練的輪數。
batch_size ：每次更新權重使用的樣本數量。
validation_split ：從訓練數據中劃分出一部分作為驗證集驗證模型。
"""
# 使用測試資料評估訓練模型
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"測試集的判斷準確度：{test_accuracy:.2f}")
# ==============================




