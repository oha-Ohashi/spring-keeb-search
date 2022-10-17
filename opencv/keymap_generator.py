from math import floor
import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
import json
import sys


img_path = sys.argv[1]
json_path = "keymap.json"
# 画像ファイルの読込み
img = cv2.imread(img_path)
if type(img).__module__ != np.__name__:
	print("image loading failed.")
	sys.exit()
height, width, channels = img.shape[:3]

# 画像をグレースケールにする
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = cv2.bitwise_not(gray)

contours, _ = cv2.findContours(dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# pt0-> pt1およびpt0-> pt2からの
# ベクトル間の角度の余弦(コサイン)を算出
def angle(pt1, pt2, pt0) -> float:
    dx1 = float(pt1[0,0] - pt0[0,0])
    dy1 = float(pt1[0,1] - pt0[0,1])
    dx2 = float(pt2[0,0] - pt0[0,0])
    dy2 = float(pt2[0,1] - pt0[0,1])
    v = math.sqrt((dx1*dx1 + dy1*dy1)*(dx2*dx2 + dy2*dy2) )
    return (dx1*dx2 + dy1*dy2)/ v

stock = []

for cnt in contours[::-1]:
	# 輪郭線の長さを計算
	arclen = cv2.arcLength(cnt, True)
	# 輪郭線の近似
	approx = cv2.approxPolyDP(cnt, 0.01 * arclen, True)
	# 何角形かを見てみる
	if approx.shape[0] == 4 and cv2.isContourConvex(approx):
		#print("4 です")
		#print(approx)
		maxCosine = 0

		for j in range(2, 5):
			# 辺間の角度の最大コサインを算出
			cosine = abs(angle(approx[j%4], approx[j-2], approx[j-1]))
			maxCosine = max(maxCosine, cosine)

		if maxCosine < 0.1:
			xy = np.mean(approx, axis=0) / width * 10
			#print(xy[0])
			can_appended = True
			for s in stock:
				##print(math.dist(s, xy[0]))
				if math.dist(s["xy"], xy[0]) < 0.5:
					can_appended = False
			if can_appended:
				stock.append({"xy": xy[0], "home": False})
					#print(type(ap[0]))
					#print(len(ap[0]))
	elif approx.shape[0] > 10 and cv2.isContourConvex(approx):
		xy = np.mean(approx, axis=0) / width * 10
		can_appended = True
		for s in stock:
			##print(math.dist(s, xy[0]))
			if math.dist(s["xy"], xy[0]) < 0.5:
				can_appended = False
		if can_appended:
			stock.append({"xy": xy[0], "home": True})

res = []
max_y = 0
abc = list("abcdefghijklmnopqrstuvwxyz")
for i, s in enumerate(stock):			
	c = ""
	if i < len(abc):
		c = abc[i]
	res.append({
		"x": round(s["xy"][0], 2),
		"y": round(s["xy"][1], 2),
		"home": s["home"],
		"key": c})
	if max_y < round(s["xy"][1], 2):
		max_y = round(s["xy"][1], 2)

print(str(len(res)) + "keys detected!")
width = int(input("layout width (integer, unit = mm): "))
height = int(input("layout height (integer, unit = mm): "))
res = {"width": width, "height": height, "max_y": max_y, "keys": res}
with open(json_path, 'w') as f:
    json.dump(res, f, indent=4)

print("keymap saved at \""+json_path+"\"")
