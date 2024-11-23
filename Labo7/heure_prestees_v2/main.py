"""
Module heure prestées.
"""
from calculs.durees import *
from calculs.prestations import *

SEMAINE = ("lundi", "mardi", "mercredi", "jeudi", "vendredi")


def  afficher_resultats(resultats):
    """
    Cette fonction affiche le résultats de la durée de prestation hebdomadaires et le montant à facturer
    :param resultats: contient la durée totale en minutes et le montant à facturer
    :type resultats: tuple[int, float]
    :return: Aucun retour
    :rtype: None
    """
    duree_totale, montant_a_facturer = resultats
    heures, minutes = heures_minutes(duree_totale)
    print()
    print(f"Durée des prestations hebdomadaires : {heures}h et {minutes}min")
    print(f"Montant à facturer : {montant_a_facturer:.2f} €")


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
    afficher_resultats(prestations_a_facturer(duree_prestations))


if __name__ == "__main__":
    main()
