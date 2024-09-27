"""
list 進階處理

##
注意 list 資料有可變性，如果直接把某 list 的資料給另一個新變數去做更動，會影響到原本的 list。
##

"""

# 1.切片 slice
# players = ['charles', 'martina', 'michael', 'florence', 'eli', ['123', '456']]
#   #		     0          1          2           3          4          5
# print(players[:])  # 不打參數, 切片預設為頭到尾
# print(players[: 3])  #　取前三
# print(players[::2])  # 取一次, 走兩步再取一次  [ 頭 : 尾 : 每一步的大小 ]
# print(players[::-1])  # 倒過來讀取list
# print(players[1:4])  # 取 'martina', 'michael', 'florence'

# 2.賦值差異

# new_players_2 = players[:]  # 等同於把元素淺層複製過去給新變數創建新列表
# print(new_players_2, players)
# new_players_2[0] = 'Brian'
# new_players_2[5][0] = '789'
# print(new_players_2, players)

# new_players_1 = players  # 如同共用一個列表，會互相影響
# print(new_players_1, players)
# new_players_1[0] = 'Brian'
# print(new_players_1, players)

### 額外補充: 使用 copy 模組 完整複製列表給新變數使用範例，看深度複製以及淺複製差別
# import copy
#
# new_players_3 = copy.deepcopy(players)  # deep adj. 深度的
# # new_players_3 = copy.copy(players)  # 淺複製
# print(new_players_3)
# new_players_3[0] = 'Brian'
# new_players_3[5][0] = '789'
# print(new_players_3)
# print(players)

###

# 3. 新增元素到 list

# 3-1 append  新增元素到 list 的最後面

# my_foods = ['pizza', 'falafel', 'carrot cake']
# my_foods.append('sushi')  # 會直接修改 my_foods 的結構，不用重新賦值給 my_foods
# print(my_foods)
#
#
# 3-2 extend  與另一個資料元素合併，也是從後面開始插入元素
# others_foods = ['apple', 'banana', 'fried chicken']
# my_foods.extend(others_foods)  # 'apple', 'banana', 'fried chicken' 依照順序插入 my_foods 後面
# print(my_foods)
# my_foods.append(others_foods)  # 會把 others_foods 這個 list 當成一個元素新增到最後面
# print(my_foods)
#
#
# my_foods.extend(123)  # 會錯，因為只有一個不可拆的數字資料
# print(my_foods)
# my_foods.extend('apple')  # 會拆成 'a','p','p','l','e'
# print(my_foods)
# my_foods.extend(('apple', 'banana', 'fried chicken'))  # 改成 entend 元組
# print(my_foods)
# my_foods.extend({'name': 'Brian', 'year': 11,})  # 只會插入 keys
# print(my_foods)


# 練習 不使用extend，使用迴圈將 others_foods 新增到 my_foods
# my_foods = ['pizza', 'falafel', 'carrot cake']
# others_foods = ['apple', 'banana', 'fried chicken']


# 4. insert 指定在某個index插入元素
# my_foods.insert(1, 'sushi')
# print(my_foods)

# 5. sort, sorted 排序列表
# sort 會直接改變原本的列表順序
# sorted 不會改變原本的列表，會回傳排序後的新列表給你
# rand_list = [23, 87, 45, 12, 68, 34, 91, 56, 74, 29]
# rand_list.sort()
# print(rand_list)
# rand_list.sort(reverse=True)
# print(rand_list)

# new_list = sorted(rand_list)
# print(rand_list)
# print(new_list)


"""
dict 進階

##
注意 dict 資料有可變性，如果直接把某 dict 的資料給另一個新變數去做更動，會影響到原本的 dict。
##

"""

# hero_1 = {
# 	'name': 'Crazy John',
# 	'career': 'cow boy',
# 	'id': 1001,
# }

# 新增 key-value 給字典
# hero_1['age'] = 25
# hero_1['sexaul'] = 'Male'
# hero_1['skills'] = {
# 	'1': "111",
# 	'2': '222',
# 	'3': '333',
# }
# print(hero_1)

# hero_1_cn = {
# 	'綽號': '牛仔',
# 	'年齡': '25',
# 	'技能': {'第四個技能': '444'},
# 	'id': 2002,
# }
#
# hero_1.update(hero_1_cn)  # update v. 更新, 如果有重複的key, 新的會蓋過舊的
# print(hero_1)
# hero_1['skills'].update(hero_1_cn['技能'])  # 可以更新字典裏面的字典
# print(hero_1)

#List 刪除指令:
#1. 刪除特定元素:
# my_list = [1, 2, 3, 4, 5]
# my_list.remove(3)  # 刪除值為 3 的第一個元素
# print(my_list)  # [1, 2, 4, 5]

#2. 刪除特定索引的元素:
# my_list = [1, 2, 3, 4, 5]
# del my_list[2]  # 刪除索引為 2 的元素
# print(my_list)  # [1, 2, 4, 5]

#3. 使用 pop 刪除特定索引的元素:
# my_list = [1, 2, 3, 4, 5]
# i_pop = my_list.pop(3)  # 刪除並返回索引為 2 的元素
# my_list.pop()  # 不給index會刪除最後一個
# print(my_list, i_pop)  # [1, 2, 3, 5]

# #4. 刪除全部元素:
# my_list = [1, 2, 3, 4, 5]
# my_list.clear()  # 清空列表
# print(my_list)  # []

#Dictionary 刪除指令:
#1. 刪除特定鍵值對:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# del my_dict['b']  # 刪除鍵為 'b' 的鍵值對
# print(my_dict)  # {'a': 1, 'c': 3}

# #2. 使用 pop 刪除特定鍵值對:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_dict.pop('b')  # 刪除並返回鍵為 'b' 的值
# print(my_dict)  # {'a': 1, 'c': 3}

#3. 刪除全部鍵值對:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_dict.clear()  # 清空字典
# print(my_dict)  # {}

