import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

"""
pclass：乘客等級，值為 1、2、3，對應頭等、二等、三等艙。
survived：是否生還，1 表示生還，0 表示死亡。
name：乘客姓名。
sex：性別，male 為男性，female 為女性。
age：乘客年齡。
sibsp：乘客在船上的兄弟姐妹或配偶人數。
parch：乘客在船上的父母或子女人數。
ticket：船票號碼。
fare：票價。
cabin：艙位號碼。
embarked：登船港口代碼，C 代表 Cherbourg（瑟堡）、Q 代表 Queenstown（昆士敦）、S 代表 Southampton（南安普敦）。
"""

df = pd.read_csv('./titanic_data.csv')
# print(df.head())
# print(df.describe())  # 描述表格 count 可以看有沒有缺漏 age fare 有缺
# print(df.info())  # 表格資訊
# print(df.isnull())  # 用bool回傳是否空值
# print(df.isnull().sum())  # 搭配 .sum() 一目了然 (預設axis=0)

df = df.drop(['name', 'ticket', 'cabin'], axis=1)  #　刪除方向是欄位，因此使用 axis=1。先把不用的東西刪除，可以跑比較快。
# print(df.head())
df['age'] = df['age'].fillna(df['age'].mean())  # 用平均數補值
df['fare'] = df['fare'].fillna(df['fare'].median())  # 用中位數補值

# 字串的眾數補值兩個方法，二選一，不用的記得註解掉
# mode()
# print(df['embarked'].mode()[0])
# df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])  # df['embarked'].mode() 會回傳 Series, 取第0個
#  value_counts() 加上 idxmax()
print(df['embarked'].value_counts())  # 回傳 Series, index 是 S Q C
print(df['embarked'].value_counts().idxmax())  # 取 counts 最大的 idx, 這裡會取到 S
df['embarked'] = df['embarked'].fillna(df['embarked'].value_counts().idxmax())
# print(df.describe())

df['sex'] = df['sex'].map({'female': 1, 'male': 0})
# print(df.head())

# embarked 拆成 embarked_S, embarked_Q, embarked_C 在表格做出類似分類向量的感覺
#                     0          1           0
#                     1          0           0
#                     0          0           1
# print(pd.get_dummies(df['embarked'], prefix='embarked'))  # predix 前綴詞, 若沒有 prefix, embarked_S 會變成只有 S
embarked_one_hot = pd.get_dummies(df['embarked'], prefix='embarked')
df = pd.concat([df, embarked_one_hot], axis=1)
df = df.drop(['embarked'], axis=1)

# 用 pop 移除 survived 欄位, 再新增到表格最後欄位做答案
df_sur = df.pop('survived')  # pop 會移除掉東西，但是他會回傳被移除的東西，有需要可以存起來備用
df['survived'] = df_sur
# df['survived'] = df.pop('survived')  # 熟練地可以直接寫成一行
print(df.head())

np.random.seed(10)
dataset = df.values
np.random.shuffle(dataset)
X = dataset[:, 0:-1]
Y = dataset[:, -1]
# 特徵標準化
X -= X.mean(axis=0)
X /= X.std(axis=0)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
print(X_train.shape)

# 定義模型
model = Sequential()
model.add(Dense(10, input_shape=(X_train.shape[1],), activation="relu"))
model.add(Dense(10, activation="relu"))
model.add(Dense(1, activation="sigmoid"))
# model.summary()   # 顯示模型摘要資訊
# 編譯模型
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# 訓練模型
history = model.fit(X_train, Y_train, validation_split=0.2, epochs=20, batch_size=10)
# 評估模型
loss, accuracy = model.evaluate(X_train, Y_train)
print("訓練資料集的準確度 = {:.2f}".format(accuracy))
loss, accuracy = model.evaluate(X_test, Y_test)
print("測試資料集的準確度 = {:.2f}".format(accuracy))

# pip install matplotlib
import matplotlib.pyplot as plt


# 顯示訓練和驗證損失的圖表
loss = history.history["loss"]
val_loss = history.history["val_loss"]
epochs = range(1, len(loss)+1)
plt.plot(epochs, loss, "b-", label="Training Loss")  
# plt.plot() 用於繪製曲線。"bo" 代表藍色（b）的圓點（o），用於顯示訓練損失的數據點。label="Training Loss" 設定圖例標籤。
plt.plot(epochs, val_loss, "r--", label="Validation Loss")
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