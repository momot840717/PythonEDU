import numpy as np
import cv2
"""
pip install opencv-python
"""


# 讀取自己的圖片 (JPG/PNG)，再轉為灰階
img = cv2.imread("Usagi.jpg")  # 檔名不要中文
# 顯示圖片
# cv2.imshow('Usagi', img)  # 用 OpenCV 顯示, 放視窗標題跟圖片物件
# cv2.waitKey(0)  # 參數代表等待的時間，單位是毫秒。0 表示「無限等待」，也就是程式會停在這裡直到按下任意按鍵。
# cv2.destroyAllWindows()  # 關閉視窗

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # cvt -> convert（轉換）
# cv2.imshow('Usagi_gray', gray_img)  
# cv2.waitKey(0) 
# cv2.destroyAllWindows()  # 關閉視窗

kernel = np.array([[ 0,  1, -1],
                   [ 0,  1, -1],
                   [ 0,  1, -1]])


filtered = cv2.filter2D(gray_img, -1, kernel)  # -1 的意思是 保持與輸入影像 (img) 相同的顏色深度範圍 EX: 0~255
filtered2 = cv2.filter2D(img, -1, kernel)
cv2.imshow("Usagi_Filter", filtered)
cv2.imshow("Usagi_Filter2", filtered2)
cv2.imshow('Usagi_gray', gray_img)
cv2.imshow('Usagi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 用 plt 跟 signal 做濾波圖

import matplotlib.pyplot as plt
from scipy import signal
"""
pip install scipy
"""


# 圖片轉為矩陣

# 如果用 Matplotlib 看彩圖，需要先轉換成 RGB 格式
img_for_plot = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_matrix = np.array(img_for_plot)
plt.imshow(img_matrix)  # "image show"
plt.show()

# 灰階圖轉矩陣
gray_img_matrix = np.array(gray_img)

# 自定義多個濾波器 (filters)
filters = [[
    [-1, -1, -1],
    [ 1,  1,  1],
    [ 0,  0,  0]],
   [[-1,  1,  0],
    [-1,  1,  0],
    [-1,  1,  0]],
   [[ 0,  0,  0],
    [ 1,  1,  1],
    [-1, -1, -1]],
   [[ 0,  1, -1],
    [ 0,  1, -1],
    [ 0,  1, -1]]]

# 圖片尺寸
plt.figure(figsize=(12, 6))

# 顯示原始圖片
plt.subplot(1, 5, 1)  # 圖片排列方式及圖片位置: 座位有1列，5個位置，此img要放在第1張的位置 -> (1,5,1)
"""
+-------+-------+-------+-------+-------+
|  Img1 |  Img2 |  Img3 |  Img4 |  Img5 |
+-------+-------+-------+-------+-------+
"""
plt.imshow(gray_img_matrix, cmap="gray")  # cmap="gray" 如果是單通道圖就強制灰階, img_matrix 是 RGB 三通道所以不會轉灰
plt.axis("off")
plt.title("Original")

# 套用 4 個濾波器
for i in range(4):
    plt.subplot(1, 5, i + 2)
    c_img = signal.convolve2d(gray_img_matrix, filters[i])  # signal.convolve2d 進行卷積
    plt.imshow(c_img, cmap="gray")
    plt.axis("off")
    plt.title(f"Filter {i+1}")   

plt.show()
