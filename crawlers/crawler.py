from urllib import request
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import pandas as pd


convocatorias = pd.read_csv('/Users/enriquecarnerofernandez/Documents/BDNS/raw_data/bdns/convocatoriasHeader.csv',
                            header = 1).iloc[:,2:10]
concesiones = pd.read_csv('/Users/enriquecarnerofernandez/Documents/BDNS/raw_data/bdns/juridicasHeader.csv',
                          header = 1).iloc[:,3:16]




def complete_bdns(original_data):
    # Allows the crawler to conect to the web page
    import ssl
    
    # Creating output dataframe and columns
    data = pd.DataFrame(original_data.codigo_bdns)
    
    data['importe_total'] = ''
    data['tipo_beneficiario'] = ''
    data['sector_beneficiario'] = ''
    data['region_impacto'] = ''
    data['finalidad'] = ''
    
    # Counter for progress
    n = 0
    
    for i in data.index:
        
        ssl._create_default_https_context = ssl._create_unverified_context
        
        url = 'https://www.pap.hacienda.gob.es/bdnstrans/GE/es/convocatoria/' + str(data.codigo_bdns[i])
        
        lost = []
        
        try:
           rawpage = request.urlopen(url) # Open the url
        except HTTPError as err:
           if err.code == 404:
               print(data.codigo_bdns[i],
                     " not found")
               
               lost.append(data.codigo_bdns[i])
               
        else:
            #Extract only the article of the page
            contenido = BeautifulSoup(rawpage, "lxml").article
            
            # Assigning values
            importe_total = contenido.find_all('div',attrs = 'bloque')[7]
            if importe_total.find('p') is None:
                data.importe_total[i] = 'NaN'
            else:
                data.importe_total[i] = importe_total.find('p').get_text()
            
            tipo_beneficiario = contenido.find_all('div',attrs = 'bloque')[10]
            if tipo_beneficiario.find('li') is None:
                data.tipo_beneficiario[i] = 'NaN'
            else:
                data.tipo_beneficiario[i] = tipo_beneficiario.find('li').get_text()
                
            sector_beneficiario = contenido.find_all('div',attrs = 'bloque')[11]
            if sector_beneficiario.find('li') is None:
                data.sector_beneficiario[i] = 'NaN'
            else:
                data.sector_beneficiario[i] = sector_beneficiario.find('li').get_text()
            
            region_impacto = contenido.find_all('div',attrs = 'bloque')[12]
            if region_impacto.find('li') is None:
                data.region_impacto[i] = 'NaN'
            else:
                data.region_impacto[i] = region_impacto.find('li').get_text()
            
            finalidad = contenido.find_all('div',attrs = 'bloque')[13]
            if finalidad.find('p') is None:
                data.finalidad[i] = 'NaN'
            else:
                data.finalidad[i] = finalidad.find('p').get_text()

        n += 1
        print(round(n / len(data.index) * 100, 4),'%')
        



complete_bdns(convocatorias)