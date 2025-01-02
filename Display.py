import tkinter as tk
from tkinter import *

w = tk.Tk()

class display:
    w.minsize(1000,700)
    
    def generate ():
        c = Canvas(w,width=450, height=450)
        c.create_line(0,200,450,200)

    
    w.title('Laby')
    button = tk.Button(w, text='Generate', width=15,command=generate)
    button.pack()
    
    w.mainloop()

    