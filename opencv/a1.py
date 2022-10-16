import cv2

# 画像ファイルの読込み
# （画像ファイルを用意して下さい。）
img = cv2.imread('sample01.jpg')

# GUIに表示
cv2.imshow('img', img)
# GUI上で何かキーをおすと、ウインドウが消える
cv2.waitKey(0)
cv2.destroyAllWindows()