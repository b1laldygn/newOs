import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os

def openFile():
    filepath = filedialog.askopenfilename(initialdir="/",
                                          title="Dosya aç:",
                                          filetypes= (("tüüüm Dosyalar","*.*"),
                                          ("txt dosyaları","*.txt")))
    os.startfile(filepath)

window = Tk()
button = Button(text="aç",command=openFile)
button.pack()
window.mainloop()
window.geometry("200x200+50+100")