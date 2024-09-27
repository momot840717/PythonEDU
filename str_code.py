# # 1. 連接字串
# # 可以使用 + 運算符或 join 方法來連接字串
#
# # 最一般的方法 使用 '+' 運算符 把每個字加起來，如果字很多會打字打到手累，程式碼也會太長。
# str1 = "Hello"
# str2 = "World"
# result = str1 + " " + str2
# # print(result)  # "Hello World"
#
# text = "hello world"
# print(text.upper())      # 輸出: "HELLO WORLD"
# print(text.lower())      # 輸出: "hello world"
# print(text.capitalize()) # 輸出: "Hello world"
# print(text.title())      # 輸出: "Hello World"
#
#
# text = "   Hello World   "
# print(text.strip())  # 輸出: "Hello World"
# print(text.lstrip()) # 輸出: "Hello World   "
# print(text.rstrip()) # 輸出: "   Hello World"


# 以下是比較重要的
# text = "Hello World"
# print(text.replace("World", "Python"))  # replace v. 取代 ,replace 取代 World 變為 Python, 輸出: "Hello Python"


# 使用 join 方法，把 list 裡面的字串使用指定字串來做連接
# words = ["Hello", "World", "HI", "Brian", "I", "love", "stock"]
# result = " ".join(words)  # 這裡使用一個空格字串連接所有文字元素
# print(result)  # "Hello World HI Brian I love stock"
#
#
# text = "Hello World HI Brian I love stock"
# words = text.split(" ")  # split v.切片, 使用空格拆分字串
# print(words)  # 輸出: ['Hello', 'World', 'HI', 'Brian', 'I', 'love', 'stock']


# baseball_site_data = '''146144^7^2^日职棒-NPB^日職棒-NPB^NPB^65^欧力士猛牛^歐力士野牛^Orix Buffaloes^67^乐天鹰^東北樂天金鷹^RAKUTEN GOLDEN EAGLES^0^0^0^0^0^1^0^0^0^0^0^0^^2^^^^^^^0^3^2^6^0^0^1^#009900^2024,8,13,17,0^^1.85^1.92^1^1'''
# score_list = baseball_site_data.split('^')[14:-12]
# print(score_list)



