import tkinter as tk
from tkinter import *
import Algorithm as alg

w = tk.Tk()

class display:
    w.minsize(500,500)
    
    def generate ():

        c = Canvas(w,bg='lightgray',width=450, height=450)
        pas = 20
        laby = alg.genlaby()
        for i in range(1,19):
            for j in range(1,19):
                if laby(i,j) is not None:
                    if not laby(i,j).haut: c.create_line((i-1)*pas, (j-1)*pas, (i-1)*pas+pas, (j-1)*pas, fill='black')
                    if not laby(i,j).bas: c.create_line((i-1)*pas, (j-1)*pas+pas, (i-1)*pas+pas, (j-1)*pas+pas, fill='black')
                    if not laby(i,j).gauche: c.create_line((i-1)*pas, (j-1)*pas, (i-1)*pas, (j-1)*pas+pas, fill='black')
                    if not laby(i,j).droite: c.create_line((i-1)*pas+pas, (j-1)*pas, (i-1)*pas+pas, (j-1)*pas+pas, fill='black')
        c.pack()
        
        

    
    w.title('Laby')
    button = tk.Button(w, text='Generate', width=15,command=generate, activebackground='blue', activeforeground='white', bg='lightgray')
    button.pack()
    
    w.mainloop()

    