from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
from pygame import mixer
mixer.init()

root = Tk()
root.attributes('-fullscreen', True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    img = Image.open("jarvis.gif") 
    lbl = Label(root)
    lbl.place(x=0, y=0)

    mixer.music.load(r"c:\Users\KAVI PRASANTH\Downloads\jarvis_plug_in.mp3")
    mixer.music.play()

    def update_image():
        for img_frame in ImageSequence.Iterator(img):
            img_frame = img_frame.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
            img_tk = ImageTk.PhotoImage(img_frame)
            lbl.config(image=img_tk)
            lbl.image = img_tk  
            root.update()
            time.sleep(0.05)

    root.after(100, update_image)
    root.after(5000, root.destroy)  

play_gif()
root.mainloop()