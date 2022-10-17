import json
import math
import tkinter as tk
from tkinter import filedialog
import pyautogui
import os

window_width = 1200
window_size = [window_width, int(window_width * 9/16)]
top_margin = 70
r = 35
obj = {}
entries = []

root = tk.Tk()
root.title("Keymap Editor")
root.geometry(str(window_size[0]) + "x" + str(window_size[1]))

canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

img = [
    tk.PhotoImage(file="icons/open.png"),
    tk.PhotoImage(file="icons/save.png")
]

fTyp = [("", "json")]
iDir = os.path.abspath(os.path.dirname(__file__))
def open_file():
    global obj
    try:
        file_name = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
        print("opening: " + file_name)
        with open(file_name) as f:
            loadedJSON = json.load(f)
            obj = loadedJSON
        window_size[1] = top_margin + math.floor(window_size[0] / 10 * (obj["max_y"]+0.5))
        root.geometry(str(window_size[0]) + "x" + str(window_size[1]))
        root.title(os.path.basename(file_name) + " - Keymap Editor")
        place_keys()
    except:
        print("an exception")
        import traceback
        traceback.print_exc()
def save_file():
    global obj, entries
    try:
        #print("len ent: " + str(len(entries)))
        #print("obj: " + str(obj))
        new_keys = list(map(lambda ent: ent.get(), entries))
        #print("len new_keys: " + str(len(new_keys)))
        abc = list("abcdefghijklmnopqrstuvwxyz")
        todo = list("abcdefghijklmnopqrstuvwxyz")
        for i, k in enumerate(new_keys):
            if k in abc and k in todo:
                obj["keys"][i]["key"] = k
                todo.remove(k)
            else:
                obj["keys"][i]["key"] = ""
        place_keys()
        
        filename = filedialog.asksaveasfilename(filetypes=fTyp, initialdir=iDir, initialfile="keymap.json", defaultextension="json")
        print("saving at: " + filename)
        with open(filename, 'w') as f:
            json.dump(obj, f, indent=4)
    except:
        print("an exception")
        import traceback
        traceback.print_exc()

def open_handler(e):
    root.after(1, open_file)
def save_handler(e):
    root.after(1, save_file)

button_open = tk.Button(root, image=img[0], text="open", compound="top")
button_save = tk.Button(root, image=img[1], text="save", compound="top")
button_open.place(x=window_width-120, y=10)
button_save.place(x=window_width-60, y=10)
button_open.bind("<1>", open_handler)
button_save.bind("<1>", save_handler)

def key_handler(e):
    global obj
    if e.keycode in [8, 9, 16, 17, 46]: #BS Tab Ctrl Sft Delete
        #print('not tab')
        pass
    elif e.state == 4 and e.keysym == "s":
        save_file()
    else:
        #print(e)
        pyautogui.press("tab")

#canvas.create_line(20, 10, 280, 190, fill = "Blue", width = 5)
def place_keys():
    global obj, entries
    entries = []
    canvas.delete("all")
    for i, key in enumerate(obj["keys"]):
        center = {
            "x": key["x"]/10*window_size[0],
            "y": top_margin + key["y"]/10*window_size[0]
        }
        if key["home"]:
            fill_color = "#FFFFDF"
        else:
            fill_color = "#FFFAFA"
        canvas.create_oval(center["x"] - r, center["y"] - r,
                            center["x"] + r, center["y"] + r,
                            fill=fill_color)

        entry_height = 45
        txt = tk.Entry(root, width=1, font=("Courier New", int(entry_height/2)))
        txt.insert(0, key["key"])
        txt.bind("<KeyPress>", key_handler)
        txt.place(
            x=center["x"] - entry_height/2/2, 
            y=center["y"] - entry_height/2,
            width=entry_height/2,
            height=entry_height
        )
        entries.append(txt)


root.mainloop()
