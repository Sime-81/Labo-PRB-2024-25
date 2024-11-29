"""
main script
"""
from time import sleep
from lib.fichiers import *
from lib.note import *

NOM_FICHIER_INPUT = "donnees/liste_de_classe.txt"
NOM_FICHIER_OUTPUT = "donnees/notes_informatique.txt"
NB_NOTES = 5

def afficher_liste_de_classe(liste):
    print("LISTE DES ELEVES")
    print("---------------------------")
    for eleve in range(len(liste)):
        print(f'{eleve+1}. {" ".join(liste[eleve])}')
    print()



def menu(init_ok):
    print("MENU")
    print("---------------------------")
    print("1. Initialiser le fichier de notes")
    if init_ok :
        print("2. Afficher la liste de classe")
    print("9. Quitter")
    print()
    return int(input('Quel est votre choix ? '))


def main():
    """
    fonction main démarre le programme
    :return: rien
    :rtype: None
    """
    running = 0
    init_ok = False
    while running != 9 :
        running = menu(init_ok)
        if running == 1:
            liste_de_classe = lire_liste_de_classe(NOM_FICHIER_INPUT)
            tableau_de_note = generer_tableau_de_notes(liste_de_classe, NB_NOTES)
            ecrire_fichier_de_notes(NOM_FICHIER_OUTPUT, tableau_de_note)
            print(f"Le fichier \"{NOM_FICHIER_OUTPUT}\" a été initialisé.")
            init_ok = True
            sleep(1)
            print()
        if running == 2 and init_ok:
            afficher_liste_de_classe(liste_de_classe)
            sleep(1)



if __name__ == '__main__':
    main()