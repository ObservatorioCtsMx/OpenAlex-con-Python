import time as tm
import pandas as pd
import pickle
import os

inicio = tm.time()

ruta =  os.getcwd()


def cargar(archivo):
    Lista = []
    with open(archivo, "rb") as file:
                Lista.extend(pickle.load(file))
    return Lista


DF = pd.DataFrame(columns=['FN','VR','PT','AU','AF','BA','BF','CA','GP','BE','TI','SO','SE','BS','LA','DT','CT','CY','CL','SP','HO',
                           'DE','ID','AB','C1','RP','EM','RI','OI','FU','FX','CR','NR','TC','Z9','U1','U2','PU','PI','PA','SN','EI',
                           'BN','J9','JI','PD','PY','VL','IS','SI','PN','SU','MA','BP','EP','AR','DI','D2','EA','EY','PG','P2','WC',
                           'SC','GA','PM','UT','OA','HP','HC','DA','ER','EF','AC','AI','AP'])

nombre = 'Conceto a cargar'

Lista = cargar('PickleCarga/ArchivoFinalLimpio.pkl')

def proceso(j):
    Vector = []
    try: #1
        Vector.append(j['title'])
    except:
        Vector.append('')
    try: #2
        Vector.append(j['version'])
    except:
        Vector.append('')
    try: #3
        Vector.append(j['primary_location']['source']['type'])
    except:
        Vector.append('')
    posicion = []
    id = []
    orcid = []
    nombre = []
    pais = []
    Institucion = []
    Institucion_s_l = []
    for k in j['authorships']:
        posicion.append(k['author_position'])
        try:
            id.append(k['author']['id'])
        except:
            id.append('Sin Id Autor')
        try:
            nombre.append(k['author']['display_name'])
        except:
            nombre.append('Sin Nombre Autor')
        try:
            if k['author']['orcid'] is None:
                orcid.append('Sin Orcid Autor')
            else:
                orcid.append(k['author']['orcid'])
        except:
            orcid.append('Sin Orcid Autor')
        try:
            pais.append("-".join(str(x) for x in k['countries']))
        except:
            pais.append('Sin país')
        Instituciones = []
        try:
            for l in k['institutions']:
                Instituciones.append(l['display_name'])
            Institucion.append("-".join(x for x in Instituciones))
        except:
            Institucion.append('Sin Institucion')
        try:
            Institucion_s_l.append("-".join(k['raw_affiliation_strings']))
        except:
            Institucion_s_l.append("Sin intituciones sin limpiar")
    Vector.append("|".join(nombre))
    try: #5
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #6
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #7
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #8
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #9
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #10
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #11
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #12
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #13
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #14
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #15
        Vector.append(j['language'])
    except:
        Vector.append('')
    try: #16
        Vector.append(j['type'])
    except:
        Vector.append('')
    try: #17
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #18
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #19
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #20
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #21
        Vector.append(j[''])
    except:
        Vector.append('')
    #22 y 23
    Clave = []
    ScoreClave = []
    for k in j['keywords']:
        try:
            Clave.append(k['display_name'])
        except:
            Clave.append('')
        try:
            ScoreClave.append(str(k['score']))
        except:
            ScoreClave.append('')
    Vector.append("|".join(Clave))
    Vector.append("|".join(ScoreClave))
    #24
    try:
        indice = []
        conexion = []
        for clave, valor in j['abstract_inverted_index'].items():
            for x in valor:
                indice.append(x)
                conexion.append(clave)
        Soporte = [x for x  in range(len(indice))]
        for x in range(len(indice)):
            Soporte[indice[x]] = conexion[x]
        Abstract = " ".join(Soporte)
        Vector.append(Abstract)
    except:
        Vector.append('')
    try: #25
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #26
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #27
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #28
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #29
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #30
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #31
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #32
        Vector.append('|'.join(j['referenced_works']))
    except:
        Vector.append('')
    try: #33
        Vector.append(j['referenced_works_count'])
    except:
        Vector.append('')
    try: #34
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #35
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #36 y 37
        citas180 = 0
        citas2013 = 0
        for x in j['counts_by_year']:
            if x['year'] == 2024:
                citas180 += x['cited_by_count']
            if x['year'>2013]:
                citas2013 += x['cited_by_count']
        Vector.append(citas180)
        Vector.append(citas2013)
    except:
        Vector.append('')
        Vector.append('')
    try: #38
        Vector.append(j['primary_location']['source']['display_name'])
    except:
        Vector.append('')
    try: #39
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #40
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #41
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #42
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #43
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #44
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #45
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #46
        Vector.append(j['publication_date'])
    except:
        Vector.append('')
    try: #47
        Vector.append(j['publication_year'])
    except:
        Vector.append('')
    try: #48
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #49
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #50
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #51
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #52
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #53
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #54
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #55
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #56
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #57
        Vector.append(j['ids']['doi'])
    except:
        Vector.append('')
    try: #58
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #59
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #60
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #61
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #62
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #63
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #64
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #65
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #66
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #67
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #68
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #69
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #70
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #71
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #72
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #73
        Vector.append(j[''])
    except:
        Vector.append('')
    try: #74
        Vector.append(pais)
    except:
        Vector.append('')
    try: #75
        Vector.append(Institucion)
    except:
        Vector.append('')
    try: #76
        Vector.append(Institucion_s_l)
    except:
        Vector.append('')
    DF.loc[len(DF)] = Vector

for x in Lista:
    proceso(x)



with open(ruta+r'\PickleCarga\DFArchivoLimpio.pkl', 'wb') as archivo:
        pickle.dump(DF, archivo, protocol=pickle.HIGHEST_PROTOCOL)
        
DF.to_csv(ruta+nombre+'.csv',sep=';')