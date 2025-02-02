from keras.datasets import mnist

# 載入 MNIST 資料集, 如果是第一次載入會自行下載資料集
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
# 顯示 Numpy 二維陣列內容
print(X_train[0])
print(Y_train[0])   # 標籤資料

import matplotlib.pyplot as plt
from scipy import signal
import numpy as np


plt.subplot(1, 2, 1)
plt.imshow(X_train[0], cmap="gray")
plt.title("Label: " + str(Y_train[0]))
plt.axis("off")


kernel = np.array([[ 0,  1, -1],
                   [ 0,  1, -1],
                   [ 0,  1, -1]])
plt.subplot(1, 2, 2)
c_img = signal.convolve2d(X_train[0], kernel)  # signal.convolve2d 進行卷積
plt.imshow(c_img, cmap="gray")
plt.axis("off")
plt.title(f"c_img")   

plt.show()


from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical

# 先練習 MLP 做法

# 指定亂數種子

# 將 28*28 圖片轉換成 784 的向量
# print(X_train.shape)

column_quantity = X_train.shape[1] * X_train.shape[2]
X_train = X_train.reshape(X_train.shape[0], column_quantity).astype("float32")
X_test = X_test.reshape(X_test.shape[0], column_quantity).astype("float32")
print(X_train, X_train.shape)
# 因為是固定範圍, 所以執行正規化, 從 0-255 變至 0-1
X_train = X_train / 255
X_test = X_test / 255
# One-hot編碼
Y_train = to_categorical(Y_train)
Y_test = to_categorical(Y_test)
# 定義模型
model = Sequential()
model.add(Dense(256, input_shape=(column_quantity,), activation="relu"))
# model.add(Dropout(0.5))  # 第二次訓練再打開
model.add(Dense(256, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.summary()   # 顯示模型摘要資訊
# 編譯模型
model.compile(loss="categorical_crossentropy", optimizer="adam",
              metrics=["accuracy"])
# 訓練模型
history = model.fit(X_train, Y_train, validation_split=0.2,
                    epochs=10, batch_size=128, verbose=2)    # 思考為什麼epochs 10次而已圖表就有過擬合
# 評估模型
print("\nTesting ...")
loss, accuracy = model.evaluate(X_train, Y_train)
print("訓練資料集的準確度 = {:.2f}".format(accuracy))
loss, accuracy = model.evaluate(X_test, Y_test)
print("測試資料集的準確度 = {:.2f}".format(accuracy))



# import matplotlib.pyplot as plt
# # 顯示訓練和驗證損失
# loss = history.history["loss"]
# epochs = range(1, len(loss)+1)
# val_loss = history.history["val_loss"]
# plt.plot(epochs, loss, "bo-", label="Training Loss")
# plt.plot(epochs, val_loss, "ro--", label="Validation Loss")
# plt.title("Training and Validation Loss")
# plt.xlabel("Epochs")
# plt.ylabel("Loss")
# plt.legend()
# plt.show()
# # 顯示訓練和驗證準確度
# acc = history.history["acc"]
# epochs = range(1, len(acc)+1)
# val_acc = history.history["val_acc"]
# plt.plot(epochs, acc, "bo-", label="Training Acc")
# plt.plot(epochs, val_acc, "ro--", label="Validation Acc")
# plt.title("Training and Validation Accuracy")
# plt.xlabel("Epochs")
# plt.ylabel("Accuracy")
# plt.legend()
# plt.show()

model.save('mlp_mnist_model.keras')