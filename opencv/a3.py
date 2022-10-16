import cv2
import numpy as np
import matplotlib.pyplot as plt

# 画像ファイルの読込み
# （画像ファイルを用意して下さい。）
img = cv2.imread('waihah41.png')


# 画像をグレースケールにする
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray', gray)
#しきい値指定によるフィルタリング
#retval, dst = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY )
#cv2.imshow('dst1', dst)

dst = cv2.bitwise_not(gray)
#cv2.imshow('dst2', dst)

contours, _ = cv2.findContours(dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
	# 輪郭線の長さを計算
	arclen = cv2.arcLength(cnt, True)
	# 輪郭線の近似
	approx = cv2.approxPolyDP(cnt, 0.01 * arclen, True)
	# 何角形かを見てみる
	#print(len(approx), end='')
	if(len(approx) == 4):
		print("4 です")
		print(cnt)
    # 輪郭線の描画
    #cv2.drawContours(dst, [approx], -1, (255, 0, 0), 3, cv2.LINE_AA)

cv2.drawContours(img, contours, -1, (255, 0, 0), 3, cv2.LINE_AA)
plt.imshow(img)
plt.show()

for cnt in contours:
    # 輪郭線の長さを計算
    arclen = cv2.arcLength(cnt, True)
    # 輪郭線の近似
    approx = cv2.approxPolyDP(cnt, 0.01 * arclen, True)
    n_gon = len(approx)
	


# GUIに表示
# GUI上で何かキーをおすと、ウインドウが消える
cv2.waitKey(0)
cv2.destroyAllWindows()

