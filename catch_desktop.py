from PIL import Image
from PIL import ImageGrab
import tkinter as tk

length = 0
height = 0
x1 = 0
y1 = 0

def take_screenshot():
    img = ImageGrab.grab()
    img.crop((x1,y1,x1+length,y1+height)).save("./output/screenshot_cropped.jpg")
    print("Screenshot saved")

root = tk.Tk()
root.title("deslation")
root.geometry("400x400")

tk.Label(root, text="len").pack()
entry_len = tk.Entry(root)
entry_len.pack()

tk.Label(root, text="height").pack()
entry_height = tk.Entry(root)
entry_height.pack()

tk.Label(root, text="x1").pack()
entry_x1 = tk.Entry(root)
entry_x1.pack()

tk.Label(root, text="y1").pack()
entry_y1 = tk.Entry(root)
entry_y1.pack()

def getsize():
    global length,height,x1,y1
    length = int(entry_len.get())
    height = int(entry_height.get())
    x1 = int(entry_x1.get())
    y1 = int(entry_y1.get())

tk.Button(root, text="OK", command=getsize).pack()
tk.Button(root, text="take screenshot", command=take_screenshot).pack()
root.mainloop()
