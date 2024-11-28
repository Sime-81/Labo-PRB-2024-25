def interets_composes(capital, duree=10, taux=4.6):
 """
 Calcule la valeur du montant capitalisé sur base des intérêts composés.
 :param capital: montant du capital initial
 :type capital: float
 :param duree: durée de l'emprunt en années
 :type duree: int
 :param taux: taux d'intérêt en pourcents
 :type taux: float
 :return: le montant capitalisé
 :rtype: float
 """
 return round((capital * (1 + taux / 100) ** duree), 2)


if __name__ == '__main__':
    print(interets_composes(10000, 15, 3.2), "€")
    print(interets_composes(10000, taux=3.2), "€")
    print(interets_composes(10000, 15), "€")
    print(interets_composes(10000), "€")