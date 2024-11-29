"""
manipule les fichier. Crée/écrire/lire
"""


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
    note_formatee = "".join(f'{note:>6}'for note in notes)
    return f'{prenom:<12}{nom:<12}{note_formatee}\n'


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