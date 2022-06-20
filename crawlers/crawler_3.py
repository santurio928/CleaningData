#Import libraries
from urllib import request
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import pandas as pd
import numpy as np

# Allows the crawler to conect to the web page
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


convocatoriasI = pd.DataFrame()
codigoBDSN = 500000

for i in np.arange(1000):
    
    url = "https://www.pap.hacienda.gob.es/bdnstrans/GE/es/convocatoria/" + str(codigoBDSN)

    # Making the request
    try:
       RawPage = request.urlopen(url) # Open the url
    except HTTPError as err:
       if err.code == 404:
           print(codigoBDSN, " not found")
    else:
        print(codigoBDSN, " found")
        
        status = RawPage.code # Checking the access
        #print(status) # It must be 200 


        #if (200 == status):
        # Parsing to html
        SoupedPage = BeautifulSoup(RawPage, "html5lib")

        #Extract only the article of the page
        Contenido = SoupedPage.article

    
        organo2 = Contenido.find_all("h3")[0].get_text() + " 2"; organo2
        a = ["NaN"]*30
        li = a[:5]
        p = a[:30]
        for i in np.arange(len(Contenido.find_all("p"))):
            p[i] = Contenido.find_all("p")[i].get_text()

        for i in np.arange(len(Contenido.find_all("li"))):
            li[i] = Contenido.find_all("li")[i].get_text()
        conv = {
                Contenido.find_all("h3")[0].get_text() : p[0],
                organo2 : p[1],
                Contenido.find_all("h3")[1].get_text() : p[3],
                Contenido.find_all("h3")[2].get_text() : p[4],
                Contenido.find_all("h3")[3].get_text() : p[5],
                Contenido.find_all("h3")[4].get_text() : p[6],
                Contenido.find_all("h3")[5].get_text() : li[0],
                Contenido.find_all("h3")[6].get_text() : p[7],
                Contenido.find_all("h3")[7].get_text() : p[8],
                Contenido.find_all("h3")[8].get_text() : p[9],
                Contenido.find_all("h3")[9].get_text() : p[10],
                Contenido.find_all("h3")[10].get_text() : li[1],
                Contenido.find_all("h3")[11].get_text() : li[2],
                Contenido.find_all("h3")[12].get_text() : li[3],
                Contenido.find_all("h3")[13].get_text() : p[11],
                Contenido.find_all("h3")[14].get_text() : p[12],
                Contenido.find_all("h3")[15].get_text() : p[13],
                Contenido.find_all("h3")[16].get_text() : p[14],
                Contenido.find_all("h3")[17].get_text() : p[15],
                Contenido.find_all("h3")[18].get_text() : p[18],
                Contenido.find_all("h3")[19].get_text() : p[20],
                }
        convocatoriasI = convocatoriasI.append(conv, ignore_index=True)
    codigoBDSN += 1
convocatoriasI
codigoBDSN 