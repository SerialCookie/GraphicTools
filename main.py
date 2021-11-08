from traceurdefonctions import *
from trajectoire import *
from syracuse import *
from partition import *

def init():
    """init() -> void
    Fonction d'itinialisation du programme"""

    #Déclaration des variables
    modules=["traceurdefonction","trajectoire","syracuse","partition","aide","d\'arrêt"]
    entree=''
    again=True
    module=''
    #Coeur du programme
    anim_texte("Bonjour utilisateur de GraphicTools ! Voici la liste des modules disponibles pour l\'instant... Fais ton choix :\n")
    while again==True:
        entree=input('-------------------------------------------------\n\
Entrer 1 pour le module Traceur de fonctions\n\
Entrer 2 pour le module Trajectoire\n\
Entrer 3 pour le module Syracuse\n\
Entrer 4 pour le module Partition\n\
Entrer \'n\' si vous souhaitez arrêter le programme\n\
Entrer \'help\' si vous souhaitez avoir de l\'aide\n\
-------------------------------------------------\n')
        try:
            module=modules[int(entree)-1]
        except:
            if entree=='help':
                module='aide'
            elif entree=='n':
                module='d\'arrêt'
                again=False
        lancement=module in modules[0:-1]
        anim_texte("Lancement du module {}".format(module)) if lancement or module in modules else anim_texte("La saisie est invalide...")
        exec("{}_init()".format(module)) if lancement else None

def aide_init():
    """aide_init() -> void
    Module d'aide"""

    liens=["https://docs.google.com/document/d/1jAy2CUQJjVbk5HtR4tKJFT5cjPX4zfr2V3BPbdUuDEo/edit#bookmark=id.bwcbs9oy00fh",\
    "https://docs.google.com/document/d/1jAy2CUQJjVbk5HtR4tKJFT5cjPX4zfr2V3BPbdUuDEo/edit#bookmark=id.je47c6r4s26v",\
    "https://docs.google.com/document/d/1jAy2CUQJjVbk5HtR4tKJFT5cjPX4zfr2V3BPbdUuDEo/edit#bookmark=id.8xmhlolv9qs4",\
    "https://docs.google.com/document/d/1jAy2CUQJjVbk5HtR4tKJFT5cjPX4zfr2V3BPbdUuDEo/edit#bookmark=id.66xk792eo9db"]
    anim_texte('Pour quel module souhaitez-vous avoir de l\'aide ? :\n')
    entree=input('-------------------------------------------------\n\
Entrer 1 pour le module Traceur de fonctions\n\
Entrer 2 pour le module Trajectoire\n\
Entrer 3 pour le module Syracuse\n\
Entrer 4 pour le module Partition\n\
-------------------------------------------------\n')
    try:
        webbrowser.open(liens[int(entree)-1])
    except:
        anim_texte('La saisie est invalide...')
        aide_init()

if __name__=="__main__":
    init()