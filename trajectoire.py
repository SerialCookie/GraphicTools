from matplotlib.pyplot import legend
from noyau import *

def trajectoire_init():
    """trajectoire_init() -> void
    Regroupe toutes les instructions permettant d'utiliser les différentes fonctions du fichier trajectoire"""

    #Déclaration des variables
    lignes=[]
    legendes=[]
    try:
        nbr_lancers=int(input('Veuillez entrer le nombre de lancers à effectuer :\n'))
    except ValueError:
        anim_texte("La saisie est invalide...")
        trajectoire_init()
    #Coeur du programme
    try:
        for i in range(nbr_lancers):
            vitesse_intiale=float(input('Veuillez entrer la vitesse initiale du projectile n°{} en m/s :\n'.format(i+1)))
            masse=abs(float(input('Veuillez entrer la masse du projectile n°{} en grammes :\n'.format(i+1))))
            angle=float(input('Veuillez entrer l\'angle du projectile n°{} en degrés :\n'.format(i+1)))
            courbe=calcul_trajectoire(vitesse_intiale, masse, angle)
            legendes.append("Temps de vol : {0} sec | v : {1} | m : {2} | angle : {3}".format(round(courbe[2],2),vitesse_intiale,masse,angle))
            ligne,=gen_graph(courbe[0], courbe[1], show_graph=False)
            lignes.append(ligne)
    except:
        anim_texte('La saisie est invalide...')
        trajectoire_init()
    plt.legend(lignes, legendes)
    plt.show()

def calcul_trajectoire(vitesse, masse, angle):
    """calcul_trajectoire(float, float, float) -> tuple
    Calcule la trajectoire d'un projectile selon sa masse, sa vitesse initiale et l'angle de tir
    vitesse: Vitesse initiale de l'objet
    masse: Masse de l'objet
    angle: Angle de tir en degrés"""

    #Déclaration des variables
    angle=radians(angle)
    g=9.8
    t_vol=2*vitesse*sin(angle)/g
    intervalle=gen_abs(t_vol, 1000)
    lx=[]
    ly=[]
    #Coeur du programme
    for i in intervalle:
        lx.append(vitesse*cos(angle)*i)
        ly.append(vitesse*sin(angle)*i-0.5*g*i**2)
    #Retour de la fonction
    return lx, ly, t_vol