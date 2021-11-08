from noyau import *

def traceurdefonction_init():
    """traceurdefonction_init() -> void
    Regroupe toutes les instructions permettant d'utiliser les différentes fonctions du fichier traceurdefonction"""

    plt.clf()
    #Déclaration des variables
    legende=[]
    try:
        nbr_fonctions=abs(int(input('Veuillez entrer le nombre de fonctions à tracer :\n')))
        start=float(input('Veuillez entrer la valeur de x pour laquelle commencer le tracé des fonctions :\n'))
        end=float(input('Veuillez entrer la valeur de x pour laquelle terminer le tracé des fonctions :\n'))
        points=abs(int(input('Veuillez entrer le nombre de points des courbe à calculer entre {0} et {1} :\n'.format(start, end))))
    except ValueError:
        anim_texte("La saisie est invalide...")
        traceurdefonction_init()
    #Coeur du programme
    try:
        for i in range(nbr_fonctions):
            fonction=input('Veuillez entrer la fonction n°{} :\n'.format(i+1))
            tracefonction(fonction, start, end, points)
            legende.append(fonction)
    except:
        anim_texte('Votre saisie ne correspond pas à une expression algébrique valide... Veillez à utiliser x en tant que variable et à utiliser la syntaxe Python')
        traceurdefonction_init()
    plt.legend(legende)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0,color='k')
    plt.show()

def tracefonction(fonction, start, end, points):
    """tracefonction(str, float, float, int) -> void
    Configure la courbe  représentative de la fonction
    fonction : Fonction pour laquelle tracer sa courbe représentative
    start : Abscisse de départ
    end: Abscisses de fin
    points: Nombre de points de la courbe à calculer"""

    #Préconditions
    assert(start<end)
    #Déclaration des variables
    x=Symbol('x')
    fonction=sympify(fonction)
    lx=gen_abs(end, points, start=start)
    ly=[]
    #Coeur du programme
    for i in lx:
        ly.append(fonction.subs({x:i}))
    gen_graph(lx, ly, show_x_axis=False, show_y_axis=False, show_graph=False)