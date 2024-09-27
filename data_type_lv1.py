"""
數字分為整數跟浮點數(小數)
整數(int): 1 2 3 4 5  5000 10000 1_0000
浮點數(float): 1.0 2.1 3.14
數字資料可計算加減乘除、餘數
整數跟浮點數可以互相計算、最後型態變浮點數
"""

# a = 6
# b = 5
# c = 7.1
# print(a)
# print(b)
# print(a + b)  # 加法
# print(a - b)  # 減法
# print(a * b)  # 乘法
# print(a / b)  # 除法
# print(a // b) # 除法的商
# print(a % b)  # 除完後的餘數
# print(a ** b) # a的b次方
# print(f'a * b = {a * b}')
# print(a + c)  # 整數跟浮點數可以互相計算、最後型態變浮點數


"""
文字
用單引號或雙引號包起來的字都是文字資料
例如:  "123", '456'
使用3個單或雙引號可以放很多字串、如現在的教材用3個雙引號包起來的
"""

# str1 = '123'
# print(str1[0], str1[1], str1[2])
# print(str1[-1])
# str2 = '456'
# print(str1 + str2)


"""
布林 bool 就是判斷 True, False
數字0、None、空資料 --> False， 反之為 True
"""
# bool_number = 0
# result = bool(bool_number)
# result n. 結果
# print(result)


"""
串列 list 用中括號把資料元素包起來 例如: [1, 2, 3, 4]
list_1 = ['1', 1, '2.0', 3.4, [], [1, 2, 3], True, False]  # 串列裡面的元素是甚麼型態都可以
"""
# list_number = [1, 2, 3, 4, 5, 10, 52, 1111]
      # index    0  1  2  3  ....          7
      # index    ................    -2   -1

# length n. 長度
# list_length = len(list_number)  # 我想知道這個串列有多長
# print(list_number[list_length-1])

# python for/while 迴圈
# for num in list_number: # 用迴圈的方式看list每個元素
# 	print(num)

# for num in range(0, list_length, 2):
# 	print('index =', num, '串列元素 =', list_number[num])
# 	print(f"index = {num} 串列元素 = {list_number[num]}")


"""
元組 tuple 用 '小括號' 把資料元素包起來 例如: (1, 2, 3, 4)
!!! 但是在tuple裡面 逗號 才是 tuple 的核心, 沒有小括號, 只有逗號也可以是tuple， 例如: a = 1, 2, 3, 4。 a 就是一個tuple 資料有 1,2,3,4,
但是要生成空的 tuple, 還是要給一個小括號， 例如 a = ()
如果 tuple 只有一個元素，記得給它逗號， 例如 a = (2,) or a = 2,
結構上跟list一樣，但是 tuple 裡面的資料不能做更改
"""
# a = (1, 2, 3, 4)
# print(a, type(a))
# b = 1, 2, 3, 4
# print(b, type(b))
# c = 2,
# print(type(c))

# list_a = [1, 2, 3, 4]
# tuple_a = (1, 2, 3, 4)
# 變更 list_a 的 第一個資料
# list_a[0] = '變更成此字串'
# print(list_a)
# tuple_a[0] = '變更成此字串'  # 這樣會報錯

"""
集合 set
會用 大括號{}包資料，裡面如果有重複的元素會合併成一個
意思就是 set 裡面沒有重複的元素!
"""
# a = set() # 空集合
# list_a = [1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 6, 67, 87, 677, 67, 10, 2]
# set_a = set(list_a)
# print(set_a, type(set_a))

"""
字典 dict
用 大括號 {} 包資料，資料必須以 {key(鍵): value(值)} 的形式呈現。
key 的型態為字串或數字
value 沒有甚麼限制
例如: { 'stock_price': 944 }
"""

# empty_dict = {}  # 空字典直接給大括號
# dict_a = {
# 	'stock_code': '2330',
# 	'stock_price': 944.5,
# 	'可當日沖銷': True,
# 	'也可以放list': [1, 2, 3, '456'],
# 	123: '這邊告訴你 key 可以用數字',
# }
# print(dict_a, type(dict_a))

dict_brian = {
	'name': 'Brian',
	'year': 11,
}
print(dict_brian['name'], dict_brian['year'])




