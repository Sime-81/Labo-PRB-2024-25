"""
Module de gestion du temps de travail (saisie, conversion des heures et des minutes)
"""
def lire_heures(duree):
    """
    Cette fonction extrait le nombre d'heures à partir d'une durée sous formatage "[h]h:mm"
    :param duree: contient la durée avec le formatage ([h]h:mm)
    :type duree: str
    :return: le nombre d'heure
    :rtype: int
    """
    position_deux_points = duree.find(':')
    return int(duree[:position_deux_points])


def lire_minutes(duree):
    """
    Cette fonction extrait le nombre de minutes à partir d'une durée sous formatage "[h]h:mm"
    :param duree: contient la durée avec le formatage ([h]h:mm)
    :type duree: str
    :return: le nombre de minutes
    :rtype: int
    """
    position_deux_points = duree.find(':')
    # position_deux_points = len(hhmm) - 3  # méthode alternative
    return int(duree[position_deux_points + 1:])


def convertir_en_minutes(hhmm):
    """
    Cette fonction convertie en minutes une durée de format "[h]h:mm"
    :param hhmm: contient la durée avec le formatage ([h]h:mm)
    :type hhmm: str
    :return: la durée en minute
    :rtype: int
    """
    heures = lire_heures(hhmm)
    minutes = lire_minutes(hhmm)
    return heures * 60 + minutes


def saisir_duree(nom_jour):
    """
    Cette fonction réalise la saisie d'une chaîne de caractères au format "[h]h:mm" pour le jour donné
    :param nom_jour: jour de la semaine
    :type nom_jour: str
    :return: la durée en format ([h]h:mm)
    :rtype: str
    """
    return input(f"Prestation du {nom_jour:8s} (format [h]h:mm): ")


def heures_minutes(duree_en_minutes):
    """
    Cette fonction décompose une durée exprimée en minutes en un nombre d’heures et de minutes.
    :param duree_en_minutes: durée totale en minutes
    :type duree_en_minutes: int
    :return: nombre d'heures et de minutes
    :rtype: tuple[int, int]
    """
    heures = duree_en_minutes // 60
    minutes = duree_en_minutes % 60
    return heures, minutes