import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def creer_boite_a_moustache(chemin_fichier_csv, nom_colonne):

    donnees = pd.read_csv(chemin_fichier_csv)

    donnees.columns = donnees.columns.str.strip()

    colonne = donnees[nom_colonne].dropna()

    flierprops = dict(marker='x', markersize=10)

    plt.figure(figsize=(10, 2))
    plt.boxplot(colonne, vert=False, patch_artist=True, flierprops=flierprops)

    plt.xlabel("Valeurs")
    plt.yticks([1], [nom_colonne])

    plt.show()

    moyenne = colonne.mean()
    mediane = colonne.median()
    quartiles = np.percentile(colonne, [25, 75])
    longueur_boite = quartiles[1] - quartiles[0]
    limite_sup = quartiles[1] + 1.5 * longueur_boite

    print("Moyenne:", moyenne)
    print("Mediane:", mediane)
    print("Premier quartile:", quartiles[0])
    print("Troisième quartile:", quartiles[1])
    print("Longueur boîte:", longueur_boite)
    print("Limite supérieur:", limite_sup)

creer_boite_a_moustache("jfreechart-test-stats.csv", "TASSERT")
