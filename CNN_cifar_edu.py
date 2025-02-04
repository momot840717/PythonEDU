from keras.datasets import cifar10

# 載入 Cifar10 資料集, 如果是第一次載入會自行下載資料集
(X_train, Y_train), (X_test, Y_test) = cifar10.load_data()
# 形狀
print("X_train.shape: ", X_train.shape)
print("Y_train.shape: ", Y_train.shape)
print("X_test.shape: ", X_test.shape)
print("Y_test.shape: ", Y_test.shape)
# 顯示 Numpy 二維陣列內容
print(X_train[0])
print(Y_train[0])   # 標籤資料

"""
0	飛機 (airplane)
1	汽車 (automobile)
2	鳥 (bird)
3	貓 (cat)
4	鹿 (deer)
5	狗 (dog)
6	青蛙 (frog)
7	馬 (horse)
8	船 (ship)
9	卡車 (truck)
"""


import matplotlib.pyplot as plt

plt.imshow(X_train[0])
plt.title("Label: " + str(Y_train[0]))
plt.axis("off")
# 顯示圖片
plt.show()


from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from keras.utils import to_categorical
import numpy as np
import pandas as pd



X_train = X_train.astype("float32") / 255
X_test = X_test.astype("float32") / 255
# One-hot編碼
Y_train = to_categorical(Y_train)
Y_test = to_categorical(Y_test)
# 定義模型
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), padding="same",
                 input_shape=X_train.shape[1:], activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, kernel_size=(3, 3), padding="same",
                 activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(10, activation="softmax"))
model.summary()   # 顯示模型摘要資訊
# 編譯模型
model.compile(loss="categorical_crossentropy", optimizer="adam",
              metrics=["accuracy"])
# 訓練模型
history = model.fit(X_train, Y_train, validation_split=0.2, 
                    epochs=9, batch_size=128, verbose=2)
# 評估模型
print("\nTesting ...")
loss, accuracy = model.evaluate(X_train, Y_train)
print("訓練資料集的準確度 = {:.2f}".format(accuracy))
loss, accuracy = model.evaluate(X_test, Y_test)
print("測試資料集的準確度 = {:.2f}".format(accuracy))

# 顯示訓練和驗證損失
history_dict = history.history

loss = history_dict["loss"]
epochs = range(1, len(loss)+1)
val_loss = history_dict["val_loss"]
plt.plot(epochs, loss, "bo-", label="Training Loss")
plt.plot(epochs, val_loss, "ro--", label="Validation Loss")
plt.title("Training and Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()
# 顯示訓練和驗證準確度
acc = history_dict["accuracy"]
epochs = range(1, len(acc)+1)
val_acc = history_dict["val_accuracy"]
plt.plot(epochs, acc, "bo-", label="Training Acc")
plt.plot(epochs, val_acc, "ro--", label="Validation Acc")
plt.title("Training and Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

# 接著做 crosstab、bar
# Y_pred = model.predict(X_test)
# Y_pred_classes = np.argmax(Y_pred, axis=1)
# # 顯示混淆矩陣
# tb = pd.crosstab(Y_test, Y_pred_classes, rownames=["label"], colnames=["predict"])


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