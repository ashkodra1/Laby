import tkinter as tk
from tkinter import *
import Algorithm as alg

w = tk.Tk()
c = Canvas(w,bg='lightgray',width=450, height=450)

class display:
    w.minsize(500,500)
    
    def generate ():
        c.delete("all")
        pas = 20
        laby = alg.genlaby()
        for i in range(1,19):
            for j in range(1,19):
                if laby[i][j] is not None:
                    if not laby[i][j].haut: c.create_line((i)*pas, (j)*pas, (i)*pas+pas, (j)*pas, fill='black')
                    if not laby[i][j].bas: c.create_line((i)*pas, (j)*pas+pas, (i)*pas+pas, (j)*pas+pas, fill='black')
                    if not laby[i][j].gauche: c.create_line((i)*pas, (j)*pas, (i)*pas, (j)*pas+pas, fill='black')
                    if not laby[i][j].droite: c.create_line((i)*pas+pas, (j)*pas, (i)*pas+pas, (j)*pas+pas, fill='black')
        c.pack()
        
        

    
    w.title('Laby')
    button = tk.Button(w, text='Generate', width=15,command=generate, activebackground='blue', activeforeground='white', bg='lightgray')
    button.pack()
    
    w.mainloop()

    