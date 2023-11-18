import pandas as pd

file_path = 'downloads/jfreechart-test-stats-1.csv'

data = pd.read_csv(file_path) # lie le fichier
data.columns = data.columns.str.strip()  # retire les blancs inutiles

# Calcul pour les classes de + de 20 assertions
stats_plus_de_20 = data[data['TASSERT'] > 20][['TLOC', 'WMC']].agg(['mean', 'median', 'std'])

# Calcul pour les classes de 20 assertions et moins
stats_20_ou_moins = data[data['TASSERT'] <= 20][['TLOC', 'WMC']].agg(['mean', 'median', 'std'])

stats = {
    'Plus de 20 assertions': stats_plus_de_20,
    '20 assertions ou moins': stats_20_ou_moins
}

print(stats)
