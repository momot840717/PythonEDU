import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense


df = pd.read_csv("./diabetes.csv")
"""
Pregnancies - 懷孕次數
Glucose - 2 小時後口服葡萄糖耐受測試的血糖濃度
BloodPressure - 血壓的舒張壓
SkinThickness - 三頭肌皮膚皺摺厚度
Insulin - 血清胰島素
BMI - 身體質量指數
DiabetesPedigreeFunction - 糖尿病家族病史的影響程度
Age - 年齡
Outcome - 5 年是否有糖尿病（1：是，0：否）
"""

np.random.seed(10)  # 指定亂數種子(類似指定亂數表，可以有一個相對可控的隨機)
dataset = df.values  # 取得 df 所有數值
np.random.shuffle(dataset)  # 使用亂數打亂資料
# 分割成特徵資料和標籤資料
X = dataset[:, 0:8]
Y = dataset[:, 8]
# X = dataset[:, 0:-1]
# Y = dataset[:, -1]
# 特徵標準化
X -= X.mean(axis=0)
X /= X.std(axis=0)
# 分割訓練和測試資料集

X_train, Y_train = X[:690], Y[:690]     # 訓練資料前690筆
X_test, Y_test = X[690:], Y[690:]       # 測試資料後78筆
# 定義模型
model = Sequential()
model.add(Dense(10, input_shape=(8,), activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(1, activation="sigmoid"))
# model.summary()   # 顯示模型摘要資訊

# 編譯模型
model.compile(loss="binary_crossentropy", optimizer="adam", 
              metrics=["accuracy"])
# 訓練模型
model.fit(X_train, Y_train, epochs=150, batch_size=10)
# 評估模型
loss, accuracy = model.evaluate(X_train, Y_train)
print("訓練資料集的準確度 = {:.2f}".format(accuracy))
loss, accuracy = model.evaluate(X_test, Y_test)
print("測試資料集的準確度 = {:.2f}".format(accuracy))
# 測試資料集的預測值
Y_pred = model.predict(X_test, batch_size=10)
print(Y_pred[0], Y_pred[1])

# 訓練模型
history = model.fit(X_train, Y_train, validation_data=(X_test, Y_test), 
          epochs=10, batch_size=10)
# 評估模型
loss, accuracy = model.evaluate(X_train, Y_train)
print("訓練資料集的準確度 = {:.2f}".format(accuracy))
loss, accuracy = model.evaluate(X_test, Y_test)
print("測試資料集的準確度 = {:.2f}".format(accuracy))

print(history)
print(history.history)

# pip install matplotlib
import matplotlib.pyplot as plt


# 顯示訓練和驗證損失的圖表
loss = history.history["loss"]
val_loss = history.history["val_loss"]
epochs = range(1, len(loss)+1)
plt.plot(epochs, loss, "bo", label="Training Loss")  
# plt.plot() 用於繪製曲線。"bo" 代表藍色（b）的圓點（o），用於顯示訓練損失的數據點。label="Training Loss" 設定圖例標籤。
plt.plot(epochs, val_loss, "r", label="Validation Loss")
# "r" 代表紅色（r），這條曲線表示驗證集的損失。
plt.title("Training and Validation Loss")
plt.xlabel("Epochs")  # X軸名稱
plt.ylabel("Loss")  # Y軸名稱
plt.legend()  # 圖表顯示圖例
plt.show()  # 顯示圖表


# 顯示訓練和驗證準確度
acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]
epochs = range(1, len(acc)+1)
plt.plot(epochs, acc, "b-", label="Training Acc")
plt.plot(epochs, val_acc, "r--", label="Validation Acc")
plt.title("Training and Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()