import tkinter as tk
from tkinter import *

w = tk.Tk()

class display:
    w.minsize(500,500)
    
    def generate ():
        c = Canvas(w,bg='lightgray',width=450, height=450)
        
        c.pack()
        

    
    w.title('Laby')
    button = tk.Button(w, text='Generate', width=15,command=generate, activebackground='blue', activeforeground='white', bg='lightgray')
    button.pack()
    
    w.mainloop()

    