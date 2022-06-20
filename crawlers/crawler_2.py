#Import libraries
from urllib import request
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import pandas as pd
import numpy as np


# Allows the crawler to conect to the web page HANDSHAKE
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Web page
url = "https://www.pap.hacienda.gob.es/bdnstrans/GE/es/convocatoria/570125"

# Making the request
RawPage = request.urlopen(url) # Open the url
status = RawPage.code # Checking the access
print(status) # It must be 200 


#if (200 == status):
# Parsing to html
SoupedPage = BeautifulSoup(RawPage, "html5lib")

#Extract only the article of the page
Contenido = SoupedPage.article


    
for i in np.arange(20):
    print("# h3",i," ",Contenido.find_all("h3")[i].get_text())

for i in np.arange(len(Contenido.find_all("p"))):
    print("## p",i," ",Contenido.find_all("p")[i].get_text())
   
for i in np.arange(len(Contenido.find_all("li"))):
    print("## li",i," ",Contenido.find_all("li")[i].get_text())


# h3 0   Órgano convocante
## p 0   LA RIOJA
## p 1   CONSEJERÍA DE AGRICULTURA, GANADERÍA, MUNDO RURAL, TERRITORIO Y POBLACIÓN
# h3 1   Sede electrónica para la presentación de solicitudes
## p 3   https://www.larioja.org/oficina-electronica/es
# h3 2   Código BDNS
## p 4   570125
# h3 3   Mecanismo de Recuperación y Resiliencia
## p 5   NO
# h3 4   Fecha de registro
## p 6   15/06/2021
# h3 5   Instrumento de ayuda
## li 0   SUBVENCIÓN Y ENTREGA DINERARIA SIN CONTRAPRESTACIÓN 
# h3 6   Tipo de convocatoria
## p 7   Concurrencia competitiva - canónica
# h3 7   Presupuesto total de la convocatoria
## p 8   11,704.10 €
# h3 8   Título de la convocatoria en español
## p 9   Beca de formación de personal en materia de desarrollo rural y reto demográfico.
# h3 9   Título de la convocatoria en otra lengua cooficial
## p 10   .
# h3 10   Tipo de beneficiario elegible
## li 1   PERSONAS FÍSICAS QUE NO DESARROLLAN ACTIVIDAD ECONÓMICA
# h3 11   Sector económico del beneficiario
## li 2   Investigación y desarrollo
# h3 12   Región de impacto
## li 3   ES230 - La Rioja
# h3 13   Finalidad (política de gasto)
## p 11   INVESTIGACIÓN, DESARROLLO E INNOVACIÓN
# h3 14   Título de las Bases reguladoras
## p 12  
# h3 15   Dirección electrónica de las bases reguladoras
## p 13
# h3 16   ¿El extracto de la convocatoria se publica en diario oficial?
## p 14 
# h3 17   ¿Se puede solicitar indefinidamente?
## p 15 
# h3 18   Fecha de inicio del periodo de solicitud
## p 18
# h3 19   Fecha de finalización del periodo de solicitud
## p 20 

Contenido.find_all("h3")[0].get_text()

Contenido.find_all("h3")[0].get_text()

lis = []

convocatoriasI = pd.DataFrame()
organo2 = Contenido.find_all("h3")[0].get_text() + " 2"; organo2
conv = {
        Contenido.find_all("h3")[0].get_text() : Contenido.find_all("p")[0].get_text(),
        organo2 : Contenido.find_all("p")[1].get_text(),
        Contenido.find_all("h3")[1].get_text() : Contenido.find_all("p")[3].get_text(),
        Contenido.find_all("h3")[2].get_text() : Contenido.find_all("p")[4].get_text(),
        Contenido.find_all("h3")[3].get_text() : Contenido.find_all("p")[5].get_text(),
        Contenido.find_all("h3")[4].get_text() : Contenido.find_all("p")[6].get_text(),
        Contenido.find_all("h3")[5].get_text() : Contenido.find_all("li")[0].get_text(),
        Contenido.find_all("h3")[6].get_text() : Contenido.find_all("p")[7].get_text(),
        Contenido.find_all("h3")[7].get_text() : Contenido.find_all("p")[8].get_text(),
        Contenido.find_all("h3")[8].get_text() : Contenido.find_all("p")[9].get_text(),
        Contenido.find_all("h3")[9].get_text() : Contenido.find_all("p")[10].get_text(),
        Contenido.find_all("h3")[10].get_text() : Contenido.find_all("li")[1].get_text(),
        Contenido.find_all("h3")[11].get_text() : Contenido.find_all("li")[2].get_text(),
        Contenido.find_all("h3")[12].get_text() : Contenido.find_all("li")[3].get_text(),
        Contenido.find_all("h3")[13].get_text() : Contenido.find_all("p")[11].get_text(),
        Contenido.find_all("h3")[14].get_text() : Contenido.find_all("p")[12].get_text(),
        Contenido.find_all("h3")[15].get_text() : Contenido.find_all("p")[13].get_text(),
        Contenido.find_all("h3")[16].get_text() : Contenido.find_all("p")[14].get_text(),
        Contenido.find_all("h3")[17].get_text() : Contenido.find_all("p")[15].get_text(),
        Contenido.find_all("h3")[18].get_text() : Contenido.find_all("p")[18].get_text(),
        Contenido.find_all("h3")[19].get_text() : Contenido.find_all("p")[20].get_text(),
        }
