"""
Module calculant le montant à facturer et le duree_total des prestation de la semaine
"""
TAUX_HORAIRE = 37.50


def prestations_a_facturer(prestations, taux_horaire=TAUX_HORAIRE):
    """
    Cette fonction retourne la durée total et le montant facturé en fonction de la durée en minute et le taux horaire
    :param prestations: durée en minute
    :type prestations: list[int]
    :param taux_horaire: le taux horaire
    :type taux_horaire: float
    :return: la durée total en minute, le montant à facturer
    :rtype: tuple[int, float]
    """
    duree_totale = sum(prestations)
    montant_a_facturer = duree_totale * taux_horaire / 60
    return duree_totale, montant_a_facturer