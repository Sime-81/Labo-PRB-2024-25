"""
Ce fichier contient un programme pour lire une liste d'élèves,
générer un tableau de notes aléatoires,
et écrire ces données dans un fichier formaté.
"""
from random import randint
from time import sleep

NOM_FICHIER_INPUT = "liste_de_classe.txt"
NOM_FICHIER_OUTPUT = "notes_informatique.txt"
NB_NOTES = 5


def lire_liste_de_classe(nom_fichier):
    """
    lis le fichier donné et retourne une liste de chaque personne sous format [Prenom, Nom]
    :param nom_fichier: Nom du fichier
    :type nom_fichier: str
    :return: liste contenant chaque personne format [Prenom, Nom]
    :rtype: list[list[str, str]]
    """
    liste_de_classe = []
    try :
        with open(nom_fichier, "r", encoding='utf8') as fc:
            for ligne in fc:
                liste_de_classe.append(ligne.split())
    except FileNotFoundError:
        print("Fichier non trouvé")
    finally:
        return liste_de_classe


def generer_notes(nb_notes):
    """
    génère une liste de note compris entre 0 et 20 en fonction du nombre de note désirée
    :param nb_notes: Nombre de note désiré
    :type nb_notes: int
    :return: liste des notes compris entre 0 et 20
    :rtype: list[float]
    """
    liste_note = []
    for note in range(nb_notes):
        note = randint(0, 100)
        note /= 5
        liste_note.append(f"{note:.1f}")
    return liste_note


def generer_tableau_de_notes(liste_de_classes, nb_notes):
    """
    génère un tableau de note en fonction de la liste de classes et le nombre notes
    :param liste_de_classes: la liste de classe
    :type liste_de_classes: list[list[str, str]]
    :param nb_notes: le nombre de notes
    :type nb_notes: int
    :return: retourne le tableau de note en commençant par le prenom et nom de l'élève
    :rtype: list[list[str | int]]
    """
    tableau_de_note = []
    for (prenom, nom) in liste_de_classes:
        tableau_de_note.append([prenom, nom] + generer_notes(nb_notes))
    return tableau_de_note

def formater_ligne_notes(prenom, nom, notes):
    """
    Formate une ligne contenant le prénom, le nom et les notes d'un élève.
    param prenom: Le prénom de l'élève.
    :type prenom: str
    :param nom: Le nom de l'élève.
    :type nom: str
    :param notes: notes de l'élève.
    :type notes: list[float]
    :return: chaîne de caractères formatée contenant le prénom, le nom, et les notes de l'élève
    :rtype: str
    """
    note_formatée = "".join(f'{note:>6}'for note in notes)
    return f'{prenom:<12}{nom:<12}{note_formatée}\n'


def ecrire_fichier_de_notes(nom_fichier, tableau_de_note):
    """
    Écrit un tableau de notes formaté dans un fichier.
    :param nom_fichier: Le nom du fichier
    :type nom_fichier: str
    :param tableau_de_note: contient le prenom, nom et les notes de l'élève
    :type tableau_de_note: list[list[str | int]]
    :return: Indique si l'écriture a été effectuée avec succès.
    :rtype: bool
    :raises IOError: Si le fichier ne peut pas être écrit.
    """
    try:
        with open(nom_fichier, 'w', encoding='utf8') as fc:
            for element in tableau_de_note:
                fc.write(formater_ligne_notes(element[0], element[1], element[2:]))
        return True
    except IOError:
        print("Le fichier n'a pas pu être écrit")
        return False


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