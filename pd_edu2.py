import pandas as pd


df1 = pd.read_csv('20250113上市股盤後.csv')
df1 = df1[df1['證券代號'].apply(lambda x: len(x) == 4)]

"""
lambda 匿名函數，可以將簡單的自訂函數縮寫成一行，且不用命名函數名稱

lambda x: x*2
x 是函數的參數
x*2 是 return

也可以使用多變數 例如 lambda x, y: x*2+y*2

lambda x: len(x) == 4 就是判斷 x 長度是否等於4的匿名函數，因為是判斷所以回傳 bool
"""

# 指定'交易日期'放在'欄位index為0'的位置
df1.insert(0, '交易日期', '2025-01-13')  
# print(df1)

df2 = pd.read_csv('20250114上市股盤後.csv')
df2 = df2[df2['證券代號'].apply(lambda x: len(x) == 4)]
df2.insert(0, '交易日期', '2025-01-14')
# print(df2)