from noyau import *

def syracuse_init():
    """syracuse_init() -> void
    Regroupe toutes les instructions permettant d'utiliser les différentes fonctions du fichier syracuse"""

    #Déclaration des variables
    try:
        nombre_depart=abs(int(input('Veuillez entrer le nombre pour lequel appliquer l\'algorithme de Syracuse :\n')))
    except ValueError:
        anim_texte("La saisie est invalide...")
        syracuse_init()
    #Coeur du programme:
    gen=syracuse_gen(nombre_depart)
    plt.text(len(gen[0])/2, max(gen[0])*1.1, "Temps de vol : {}".format(gen[1]), verticalalignment='center', horizontalalignment='center')
    gen_graph(gen_abs(gen[1],gen[1]), gen[0])

def syracuse_gen(nombre):
    """syracuse_gen(int) -> tuple
    Calcule la liste de nombres générés par l'algorithme de Syracuse jusqu'à atteindre le cycle 1 2 4
    nombre: Nombre pour lequel débuter l'algorithme"""

    #Déclaration des variables
    nombre_temporaire=nombre
    liste_syracuse=[nombre_temporaire]
    temps_vol=0
    #Coeur du programme
    while not(nombre_temporaire==1 and liste_syracuse[-4]==1):
        nombre_temporaire=nombre_temporaire/2 if nombre_temporaire%2==0 else nombre_temporaire*3+1
        liste_syracuse.append(nombre_temporaire)
        temps_vol+=1
    #Retour de la fonction
    return liste_syracuse, temps_vol