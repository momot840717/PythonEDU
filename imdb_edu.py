import numpy as np
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Embedding, Flatten, Conv1D, MaxPooling1D


# 載入 IMDb 資料集
top_words = 10000
(X_train, Y_train), (X_test, Y_test) = imdb.load_data(num_words=top_words)  # 取前1000個常用詞
# print(Y_train[:5])

# 確認最大的單字索引值
max_index = max(max(sequence) for sequence in X_train)

# 呼叫數字轉文字的字典
word_index = imdb.get_word_index()
# print(word_index['the'])

reverse_word_index = {value: key for key, value in word_index.items()} # 一行翻轉字典 key, value 反過來
# print(reverse_word_index[1], reverse_word_index[2])
X_train_words = [reverse_word_index[i] for i in X_train[0]]
# print(X_train_words)
"""
X_train的數字意思
0:	單純補零填長度(看下面sequence.pad_sequences)
1:	評論開頭
2:	未知單詞
3:  目前沒有意思
4+	真正的單詞索引（對應 imdb.get_word_index()）
原本 word_index 的索引	
1 → "the"
IMDb X_train 內的索引
4 → "the"
所以 4-3=1 才能正確對應
"""
X_train_words = [reverse_word_index.get(i-3, '?') for i in X_train[0]]
# print(X_train_words)

"""
dict 的 get() 用法
word_index = {
    "the": 1,
    "and": 2,
    "a": 3,
    "of": 4,
    "to": 5
}

word_index["hello"] -> hello不在字典裡, 會報錯
word_index.get("hello", "未知單詞")  -> 回傳 "未知單詞", 不會報錯
"""

# 資料預處理
max_words = 500
"""
sequence.pad_sequences 把每個列表補足或切割到指定長度
不足的是補零(zero padding)
"""
X_train = sequence.pad_sequences(X_train, maxlen=max_words)
X_test = sequence.pad_sequences(X_test, maxlen=max_words)
# print(X_train[0])

# 定義模型1
def model_1():
    model = Sequential()
    model.add(Embedding(input_dim=top_words, output_dim=32, input_shape=(max_words,)))
    """
    input_dim=10000 → 你的詞彙表大小為 10000，這表示模型需要學習 10000 個詞的詞向量。
    output_dim=32 → 每個詞會對應到一個 32 維的向量，這就是詞向量的維度。
    input_length=500 → 每條輸入數據（影評）最多包含 500 個詞。
    輸入 [14, 22, 16, 43, 530] 給 Embedding 
    輸出對應可能的詞向量，EX: [[0.1, -0.2,..., 0.4], [-0.3, 0.8,..., -0.5], ...] 每個元素長度32個
    """

    model.add(Dropout(0.4))
    model.add(Flatten())
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.4))
    model.add(Dense(1, activation="sigmoid"))
    model.summary()   # 顯示模型摘要資訊
    # 編譯模型
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model

# 定義模型2
def model_2():
    model = Sequential()
    model.add(Embedding(top_words, 32, input_length=max_words))
    model.add(Dropout(0.25))
    model.add(Conv1D(filters=32, kernel_size=3, padding="same",
                    activation="relu"))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(0.25))
    model.add(Dense(1, activation="sigmoid"))
    model.summary()   # 顯示模型摘要資訊
    # 編譯模型
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


model = model_1()
# model = model_2()

# 訓練模型
history = model.fit(X_train, Y_train, validation_split=0.2, 
          epochs=5, batch_size=128, verbose=2)
# 評估模型
loss, accuracy = model.evaluate(X_test, Y_test)
print("測試資料集的準確度 = {:.2f}".format(accuracy))


