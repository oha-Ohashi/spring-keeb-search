import json
import math
import tkinter as tk
from turtle import circle

window_size = [1200, 0]
input_path = "output.json"
r = 35
obj = []
with open(input_path) as f:
    obj = json.load(f)
ys = list(map(lambda key: key["y"], obj))
print(max(ys))
window_size[1] = math.floor(window_size[0] / 10 * (max(ys)+0.5)) 

root = tk.Tk()
root.geometry(str(window_size[0]) + "x" + str(window_size[1]))

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

#canvas.create_line(20, 10, 280, 190, fill = "Blue", width = 5)
for key in obj:
    center = {
        "x": key["x"]/10*window_size[0],
        "y": key["y"]/10*window_size[0]
    }
    canvas.create_oval(center["x"] - r, center["y"] - r,
                        center["x"] + r, center["y"] + r)

root.mainloop()