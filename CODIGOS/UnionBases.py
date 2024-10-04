import time as tm
import pandas as pd
import pickle
import os

inicio = tm.time()

ruta =  os.getcwd()

Conceptos = [r'\c171250308',r'\c57527310',r'\c91129048',r'\c2778402822',r'\c74214498',r'\c155672457',r'\c49326732',r'\c80783014',r'\c51967427',r'\c2776030612',
r'\c2777803738',r'\c126201875',r'\c159951928',r'\c141795571',r'\c2780357685',r'\c41858301',r'\c141400236',r'\c175854130',r'\c85362591',r'\c92880739',
r'\c180238147',r'\c2909374376',r'\c138631740',r'\c45206210',r'\c77066764',r'\c186187911',r'\c140676511',r'\c187911381',r'\c48940184',r'\c27289702',
r'\c46312889',r'\c513720949',r'\c66344492',r'\c175616097',r'\c2910849864',r'\c3231350',r'\c25479853',r'\c31499863',r'\c76110504',r'\c190818770',
r'\c146763847',r'\c204399865',r'\c2777968448',r'\c2778889443',r'\c2780569836',r'\c45083100',r'\c64564810',r'\c177367955',r'\c2776540687',
r'\c2777715892',r'\c16387964',r'\c15083742',r'\c26926545',r'\c33197981',r'\c82432429',r'\c87023908',r'\c129275984',r'\c148402106',r'\c29930090',
r'\c127445965',r'\c2777486477',r'\c21946209',r'\c18150654',r'\c9708629',r'\c108410000',r'\c199529486',r'\c140807948',r'\c128355301',r'\c2777619693',
r'\c133267278',r'\c2779073274',r'\c134424308',r'\c51141536',r'\c2987941056',r'\c85255121',r'\c2986665194',r'\c2778613005',r'\c165983687',r'\c90291627',
r'\c173409883',r'\c173356080',r'\c162117346',r'\c43766710',r'\c154267886',r'\c2780880673',r'\c146427324',r'\c126513998',r'\c165886283',r'\c131872197',
r'\c72045907',r'\c2910607562',r'\c186801447',r'\c2777046567',r'\c58916441',r'\c180936280',r'\c172600038',r'\c32785018',r'\c80086925',r'\c179203168',
r'\c2908926650',r'\c38535076',r'\c54887055',r'\c106597312',r'\c143904697',r'\c2776801781',r'\c2778120352',r'\c71191651',r'\c20608485',r'\c23978448']

def guardar(ext,palabra):
    with open(palabra+'.pkl', 'wb') as archivo:
        pickle.dump(ext, archivo, protocol=pickle.HIGHEST_PROTOCOL)


def cargar(carpeta):
    archivo = []
    for nombre in os.listdir(carpeta):
        if nombre.endswith(".pkl"):
            path = os.path.join(carpeta, nombre)
            with open(path, "rb") as file:
                archivo.extend(pickle.load(file))
    return archivo

os.mkdir(ruta+r'\PickleCarga')
os.chdir(ruta+r'\PickleCarga')

Listaf = []
for x in Conceptos:
    y = cargar(ruta+x)
    guardar(y,x[1:])
    Listaf.extend(y)

guardar(Listaf,"ArchivoFinal")

Listaf = []
for x in Conceptos:
    y = cargar(ruta+x)
    [Listaf.append(j) for j in y if j not in Listaf]

guardar(Listaf,"ArchivoFinalLimpio")


print(tm.time()-inicio)
