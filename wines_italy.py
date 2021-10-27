import pandas as pd

wines = pd.read_csv('winemag-data-130k-v2.csv')


data_frame = pd.DataFrame(wines)
opc = ['Italy']
italy_wines = data_frame.loc[data_frame['country'].isin(opc)]


print(italy_wines)
