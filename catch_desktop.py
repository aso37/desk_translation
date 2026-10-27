from PIL import Image
from PIL import ImageGrab
import tkinter as tk

size = 0

def take_screenshot():
    img = ImageGrab.grab()
    img.crop((0,0,size,size)).save("./output/screenshot.jpg")
    print("Screenshot saved")

#print("please enter the lenth and heiht you want:")
#len=float(input())
#height=float(input())
#print(len,height)

root = tk.Tk()
root.title("deslation")
root.geometry("400x400")

entry = tk.Entry(root)
entry.pack()

def getsize():
    global size
    size = int(entry.get())

tk.Button(root, text="OK", command=getsize).pack()
tk.Button(root, text="take screenshot", command=take_screenshot).pack()
root.mainloop()
