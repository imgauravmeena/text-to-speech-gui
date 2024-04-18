# Importing necessary modules

from tkinter import *
import customtkinter 
from gtts import gTTS
import os
from PIL import Image, ImageTk

root = customtkinter.CTk()

# Apperance

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root.title("Text to Speech")
root.geometry("573x500")
root.resizable(0,0)
Font = customtkinter.CTkFont(family="Bebas Neue Bold",size = 50)
Font2 = customtkinter.CTkFont(family="Franklin Gothic Medium",size=16)

# Taking Entry as Text

e = customtkinter.CTkEntry(master=root,placeholder_text="Write anything to listen...",width=300, height=40,corner_radius=70, 
border_width=2,border_color="Green",fg_color="transparent", text_color="Green",font=Font2,placeholder_text_color="Green")
e.place(x=140, y = 200)

msg = e.get()

# Making Function To Convert Text to Speech

def send ():
    yo = gTTS(text=msg,lang="en",slow = False)
    yo.save("abc.mp3")
    os.system("start abc.mp3")
    

def reset():
    e.delete(0, END)
    os.remove("abc.mp3")


img = customtkinter.CTkImage(dark_image=Image.open("playcircle.png"),size=(30,30))

eBt = customtkinter.CTkButton(master=root,width=115, height=40,corner_radius=70,text="Play",border_color="#03A9F4",
border_width=2,font=Font2,text_color="#03A9F4",hover_color="#272727", fg_color="transparent",command=send,image=img)
eBt.place(x=225, y=270)

eBt2 = customtkinter.CTkButton(master=root,width=115, height=40,corner_radius=70,text="Reset",border_color="#03A9F4",
border_width=2,font=Font2,text_color="#03A9F4",hover_color="#272727", fg_color="transparent",command=reset)
eBt2.place(x=225, y=325)

lable1 = customtkinter.CTkLabel(root, text="Text to Speech",font =Font,pady=50,padx=170, width=20, height=30).grid(
    row=1,columnspan = 30)

root.mainloop()