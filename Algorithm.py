import random

class Position:
  def __init__(self, x, y):
    self.x = x
    self.y = y


class Carree:
  def __init__(self, visite, bas, haut, gauche, droite):
    self.visite = visite
    self.bas = bas
    self.haut = haut
    self.gauche = gauche
    self.droite = droite



def genlaby():
    posx=0 #colonnes
    posy=0 #lignes
    hasard=0 #hasard direction
    trajet=[Position(x,y) for x in range(18) for y in range(18)] #tableau pour sauvegarder le trajet de mon générateur de labyrinthe
    compteur=0 #nombre de cases visité
    laby = [[Carree(False, False, False, False, False) for i in range(19)] for j in range(19)]



    #chaque case de laby as ses propre caractéristiques (bas,haut,gauche,droite,visite)
    # for posx in range(19):
    #   for posy in range(19):
    #     laby[posx,posy]=new Carree

    # #chaque case de trajet a sa propre position
    # for compteur in range(324):
    #   trajet[compteur]=new Position


    #bordure du laby (0 à 19)
    for posx in range(19):
        laby[posx][18].visite=True
        laby[posx][0].visite=True

    for posy in range(19):
        laby[0][posy].visite=True
        laby[18][posy].visite=True


    compteur=1 #le trajet est pas encore commencé


    #on commence dans la case (1,1)
    posx=1
    posy=1
    while compteur>0 and compteur<325:
        hasard=random.randint(1, 4) # on génère un nombre entre 1 et 4 pour déterminer la direction
        #si on est bloqué, retourne à la dernière case avec d'autres possibilités
        if laby[posx][posy+1].visite==True and laby[posx][posy-1].visite==True and laby[-1][posy].visite==True and laby[posx+1][posy].visite==True:
            laby[posx][posy].visite=True
            posx=trajet[compteur-1].x
            posy=trajet[compteur-1].y
            compteur=compteur-1

            #bas=1
        elif hasard==1 and laby[posx][posy+1].visite==False: #si hasard=1 et la case en bas de nous n'est pas encore visité 
            laby[posx][posy].visite=True # la case qu'on est dedans est maintenant visité
            laby[posx][posy].bas=True #détruire mur
            laby[posx][posy+1].haut=True
            trajet[compteur].x=posx
            trajet[compteur].y=posy  #garder en mémoire le trajet de mon algorithme
            compteur=compteur+1  #le nombre de cases visité s'incrémente de 1
            posy=posy+1

            #haut=2
        elif hasard==2 and laby[posx][posy-1].visite==False: #si hasard=2 et la case en haut de nous n'est pas encore visité 
            laby[posx][posy].visite=True
            laby[posx][posy].haut=True
            laby[posx][posy-1].bas=True
            trajet[compteur].x=posx
            trajet[compteur].y=posy
            compteur=compteur+1
            posy=posy-1

            #gauche=3
        elif hasard==3 and laby[posx-1][posy].visite==False: #si hasard=3 et la case à gauche de nous n'est pas encore visité 
            laby[posx][posy].visite=True
            laby[posx][posy].gauche=True
            laby[posx-1][posy].droite=True
            trajet[compteur].x=posx
            trajet[compteur].y=posy
            compteur=compteur+1
            posx=posx-1

            #droite=4
        elif hasard==4 and laby[posx+1][posy].visite==False: #si hasard=4 et la case à droite de nous n'est pas encore visité 
            laby[posx][posy].visite=True
            laby[posx][posy].droite=True
            laby[posx+1][posy].gauche=True
            trajet[compteur].x=posx
            trajet[compteur].y=posy
            compteur=compteur+1
            posx=posx+1

    return laby

