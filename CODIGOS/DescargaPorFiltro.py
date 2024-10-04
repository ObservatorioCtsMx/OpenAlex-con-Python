import requests as rq
import time as tm
import pickle
import os

ruta =  os.getcwd()

inicio = tm.time()

iniciocadena = 'https://api.openalex.org/works?per-page=200&cursor='
fincadena = ',authorships.countries:BR|MX|AR|CO|CL|PE|EC|VE|CR|BO|PR|CU|PA|NI|UY|DO|PY|SV|GT|HT|HN|JM|BS|VI|BB|LC|GY|CW|KY|SR|BZ|GF|GP|KN|DM|GD|AG|VC|MS|SX|TC|AW|FK|MQ|VG'
filtro = ['abstract.search:','default.search:','fulltext.search:','keyword.search:','semantic.search:','title.search:','concepts.id:','title_and_abstract.search:']


def respuesta(palabra,nc,numero):
    res = rq.get(iniciocadena+nc+'&filter='+filtro[numero]+palabra+fincadena)
    print(res.status_code)
    return res.json()['meta'],res.json()['results']


def guardar(ext,clave,numero,palabra):
    with open(clave+filtro[numero].replace(".","_").replace(":","_")+palabra+'cursor'+'.pkl', 'wb') as archivo:
        pickle.dump(ext, archivo, protocol=pickle.HIGHEST_PROTOCOL)

Conceptos = ['nano']

    

for x in Conceptos:
    os.chdir(ruta)
    os.mkdir(x)
    meta = {'next_cursor' : '*'}
    os.chdir(ruta+'\\'+x)
    j=0
    while(meta['next_cursor']!=None):
        j+=1
        meta,resultados = respuesta(x,meta['next_cursor'],7)
        guardar(resultados,'_'+str(j)+'_',7,x)
