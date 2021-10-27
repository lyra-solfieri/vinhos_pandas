import pandas as pd

wines = pd.read_csv('winemag-data-130k-v2.csv')

data_frame = pd.DataFrame(wines)
opc = ['New Zealand', 'Australia']


oceania_wines = data_frame[(data_frame['points'] > 95) &
                           data_frame['country'].isin(opc)]

# Apenas a Australia tem pontuação maior que 95 entre os dois países
print(oceania_wines.head(100))
