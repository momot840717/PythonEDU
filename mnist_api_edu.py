import numpy as np
from keras.datasets import mnist
from keras.models import Model
from keras.layers import Dense, Input

# 指定亂數種子
seed = 7
np.random.seed(seed)
# 載入資料集
(X_train, _), (X_test, _) = mnist.load_data()
# 轉換成 28*28 = 784 的向量
X_train = X_train.reshape(X_train.shape[0], 28*28).astype("float32")
X_test = X_test.reshape(X_test.shape[0], 28*28).astype("float32")
# 正規化, 從 0-255 至 0-1
X_train = X_train / 255
X_test = X_test / 255
# 定義 autoencoder 模型

center_units = 64

# 輸入層
input_img = Input(shape=(784,))

# 建立編碼器部分
x = Dense(128, activation="relu")(input_img)
encoded = Dense(center_units, activation="relu")(x)
"""
784->128->64
"""


# 建立解碼器部分
x = Dense(128, activation="relu")(encoded)  # 64 在 encoded
decoded = Dense(784, activation="sigmoid")(x)  
# 784長度的向量 每個元素都是 0~1 區間，0~1的原因是前面做了正規化，訓練圖的數值都在0~1
"""
64->128->784
"""

# 先將輸入層與輸出層連接起來，建立整個 Autoencoder(AE) 模型：
autoencoder = Model(input_img, decoded)
autoencoder.summary()


# 定義 encoder 模型，連接輸入層到 encoded 的隱藏層
encoder = Model(input_img, encoded)
encoder.summary()


# 定義 decoder 模型
"""
但是你不能直接做 Model(encoded, decoded)
而是要做一個新輸入層，再搭配 autoencoder 的倒數第二、倒數第一層
這樣建構的好處是 autoencoder 做訓練的時候 decoder 就可以共享到訓練結果
(因為decoder本來就是從autoencoder的部分要來的)
"""
decoder_input = Input(shape=(center_units,))
decoder_layer = autoencoder.layers[-2](decoder_input)
decoder_layer = autoencoder.layers[-1](decoder_layer)
decoder = Model(decoder_input, decoder_layer)
decoder.summary()    # 顯示模型摘要資訊


"""
編譯、訓練模型， autoencoder 物件、encoder、decoder 相互是連接的
這感覺就像是 list、dict 是可變動性的物件
就算賦值到其他變數再去更改裡面的資料，原資料還是會被更改的
list_1 = [1,2,3,4]
list_2 = list_1
list_2[0] = 5

dict_1 = {1:1, 2:2, 3:3}
dict_2 = dict_1
dict_2[1] = 11
print(list_1, dict_1)
"""
autoencoder.compile(loss="binary_crossentropy", optimizer="adam",
                    metrics=["accuracy"])
autoencoder.fit(X_train, X_train, validation_data=(X_test, X_test), 
                epochs=10, batch_size=256, shuffle=True, verbose=2)

# 壓縮圖片
encoded_imgs = encoder.predict(X_test)
# encoder 的結果傳入 decoder 還原圖片
decoded_imgs = decoder.predict(encoded_imgs)

print(decoded_imgs[0])

# 顯示原始, 壓縮和還原圖片
import matplotlib.pyplot as plt

n = 10  # 顯示幾個數字
plt.figure(figsize=(20, 6))
for i in range(n):
    # 原始圖片
    ax = plt.subplot(3, n, i + 1)
    ax.imshow(X_test[i].reshape(28, 28), cmap="gray")
    ax.axis("off")
    # 壓縮圖片
    ax = plt.subplot(3, n, i + 1 + n)
    ax.imshow(encoded_imgs[i].reshape(8, 8), cmap="gray")
    ax.axis("off")
    # 還原圖片
    ax = plt.subplot(3, n, i + 1 + 2*n)
    ax.imshow(decoded_imgs[i].reshape(28, 28), cmap="gray")
    ax.axis("off")
plt.show()