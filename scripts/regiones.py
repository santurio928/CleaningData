import pandas as pd
import numpy as np

############################# ADMINISTRATIONS LIST ############################

# Import data
ccaa = pd.read_csv('/Users/enriquecarnerofernandez/Documents/BDNS/raw_data/administrations/codccaa.tsv',
                   header = 1, sep = '\t').iloc[:,:2]
provincias = pd.read_csv('/Users/enriquecarnerofernandez/Documents/BDNS/raw_data/administrations/codprov.tsv',
                         header = 1, sep = '\t').iloc[:,:2]
municipios = pd.read_csv('/Users/enriquecarnerofernandez/Documents/BDNS/raw_data/administrations/codmun.tsv',
                         header = 1, sep = '\t')

ccaa
provincias
municipios

# Eliminate commas, reoder compound names
def reorder_names(datos):
    for i in range(len(datos)):
        for n in datos:
            if isinstance(datos[n][i],np.integer):
                continue
            if ',' in datos[n][i]:
                datos[n][i] = datos[n][i].split(',')[1][1:] + ' ' + datos[n][i].split(',')[0]

reorder_names(ccaa)
reorder_names(provincias)
reorder_names(municipios)

# Merge data
listado = pd.merge(pd.merge(municipios,
                            ccaa,
                            left_on = 'CODAUTO',
                            right_on = 'CODIGO',
                            how = 'left'),
                   provincias,
                   left_on = 'CPRO',
                   right_on = 'CODIGO',
                   how = 'left')[['NOMBRE ',
                                  'LITERAL_y',
                                  'LITERAL_x']]

# Rename columns
listado.rename(columns = {'NOMBRE ':'municipio',
                          'LITERAL_y':'provincia',
                          'LITERAL_x':'ccaa'},
               inplace = True)

listado

# Export data
#listado.to_csv('/Users/enriquecarnerofernandez/Documents/BDNS/cured_data/municipios.csv',
#               index = False)

################################## COMARCAS ###################################

# Load data
comarcas = pd.read_csv('/Users/enriquecarnerofernandez/Documents/BDNS/raw_data/administrations/comarcas99_metodologia.tsv',
                       sep = '\t').iloc[:,:3]

# Rename dataframe columns
comarcas.rename(columns = {'FUENTE: Ministerio de Agricultura, Pesca y Alimentación':'provincia',
                           'Unnamed: 1':'comarca',
                           'Unnamed: 2':'municipio'},
                inplace = True)

# Drop numbers in comarca column
for i in range(len(comarcas.comarca)):
    if isinstance(comarcas['comarca'][i],str):
        if comarcas.comarca[i][0] != 'C':
            comarcas.comarca[i] = np.nan
        else:
            comarcas.comarca[i] = comarcas.comarca[i].split(':')[-1][1:]

# Substitue nan values in comarca & provincia column
comarcas['provincia'].fillna(method = 'ffill',
                             inplace = True)
comarcas['comarca'].fillna(method = 'ffill',
                             inplace = True)

# Drop nan values
comarcas = comarcas.dropna().reset_index(drop = True)

# Fix names
for i in range(len(comarcas.municipio)):
    if '(' in str(comarcas.municipio[i]):
        comarcas.municipio[i] = comarcas.municipio[i].split('(')[1][:-1] + ' ' + comarcas.municipio[i].split('(')[0][:-1]

comarcas

# Merge municipios & comarcas dataframes
administraciones = pd.merge(listado,
                            comarcas[['comarca',
                                      'municipio']],
                            on = 'municipio',
                            how = 'left')

administraciones

administraciones.query('provincia == "Alicante/Alacant"')