"""
for迴圈是在設定範圍內從頭運作到尾，但最後一個會停止不運作
例如: 運作設定範圍0~10, 實際會運作0~9， 10停止不做
"""
# # 使用 range界定for次數
# for i in range(0, 10):
# 	# print(i)  # 0~9 分別換行顯示
# 	# print(i, end='')  # 0~9不換行連起來顯示
# 	'''如果我要不換行 每個 i 格一空格顯示要怎麼設計呢?'''
# 	'Ans:'
# 	print(i, end=' ')

# for i in range(0, 10, 2):  # 每兩個執行一次
# 	print(i)

# for i in range(10, 0, -1):  # 倒過來執行迴圈
	# print(i)



"""
while 迴圈是在條件布林值為True的情況下持續運作，直到條件布林值變為False。
也就是說，如果一直為True，while迴圈就不會停止
"""
# i = 0
# while i <= 10:  # i = 11 的時候停止
# 	print(i <= 10)  # 顯示條件的bool
# 	print(i)
# 	i += 1  # i = i + 1
#
# 	print(i, i <= 10)
#
# while True:
# 	print('No stop looping')


"""
雙重 for 迴圈
"""
print('='*126)
for i in range(1, 10):
	for j in range(2, 10):
		print(f'{j} x {i} = {i*j}', end = '\t||\t')
	print('')
print('='*126)





