"""
Module heure prestées.
"""
SEMAINE = ("lundi", "mardi", "mercredi", "jeudi", "vendredi")
TAUX_HORAIRE = 37.50


def lire_heures(duree):
    """
    retourne une durée en type int et prend une duree formatée en ([h]h:mm)
    :param duree: contient la durée avec le formatage ([h]h:mm)
    :type duree: str
    :return: le nombre d'heure
    :rtype: int
    """
    position_deux_points = duree.find(':')
    return int(duree[:position_deux_points])


def lire_minutes(duree):
    """
    retourne une durée en type int prend une durée formatée en ([h]h:mm)
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
    retourne une durée en minute prend une durée formatée en ([h]h:mm)
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
    demande la saisie d'une durée en format ([h]h:mm) et prend le jour de la semaine
    :param nom_jour: jour de la semaine
    :type nom_jour: str
    :return: la durée en format ([h]h:mm)
    :rtype: str
    """
    return input(f"Prestation du {nom_jour:8s} (format [h]h:mm): ")


def prestations_a_facturer(prestations, taux_horaire):
    """
    retourne la durée total et le montant facturé et prend la durée en minute et le taux horaire
    :param prestations: durée en minute
    :type prestations: list[int]
    :param taux_horaire: le taux horaire
    :type taux_horaire: float
    :return: la durée total en minute, le montant à facturer
    :rtype: tuple(int, float)
    """
    duree_totale = sum(prestations)
    montant_a_facturer = duree_totale * taux_horaire / 60
    return duree_totale, montant_a_facturer


def heures_minutes(duree_en_minutes):
    """
    Cette fonction décompose une durée exprimée en minutes en un nombre d’heures et de minutes.
    :param duree_en_minutes: durée totale en minutes
    :type duree_en_minutes: int
    :return: nombre d'heures et de minutes
    :rtype: tuple(int, int)
    """
    heures = duree_en_minutes // 60
    minutes = duree_en_minutes % 60
    return heures, minutes


def main():
    # Programme principal
    print("Facturation des prestations")
    print("---------------------------")
    print()

    # Saisie de la durée des prestations pour chaque jour de la semaine
    duree_prestations = []
    for jour in SEMAINE:
        duree = saisir_duree(jour)
        duree_prestations.append(convertir_en_minutes(duree))

    # Calcul de la durée totale et du montant à facturer
    duree_totale, montant_a_facturer = prestations_a_facturer(duree_prestations, TAUX_HORAIRE)
    heures, minutes = heures_minutes(duree_totale)

    # Affichage des résulats
    print()
    print(f"Durée des prestations hebdomadaires : {heures}h et {minutes}min")
    print(f"Montant à facturer : {montant_a_facturer:.2f} €")


if __name__ == "__main__":
    main()
