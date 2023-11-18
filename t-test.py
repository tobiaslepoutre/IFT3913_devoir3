import pandas as pd
from scipy import stats

#Lie de fichier
file_path = '/mnt/data/jfreechart-test-stats-1.csv'
data = pd.read_csv(file_path)
data.columns = data.columns.str.strip()  # retire les espaces blanc inutiles

# Trie les valeurs de TLOC et WMC pour les classes de + de 20 assertions
# et celles de 20 ou moins:
tloc_plus_20 = data[data['TASSERT'] > 20]['TLOC']
tloc_20_ou_moins = data[data['TASSERT'] <= 20]['TLOC']
wmc_plus_20 = data[data['TASSERT'] > 20]['WMC']
wmc_20_ou_moins = data[data['TASSERT'] <= 20]['WMC']

# Applique le t-test à TLOC et WMC
t_test_tloc = stats.ttest_ind(tloc_plus_20, tloc_20_ou_moins, equal_var=False)
t_test_wmc = stats.ttest_ind(wmc_plus_20, wmc_20_ou_moins, equal_var=False)

# Affiche les résultats
print("TLOC t-test:", t_test_tloc)
print("WMC t-test:", t_test_wmc)