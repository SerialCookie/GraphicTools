from header import *

def compter_chiffres_decimaux(nombre):
    """compter_chiffres_decimaux(float) -> int
    Compte le nombre de chiffres après la virgule
    nombre: Nombre pour lequel efectuer le décompte"""

    #Déclaration des variables
    nombre=str(float(nombre))
    #Coeur du programme
    nombre=nombre.split('.')[1]
    #Retour de la fonction
    return len(nombre)

def range_decimal(start, end, intervalle=1):
    """range_decimal(float, float, float) -> list
    Génère une liste de nombres à la manière de la fonction range, en prenant en argument des flottants
    start: Début de la liste
    end: Fin de la liste
    intervalle: Intervalle entre les nombres -- 1 par défaut"""

    #Précondition
    assert(start<end)
    #Déclaration des variables
    liste=[]
    longueur_liste=int((end-start)/intervalle+1)
    nombre_variable=start
    arrondi=compter_chiffres_decimaux(intervalle)
    #Coeur de la fonction
    for i in range(longueur_liste):
        liste.append(round(nombre_variable,arrondi))
        nombre_variable+=intervalle
    #Retour de la fonction
    return liste

def gen_abs(end, point, start=0):
    """gen_abs(int, int, float) -> list
    Génère une liste de nombres correspondant aux abscisses des points de la courbe
    end: Abscisse de fin
    point: Nombre de points à calculer
    start: Abscisse de départ -- 0 par défaut"""

    #Préconditions
    assert(start<end)
    #Déclaration des variables
    lx=[]
    scale=(end-start)/point
    #Coeur du programme
    for i in range_decimal(start, end, scale):
        lx.append(i)
    #Retour de la fonction
    return lx

def gen_graph(x,y,show_x_axis=True,show_y_axis=True, show_graph=True):
    """gen_graph(list, list, bool, bool) -> line
    Génère et affiche un graphique à partir de coordonnées de points
    x: Liste des abscisses
    y: Liste des ordonnées
    show_x_axis: Afficher l'axe des abscisses ? -- True par défaut
    show_y_axis: Afficher l'axe des ordonnées ? -- True par défaut
    show_graph: Afficher le graphique ? -- True par défaut"""

    #Coeur du programme
    line=plt.plot(x,y)
    if show_x_axis:
        plt.axhline(y=0, color='k')
    if show_y_axis:
        plt.axvline(x=0, color='k')
    if show_graph:
        plt.show()
    return line

def anim_texte(texte):
    """anim_texte(str) -> void
    Affiche le texte en faisait une animation
    texte: Texte à afficher"""

    #Coeur du programme
    for i in range(len(texte)):
        print(texte[i], end='')
        sys.stdout.flush()
        time.sleep(0.02)
    print()