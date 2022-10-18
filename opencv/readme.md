# How to create your own keymap

## Windows
1. Open a command prompt at `opencv/`
2. run:
```
	keymap_generator.exe example.png
```
3. input the real layout width and height(mm)
4. run:
```
	keymap_editor.exe
```

## Linux or Mac
1. Install Python, tkInter, OpenCV.
2. ```cd opencv```
3. run:
```
	keymap_generator.py example.png
```
4. input the real layout width and height(mm)
5. run:
```
	keymap_editor.exe
``` 

# Description 

A *keymap* JSON file includes data of both physical and software layout of a keyboard.

you will take **3 steps** to get your JSON ready.

1. ### prepare a blueprint's screenshot.

	We convert an .png/.jeg image into a normalized JSON file.You need to have some screenshots like follows:
	
	![standard layout](https://raw.githubusercontent.com/oha-Ohashi/spring-keeb-search/main/opencv/layouts/standard/standard.png)
	![Waihah41](https://github.com/oha-Ohashi/spring-keeb-search/blob/main/opencv/layouts/Waihah41/waihah41.png?raw=true)

	!Constraints! 

    - Anything other than keys should not be shown.
    - Backgruond color is supposed to be pure white.
    - A keyboard needs 26 keys or more. And 8 of them must be circles. Ther represents so-called *home position*.  
	- It doesn't matter those keys are filled or not.

2. ### Generate a `keymap.json` with `keymap_generator.exe(.py)`
	- You will pass the file path as a command line argument.
	- You will be asked the keyboard's real width and height in millimeters

3. ### Edit the `keymap.json` on the GUI app
	`keymap_editor.exe(.py)` is a GUI application. You can open, edit, and save keymaps here.
	
	By default, `keymap.json` has a software layout of A-Z order. You will have to rewrite it.

