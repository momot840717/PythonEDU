"""
安裝 NumPy

pip install numpy

引入 NumPy

import numpy as np

as 就是用後面的所寫代替模組名稱
"""

import numpy as np

# 1. 使用列表創建一維矩陣

matrix_1d = np.array([1, 2, 3, 4])
print(matrix_1d)

# 2. 創建多維矩陣

matrix_2d = np.array([[1, 2], [3, 4]])
print(matrix_2d)



# 使用內建函數創建矩陣

# 1. 全零矩陣

zeros_matrix = np.zeros((2, 3))  # 2, 3 是直2寬3的意思
print(zeros_matrix)
zeros_matrix = np.zeros((3, 2, 3))  # 3個 2 X 3 矩陣
print(zeros_matrix)

# 2. 全一矩陣

ones_matrix = np.ones((3, 3))
print(ones_matrix)

# 3.指定範圍的矩陣

range_matrix = np.arange(0, 10, 2)  # 寫法類似for迴圈中的常見的 range()
print(range_matrix)

# 隨機數矩陣

# 1.均勻分布的隨機數矩陣（0 到 1）：

random_matrix = np.random.rand(3, 2)
print(random_matrix)

# 2.標準正態分布的隨機數矩陣（平均值為 0，標準差為 1）：

normal_matrix = np.random.randn(3, 2)
print(normal_matrix)

# 3.指定範圍的隨機整數矩陣：
# randint 可以看成 rand + int 看到int 就知道輸出是整數

int_random_matrix = np.random.randint(1, 10, size=(3, 3))  # 生成2X2矩陣, 數值隨機生成 1 到 9 的"整數"
print(int_random_matrix)

# 4.自定義範圍的隨機數矩陣：

custom_random_matrix = np.random.uniform(5, 15, size=(2, 2))  # 生成2X2矩陣, 數值隨機 5 到 15 的數字
print(custom_random_matrix)

"""
單位矩陣
NumPy 提供了兩種方法創建單位矩陣：np.eye 和 np.identity。
"""
# 使用 np.eye 創建單位矩陣：

identity_matrix = np.eye(3)  # 創建 3x3 單位矩陣
print(identity_matrix)

# np.eye 支持設置對角線的偏移量，例如：

offset_matrix = np.eye(3, k=1)  # 對角線的1向"右"偏移 1 單位的矩陣
print(offset_matrix)

# 使用 np.identity 創建單位矩陣：
# np.identity 只能創建對角線在原始位置的單位矩陣。

identity_matrix = np.identity(3)  # 創建 3x3 單位矩陣
print(identity_matrix)

"""
基本操作
"""

# 1. 訪問元素

matrix = np.array([10, 20, 30, 40])
print(matrix[0])  # 獲取第一個元素
print(matrix[-1]) # 獲取最後一個元素

# 2. 切片操作

matrix = np.array([10, 20, 30, 40, 50])
print(matrix[1:4])  # 獲取第2到第4個元素

### 以上基本操作跟 list 操作差不多

# 3. 基本運算

# 矩陣間的加減乘除

matrix1 = np.array([1, 2, 3])
matrix2 = np.array([4, 5, 6])
print(matrix1 + matrix2)
print(matrix1 * matrix2)

"""
這裡要注意的是這裡的矩陣乘法跟高中的矩陣乘法算法不同

在 NumPy 中，矩陣乘法可以分為兩種方式：元素逐項乘法 和 線性代數的矩陣乘法。
"""
# 1. 元素逐項乘法 ( 這是 NumPy 的默認行為，使用 * 運算符，對應位置的元素逐項相乘)

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = matrix1 * matrix2
print(result)
# Output:
# [[ 5 12]
#  [21 32]]

#  2. 符合高中數學的矩陣乘法  ( 使用 @ 運算符，或通過 np.dot 或 np.matmul 函數實現。)

result = matrix1 @ matrix2  # 或 np.dot(matrix1, matrix2)
print(result)
# Output:
# [[19 22]
#  [43 50]]

"""
計算過程：

第一行第一列：1*5 + 2*7 = 19

第一行第二列：1*6 + 2*8 = 22

第二行第一列：3*5 + 4*7 = 43

第二行第二列：3*6 + 4*8 = 50

"""

# 數學函數

matrix = np.array([1, 2, 3])
print(np.sqrt(matrix))  # 開平方
print(np.exp(matrix))   # e的次方  e^1, e^2, e^3

"""
矩陣的屬性指令
"""
# 1.形狀 (shape)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.shape)  # 輸出 (2, 3)

#### 改變矩陣形狀(非常重要、非常實用)
matrix = np.array([1, 2, 3, 4, 5, 6])
reshaped_matrix = matrix.reshape((2, 3))
print(reshaped_matrix)


# 2.數據類型 (dtype)

matrix = np.array([1, 2, 3], dtype=float)
print(matrix.dtype)

# 創建 float64 矩陣
matrix64 = np.array([1.123456789, 2.123456789], dtype=np.float64)
print("Float64 Matrix:", matrix64)
print("Data Type:", matrix64.dtype)

# 創建 float32 矩陣
matrix32 = np.array([1.123456789, 2.123456789], dtype=np.float32)
print("Float32 Matrix:", matrix32)
print("Data Type:", matrix32.dtype)

# 3.大小 (size)

matrix = np.array([[1, 2], [3, 4]])
print(matrix.size)  # 總元素數量


"""
合併與分割矩陣
"""

# 1.合併矩陣
## 使用 np.concatenate

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6]])
combined_matrix = np.concatenate((matrix1, matrix2), axis=0)  # 沿行拼接
print(combined_matrix)

combined_matrix = np.concatenate((matrix1, matrix2.T), axis=1)  # 沿列拼接  
print(combined_matrix)
"""
# .T 是矩陣旋轉90度的意思
| 5  6 |  =>  | 5 |
              | 6 |
"""

##使用 np.hstack 和 np.vstack

# 水平拼接
h_combined = np.hstack((matrix1, matrix2.T))
print(h_combined)

# 垂直拼接
v_combined = np.vstack((matrix1, matrix2))
print(v_combined)

# 2.分割矩陣
## 使用 np.split

matrix = np.array([1, 2, 3, 4, 5, 6])
split_matrix = np.split(matrix, 2)
print(split_matrix)

## 使用 np.vsplit 和 np.hsplit

# 垂直分割 ：行方向分割，看起來像「水平線分割」
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v_split = np.vsplit(matrix, 3)
print(v_split)

# 水平分割：列方向分割，看起來像「垂直線分割」
h_split = np.hsplit(matrix, 3)
print(h_split)
