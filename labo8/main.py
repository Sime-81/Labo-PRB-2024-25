"""
main script
"""
from time import sleep
from lib.fichiers import *
from lib.note import *

NOM_FICHIER_INPUT = "donnees/liste_de_classe.txt"
NOM_FICHIER_OUTPUT = "donnees/notes_informatique.txt"
NB_NOTES = 5


def main():
    """
    fonction main démarre le programme
    :return: rien
    :rtype: None
    """
    print("Lecture de la liste de classe")
    liste_de_classe = lire_liste_de_classe(NOM_FICHIER_INPUT)
    sleep(0.5)
    print("Génération du tableau de notes")
    tableau_de_note = generer_tableau_de_notes(liste_de_classe, NB_NOTES)
    sleep(0.5)
    print("Création du fichier 'notes_informatique.txt")
    ecrire_fichier_de_notes(NOM_FICHIER_OUTPUT, tableau_de_note)
    sleep(0.5)
    print("Fin du programme !")


if __name__ == '__main__':
    main()