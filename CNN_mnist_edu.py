import numpy as np
import pandas as pd
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from keras.utils import to_categorical

# 載入資料集
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
# 將圖片轉換成 4D 張量
#                            資料量,        長, 寬, 通道數(灰階圖是1)
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype("float32")
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype("float32")
print("X_train Shape: ", X_train.shape)
print("X_test Shape: ", X_test.shape)
# 因為是固定範圍, 所以執行正規化, 從 0-255 至 0-1
X_train = X_train / 255
X_test = X_test / 255
# One-hot編碼
Y_train_c = to_categorical(Y_train)
Y_test_c = to_categorical(Y_test)
print("Y_train Shape: ", Y_train.shape)
print(Y_train[0])

# 定義模型
model = Sequential()
model.add(Conv2D(16, kernel_size=(3, 3), padding="same", input_shape=(28, 28, 1), activation="relu"))
# padding="same"：在輸入資料的邊緣補零，當stride = 1 時，卷積後的輸出尺寸與原始輸入尺寸相同。特徵圖size還是(28, 28)
model.add(MaxPooling2D(pool_size=(2, 2)))  # 最大池化法
model.add(Conv2D(32, kernel_size=(3, 3), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))  # 隨機選取50%資料，數值改為0，以此來降低模型的過擬合風險
model.add(Flatten())  # 將卷積層輸出的多維特徵圖展平為一維向量。可以當作 MLP 的輸入層
model.add(Dense(128, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(10, activation="softmax"))
model.summary()   # 顯示模型摘要資訊
"""
假定 kernel_size 設定 3*3

1. conv2d Param = 160
每個 filter 有9個權重(參數)再加上 1 個 bias。所以每一個 filter 有 10 個參數
filter 有 16 個所以 16*10 = 160

2.  max_pooling2d 最大池化法只是一個範圍內選取最大數值的函數，沒有訓練參數

3. conv2d Param = 4,640
前一個 filter 有 16 個，所以產生了通道數16的圖片(就是16個矩陣疊一起)，並且每個通道使用的 filter 不一樣，每一層通道參數就不一樣
第二層 CNN 的每一個 filter 參數有 3*3*16 + 1 = 145， filter 有 32 個所以 145*32 = 4640

4. flatten = 1568
(28, 28) 的圖經過經過一次最大池化，長、寬都會少一半。這裡經過兩次所以剩下 (7, 7)
加上前面 filter 有 32 個，所以是一份 (7, 7, 32) 的圖 (通道32個)，然後一次拉成一維數據(向量)
所以 7*7*32 = 1568

5. Dense Param 200832 = 1568*128 + 128
6. Dense Param 1,290 = 128*10 + 10

"""

# 編譯模型
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
# 訓練模型
history = model.fit(X_train, Y_train, validation_split=0.2, epochs=10, batch_size=128, verbose=2)
# 評估模型
print("\nTesting ...")
loss, accuracy = model.evaluate(X_train, Y_train)
print("訓練資料集的準確度 = {:.2f}".format(accuracy))
loss, accuracy = model.evaluate(X_test, Y_test)
print("測試資料集的準確度 = {:.2f}".format(accuracy))

# 顯示圖表來分析模型的訓練過程
import matplotlib.pyplot as plt
# 顯示訓練和驗證損失
loss = history.history["loss"]
epochs = range(1, len(loss)+1)
val_loss = history.history["val_loss"]
plt.plot(epochs, loss, "bo-", label="Training Loss")
plt.plot(epochs, val_loss, "ro--", label="Validation Loss")
plt.title("Training and Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()
# 顯示訓練和驗證準確度
acc = history.history["accuracy"]
epochs = range(1, len(acc)+1)
val_acc = history.history["val_accuracy"]
plt.plot(epochs, acc, "bo-", label="Training Acc")
plt.plot(epochs, val_acc, "ro--", label="Validation Acc")
plt.title("Training and Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()


# 儲存Keras模型
# model.save("mnist.keras")
# from keras.models import load_model
# 這裡可以嘗試自己用小畫家創作28*28的手寫字

Y_pred = model.predict(X_test)
Y_pred_classes = np.argmax(Y_pred, axis=1)
# 顯示混淆矩陣
tb = pd.crosstab(Y_test, Y_pred_classes, rownames=["label"], colnames=["predict"])

# # 預測結果做柱狀圖
# pred = np.array([0,0,0,0,0,0.1,0,0,0.9,0])

# # 畫出機率柱狀圖
# digits = np.arange(10)  # 數字 0 到 9
# plt.figure(figsize=(8, 4))
# plt.bar(digits, pred, color='skyblue')
# plt.xlabel("Numbur")
# plt.ylabel("Probability")
# plt.title("Probability Distribution")
# plt.xticks(digits)
# plt.ylim([0, 1])  # 機率範圍通常在 0 到 1 之間
# plt.show()