"""
Pandas 是一個基於 Python 的數據分析工具，提供高效能、易於操作的數據結構，適用於資料處理與分析。
"""
import pandas as pd


# 主要物件

# pd 的 Series：一維數據結構。

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# print(s)

# DataFrame：二維數據結構，類似於 Excel 表格。往後可以使用 pd 編輯 excel 檔案

# 方法1.使用字典轉成表格(df)
data = {
    'Name': ['Alice', 'Bob'], 
    'Age': [25, 30]
    }
df = pd.DataFrame(data)
# print(df)

# 方法2.先設定欄位名稱再塞入資料(資料用list)
columns = ['Name', 'Age']
data_list = [
    ['Alice', 25],
    ['Bob', 30],
    ['Charlie', 35]
]
df2 = pd.DataFrame(data, columns=columns)
# print(df2)

# 創建新欄位新資料
df['id'] = [1, 2]
print(df)

# 轉換型態
df['Age'] = df['Age'].astype(str)
print(df)

# 使用索引搜尋表格範圍 (.loc, .iloc)

print(df.loc[0, 'Name'])  # 使用標籤索引 (第一個參數:表格的index, 第二個參數: 欄位名稱)
# print(df.iloc[1, 0])      # 使用整數索引 (第一個參數:表格的index, 第二個參數: 欄位所在的index)
print(df.loc[0]) 
print(df.iloc[0]) 

# 使用 NumPy 函數進行數值運算範例。

import numpy as np

# print(np.log(df['Age']))
# df['Age'] = np.log(df['Age'])  # 要存新數值，要再賦值給原表格，類似修改後存檔的概念
# print(df)



# 處理遺失資料

# 建立帶有缺失值的數據
data_nan = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 30, 28],
    'City': ['New York', 'Los Angeles', np.nan, 'Chicago'],
    'Salary': [50000, 60000, 70000, np.nan]
}

# 創建 DataFrame
df_nan = pd.DataFrame(data_nan)

print(df_nan)


# 1 判斷缺失值

# print(df_nan.isnull())
# print(df_nan.notnull())

# 2 填補缺失數據

# 寫法1
# df_nan = df_nan.fillna(0)  # 用0補空值
# # 寫法2
# df_nan.fillna(0, inplace=True)  # 直接修改 df_nan 不用重新賦值
# print(df_nan)

# 2.1 填補缺失數據的其他方法

# 使用平均值填補
# df_nan['Age'].fillna(df_nan['Age'].mean(), inplace=True)
# print(df_nan)

# 使用中位數填補
# df_nan['Age'].fillna(df_nan['Age'].median(), inplace=True)
# print(df_nan)

# 使用眾數填補
# print(df_nan['City'].mode())
# df_nan['City'].fillna(df_nan['City'].mode()[0], inplace=True)
# 使用 df_nan['Age'].mode() 如果有一樣多的眾數，都可以選，這裡範例選第一個(index=0)
# print(df_nan)

# # 使用前一列值填補
# df_nan.fillna(method='ffill', inplace=True)
# print(df_nan)

# # 使用後一列值填補
# df_nan.fillna(method='bfill', inplace=True)
# print(df_nan)

# # 設定不同欄位不同填充值
df_nan.fillna({'Age': df_nan['Age'].mean(), 'City': 'Unknown'}, inplace=True)
print(df_nan)

## 給你們嘗試補 Salary 的缺值


# 3 刪除缺失數據

# df_nan.dropna()

# 4 數據合併

df_1 = pd.DataFrame({'A': [1, 2]})
df_2 = pd.DataFrame({'A': [3, 4]})
result = pd.concat([df_1, df_2])
# print(result)

# 5.群組運算 groupby
# print(df.groupby('Name'))
# print(list(df.groupby('Name')))
groupby_data = {}
for name, data in df.groupby('Name'):
    # print(name, data)
    groupby_data[name] = data
print(groupby_data)


# 6. 高效數據查詢與計算

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    'Age': [25, 30, 35, 40, 22, 28, 33, 27, 29, 31]
}

df3 = pd.DataFrame(data)
# 寫法1 在 df[] 的框框裡面寫判斷、篩選條件
print(df3[(df3['Age'] >= 25) & (df3['Age']<=35)])

print(df3[df3['Name'].str.len() == 4])

# 寫法2 使用 .query() 用字串寫條件
print(df3.query('25<= Age <=35'))
# print(df3.query('Name == Alice'))  # 為什麼錯呢 猜猜看?
# 小技巧: 當作是在引號裡寫python指令

# 計算的方式創建新欄位

df3['Age_2'] = df3['Age'] * 2 -10
print(df3)

