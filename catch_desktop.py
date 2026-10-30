from PIL import Image
from PIL import ImageGrab
import ocr
import tkinter as tk

length = 0
height = 0
x1 = 0
y1 = 0

def take_screenshot():
    global length, height, x1, y1,root
    x1 = root.winfo_x()
    y1 = root.winfo_y()
    length = root.winfo_width()
    height = root.winfo_height()
    img = ImageGrab.grab()
    img.crop((x1,y1,x1+length,y1+height)).save("./output/screenshot_cropped.jpg")
    print("Screenshot saved")
    root.after(1000, take_screenshot)

def start_move(event):
    global _offset_x,_offset_y
    _offset_x = event.x
    _offset_y = event.y

def do_move(event):
    x = root.winfo_x() + event.x - _offset_x
    y = root.winfo_y() + event.y - _offset_y
    root.geometry(f"+{x}+{y}")

root = tk.Tk()
root.geometry("800x600")
root.bind("<ButtonPress-1>", start_move)
root.bind("<B1-Motion>", do_move)
root.overrideredirect(True)
root.relief = "solid"
root.attributes("-topmost", True)
root.attributes("-alpha",0.3)

root.after(1000,take_screenshot)
root.mainloop()
