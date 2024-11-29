"""
génère des notes et les mets dans un tableau
"""
from random import randint


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