import sys
from  tkinter import *
import time 

def times():
    current_time=time.strftime("%H:%M:%S") 
    clock.config(text=current_time)
    clock.after(200,times)


root=Tk()
root.geometry("500x250")
clock=Label(root,font=("times",50,"bold"),bg="black",fg='blue')
clock.grid(row=2,column=2,pady=25,padx=100)
times()

digi=Label(root,text="Saat",font="times 24 bold",fg="red")
digi.grid(row=0,column=2)

nota=Label(root,text="saat   dakka   saniye   ",font="times 15 bold")
nota.grid(row=3,column=2)

root.mainloop()