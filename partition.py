from noyau import *

note=0
duree=1
rythme=2
ligne=0

def partition_init():
    """partition_init() -> void
    Regroupe toutes les instructions permettant d'utiliser les différentes fonctions du fichier partition"""

    #Coeur du programme
    for i in range(3):
        plt.plot([1, 100], [1+3*i, 1+3*i], 'k')
        plt.plot([1, 100], [1.5+3*i, 1.5+3*i], 'k')
        plt.plot([1, 100], [2+3*i, 2+3*i], 'k')
        plt.plot([1, 100], [2.5+3*i, 2.5+3*i], 'k')
        plt.plot([1, 100], [3+3*i, 3+3*i], 'k')
        plt.axis([0, 101, 0, 10])
    fenetre_init()

def fenetre_init():
    """fenetre_init() -> void
    Initialise l'interface graphique Tkinter"""

    #Déclaration des variables
    global window
    window = Tk()
    #Coeur du programme
    window.title("Création de partitions")
    window.geometry("480x600")
    window.minsize (480, 600)
    window.config(background='#41B77F')
    framep=Frame(window, bg= '#41B77F')
    frame = Frame (framep, bg='#41B77F')
    frame1=Frame(framep, bg='#41B77F')
    label_title = Label (frame, text="Veuillez choisir la note de musique:")
    label_title.pack()
    label_titleRYTHME = Label (frame1, text="Veuillez choisir la durée de la note:")
    label_titleRYTHME.pack()
    label_subtitle = Label(frame, text= "Les notes sont dans l'orde des octaves")
    label_subtitle.pack()

    La_button = Button(frame, text="La", command=lambda:commande_note(3.5))
    La_button.pack(pady=3, fill=X)
    Sol_button = Button(frame, text="Sol", command=lambda:commande_note(3.25))
    Sol_button.pack(pady=3, fill=X)
    Fa_button = Button(frame, text="Fa", command=lambda:commande_note(3))
    Fa_button.pack(pady=3, fill=X)
    Mi_button = Button(frame, text="Mi", command=lambda:commande_note(2.75))
    Mi_button.pack(pady=3, fill=X)
    Ré_button = Button(frame, text="Ré", command=lambda:commande_note(2.5))
    Ré_button.pack(pady=3, fill=X)
    Do_button = Button(frame, text="Do", command=lambda:commande_note(2.25))
    Do_button.pack(pady=3, fill=X)
    Si_button = Button(frame, text="Si", command=lambda:commande_note(2))
    Si_button.pack(pady=3, fill=X)
    La_button = Button(frame, text="La", command=lambda:commande_note(1.75))
    La_button.pack(pady=3, fill=X)
    Sol_button = Button(frame, text="Sol", command=lambda:commande_note(1.5))
    Sol_button.pack(pady=3, fill=X)
    Fa_button = Button(frame, text="Fa", command=lambda:commande_note(1.25))
    Fa_button.pack(pady=3, fill=X)
    Mi_button = Button(frame, text="Mi", command=lambda:commande_note(1))
    Mi_button.pack(pady=3, fill=X)
    Ré_button = Button(frame, text="Ré", command=lambda:commande_note(0.75))
    Ré_button.pack(pady=3, fill=X)
    Do_button = Button(frame, text="Do", command=lambda:commande_note(0.5))
    Do_button.pack(pady=3, fill=X)

    Ronde_button=Button(frame1, text='Ronde', command=lambda:commande_rythme(8))
    Ronde_button.pack(pady=3, fill=X)
    Blanche_button=Button(frame1, text='Blanche', command=lambda:commande_rythme(4))
    Blanche_button.pack(pady=3, fill=X)
    Noire_button=Button(frame1, text='Noire', command=lambda:commande_rythme(2))
    Noire_button.pack(pady=3, fill=X)
    Croche_button=Button(frame1, text='Croche', command=lambda:commande_rythme(1))
    Croche_button.pack(pady=3, fill=X)
    Valider=Button(frame1, text='Valider', command=placer_note)
    Valider.pack(pady=25)

    Montrer_graphique=Button(frame1, text='Montrer le graphique', command=montrer_le_graphique)
    Montrer_graphique.pack(pady=10)

    framep.pack(expand=YES)
    frame.pack(expand=YES, side=LEFT, padx=5)
    frame1.pack(expand=YES, side=RIGHT, padx=5)
    window.mainloop()

def commande_note(nbr):
    """commande_note(int) -> void
    Définit la valeur de note en fonction du bouton pressé"""

    global note
    note=nbr

def commande_rythme(nbr):
    """commande_rythme(int) -> void
    Définit la valeur de duree en fonction du bouton pressé"""

    global duree
    duree=nbr

def placer_note():
    """placer_note() -> void
    Spécifie la manière dont la note et le rythme sont afficher, puis enregistre ses coordonnée"""

    #Déclaration des variables
    global rythme, ligne
    place=3*(2-ligne)
    if duree==8:
        forme='w'
    if duree==4:
        forme='w'
        plt.plot([rythme+1.7, rythme+1.7], [note+place, note+1+place], 'k')
    if duree==2:
        forme='k'
        plt.plot([rythme+1.7, rythme+1.7], [note+place, note+1+place], 'k')
    if duree==1:
        forme='k'
        plt.plot([rythme+1.7, rythme+1.7], [note+place, note+1+place], 'k')
        plt.plot([rythme+1.7, rythme+2.7], [note+1+place, note+0.5+place], 'k')
    if note==3.5 or note==0.5:
        plt.plot([rythme-2.3, rythme+2.3], [note+place, note+place], 'k')

    plt.plot([rythme], [note+place], 'ko', markerfacecolor=forme, markersize=12)
    rythme+=4+duree/1.5
    if rythme>100:
        rythme=rythme%100
        ligne+=1


def montrer_le_graphique():
    """montrer_le_graphique() -> void
    Détruit la fenêtre Tkinter et affiche la partition sur le graphique"""

    #Coeur du programme
    window.destroy()
    plt.show()
