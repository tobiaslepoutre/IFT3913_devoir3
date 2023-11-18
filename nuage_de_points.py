import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import numpy as np


def etude_relation_variables(chemin_fichier_csv, colonne_x, colonne_y):

    donnees = pd.read_csv(chemin_fichier_csv)

    donnees.columns = donnees.columns.str.strip()

    x = donnees[colonne_x]
    y = donnees[colonne_y]

    # Test de normalité avec Anderson-Darling
    normal_x = st.anderson(x).statistic < st.anderson(x).critical_values[2]  # Niveau de confiance à 95%
    normal_y = st.anderson(y).statistic < st.anderson(y).critical_values[2]  # Niveau de confiance à 95%

    plt.figure(figsize=(10, 4))
    plt.scatter(x, y)

    # Vérifier si les deux données des deux variables sont normalement répartie
    if normal_x and normal_y:
        print("Les deux variables sont normalement répartie")
        # Si les deux variables sont normalement répartie, alors utilise Pearson pour vérifier s'il
        # existe une relation linéaire
        corr, _ = st.pearsonr(x, y)
        # Si le coef de Pearson est proche de 1 ou -1, alors tracer la droite de régression linéaire
        if abs(corr) > 0.6:  # seuil pour affirmer que les deux variables ont une relation linéaire
            m, b = np.polyfit(x, y, 1)
            plt.plot(x, m * x + b, color='green')
            print("Les deux variables ont une relation linéaire, avec un coef de Person de:", corr)
        else:
            # Si le coef de Person est proche de 0, les deux variables n'ont pas une relation linéaire,
            # alors on vérifie si les deux variables ont une relation non liéaire avec le coef de Spearman
            corr, _ = st.spearmanr(x, y)
            # Si le coef de Spearman est proche de 1 ou -1, alors tracer la droite de régression non linéaire
            if abs(corr) > 0.6:  # seuil pour affirmer que les deux variables ont une relation non linéaire
                coefs = np.polyfit(x, y, 2)
                poly_eqn = np.poly1d(coefs)
                plt.plot(np.sort(x), poly_eqn(np.sort(x)), color='green')
    else:
        print("Les deux variables ne sont pas normalement répartie")
        # Si les deux variables ne sont pas normalement répartie, alors on utilise Sperman pour vérifier s'il
        # existe une relation linéaire ou non linéaire
        corrS, _ = st.spearmanr(x, y)
        corrP, _ = st.pearsonr(x, y)

        # Si le coef de Spearman est proche de 1 ou -1 cela signifie qu'il existe une relation entre les deux variables,
        # alors on trace une fonction de régression polynomial de dégré 2, qui pourra s'ajuster aussi bien à une relation
        # linéaire qu'à une relation non linéaire
        if abs(corrS) > 0.6:  # Seuil pour la décision de l'existence d'une relation
            # Afin de connaitre la nature de la relation, on analyse le coef de Person, si
            # lui aussi est proche de 1 ou -1, ceci suggère une relation linéaire, sinon la relation est non linéaire
            if abs(corrP) > abs(corrS):
                m, b = np.polyfit(x, y, 1)
                plt.plot(x, m * x + b, color='green')
                print(f"Les deux variables ont une relation linéaire avec un coefficient de Spearman de: {corrS} et de "
                      f"Pearson de: {corrP}")
            else:
                coefs = np.polyfit(x, y, 2)
                poly_eqn = np.poly1d(coefs)
                plt.plot(np.sort(x), poly_eqn(np.sort(x)), color='green')
                print("Les deux variables ont une relation non linéaire avec un coefficient de Spearman de:", corrS)
        else:
            print("Les deux variables n'ont aucune relation")

    plt.title(f"Nuage de points avec la régression entre {colonne_x} et {colonne_y}")
    plt.xlabel(colonne_x)
    plt.ylabel(colonne_y)

    plt.show()

etude_relation_variables("jfreechart-test-stats.csv", "WMC", "TASSERT")
