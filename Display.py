import tkinter as tk #librarie utilisée pour le projet
from tkinter import *
import Algorithm as alg #importation du fichier Algorithm pour générer le labyrinthe

w = tk.Tk() #création de la fenêtre
c = Canvas(w,width=450, height=450) #creation du canvas pour dessiner

class display:
    w.minsize(500,500) #taille fenêtre
    
    def generate ():
        c.delete("all") #effacer le contenu du canvas
        pas = 20
        laby = alg.genlaby() #reception du laby

        #affichage
        for i in range(1,18):
            for j in range(1,18):
                if laby[i][j] is not None:
                    if not laby[i][j].haut: c.create_line((i)*pas, (j)*pas, (i)*pas+pas, (j)*pas, fill='black')
                    if not laby[i][j].bas: c.create_line((i)*pas, (j)*pas+pas, (i)*pas+pas, (j)*pas+pas, fill='black')
                    if not laby[i][j].gauche: c.create_line((i)*pas, (j)*pas, (i)*pas, (j)*pas+pas, fill='black')
                    if not laby[i][j].droite: c.create_line((i)*pas+pas, (j)*pas, (i)*pas+pas, (j)*pas+pas, fill='black')
        c.pack()
        
        

    
    w.title('Laby')
    #creation du bouton
    button = tk.Button(w, text='Generate', width=15,command=generate, activebackground='blue', activeforeground='white', bg='lightgray')
    button.pack()
    
    w.mainloop()

    