from tkinter import *
import time
root = Tk()
root.geometry("160x65+0+0")
root.resizable(0,0)
root.config(bg="black")
root.overrideredirect(1)


def start():
    text= time.strftime("%H:%M:%S")
    lable.config(text=text)
    lable.after(200,start)

lable = Label(root,fg="white",bg="black",font=("comicsansms",29
                                ,"bold"))
lable.grid(row=0,column=1)
start()
root.mainloop()