convocatoriasI = convocatoriasI.append(conv, ignore_index=True)
convocatoriasI
conv



url = "https://www.pap.hacienda.gob.es/bdnstrans/GE/es/convocatoria/" + str(500296)


    
try:
   RawPage = request.urlopen(url)
except HTTPError as err:
   if err.code == 404:
       print("500046 not found")
else:
    print("yes")


a = np.arange(20)
a[:] = "NaN";a
li = a[:5];li
p = a[:30];p
a = ["NaN"]*30
a[0] = "Cerp"
for i in np.arange(len(Contenido.find_all("p"))):
    p[i] = Contenido.find_all("p")[i].get_text()

for i in np.arange(len(Contenido.find_all("li"))):
    li[i] = Contenido.find_all("li")[i].get_text()
    
convocatoriasI = pd.DataFrame()
organo2 = Contenido.find_all("h3")[0].get_text() + " 2"; organo2
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
convocatoriasI



conv = {
        Contenido.find_all("h3")[0].get_text() : Contenido.find_all("p")[0].get_text(), # h3 0   Órgano convocante
        organo2 : Contenido.find_all("p")[1].get_text(),
        Contenido.find_all("h3")[1].get_text() : Contenido.find_all("p")[3].get_text(), # h3 1   Sede electrónica para la presentación de solicitudes
        Contenido.find_all("h3")[2].get_text() : Contenido.find_all("p")[4].get_text(), # h3 2   Código BDNS
        Contenido.find_all("h3")[3].get_text() : Contenido.find_all("p")[5].get_text(), # h3 3   Mecanismo de Recuperación y Resiliencia
        Contenido.find_all("h3")[4].get_text() : Contenido.find_all("p")[6].get_text(), # h3 4   Fecha de registro
        Contenido.find_all("h3")[5].get_text() : Contenido.find_all("li")[0].get_text(), # h3 5   Instrumento de ayuda
        Contenido.find_all("h3")[6].get_text() : Contenido.find_all("p")[7].get_text(), # h3 6   Tipo de convocatoria
        Contenido.find_all("h3")[7].get_text() : Contenido.find_all("p")[8].get_text(), # h3 7   Presupuesto total de la convocatoria
        Contenido.find_all("h3")[8].get_text() : Contenido.find_all("p")[9].get_text(), # h3 8   Título de la convocatoria en español
        # Contenido.find_all("h3")[9].get_text() : Contenido.find_all("p")[10].get_text(), # h3 9   Título de la convocatoria en otra lengua cooficial
        Contenido.find_all("h3")[10].get_text() : Contenido.find_all("li")[1].get_text(), # h3 10   Tipo de beneficiario elegible
        Contenido.find_all("h3")[11].get_text() : Contenido.find_all("li")[2].get_text(), # h3 11   Sector económico del beneficiario
        Contenido.find_all("h3")[12].get_text() : Contenido.find_all("li")[3].get_text(), # h3 12   Región de impacto
        Contenido.find_all("h3")[13].get_text() : Contenido.find_all("p")[11].get_text(), # h3 13   Finalidad (política de gasto)
        Contenido.find_all("h3")[14].get_text() : Contenido.find_all("p")[12].get_text(), # h3 14   Título de las Bases reguladoras
        # Contenido.find_all("h3")[15].get_text() : Contenido.find_all("p")[13].get_text(), # h3 15   Dirección electrónica de las bases reguladoras
        # Contenido.find_all("h3")[16].get_text() : Contenido.find_all("p")[14].get_text(), # h3 16   ¿El extracto de la convocatoria se publica en diario oficial?
        # Contenido.find_all("h3")[17].get_text() : Contenido.find_all("p")[15].get_text(), # h3 17   ¿Se puede solicitar indefinidamente?
        # Contenido.find_all("h3")[18].get_text() : Contenido.find_all("p")[18].get_text(), # h3 18   Fecha de inicio del periodo de solicitud
        # Contenido.find_all("h3")[19].get_text() : Contenido.find_all("p")[20].get_text(), # h3 19   Fecha de finalización del periodo de solicitud
        }