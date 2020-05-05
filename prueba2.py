#-*- coding: utf-8 -*
import script_datos
import socket
import novedades_datos
import mysql.connector
import sys
from itertools import zip_longest
from urllib.request import urlopen
import csv
import urllib

titulos1 = []
sinopsis1 = []
tit_org1 = []
dibujantes1 = []
guion1 = []
ed_franc1 = []
ed_amer1 = []
ed_jap1 = []
ed_esp1 = []
genero1 = []
formato1 = []
sent_lect1 = []
tomos_jap1 = []
tomos_esp1 = []
titulo_per_obra1 = []
titulo_per_obra2 =[]
numero_tomo1 = []
num_paginas1 = []
precios_tomos1 = []
enl_portadas1 = []
novedades = []
novedades_pal = []
novedades_commit = []


def aslist(generator):
    "Function decorator to transform a generator into a list"
    def wrapper(*args, **kwargs):
        return list(generator(*args, **kwargs))
    return wrapper


try:
    conn = mysql.connector.connect(host="localhost",port=3306,db="manga",user="root",password="")
    cursor = conn.cursor()
    children_col = script_datos.html_data()
    col_html = script_datos.html_data_col()
    
    '''titulo_obra_per_tomo = script_datos.titulo_obra_per_tomo()
    titulos = list(str(i) for i in titulo_obra_per_tomo)
    print(len(titulos))
    numero_tomo = script_datos.numero_tomos(col_html)
    numeros = list(str(i) for i in numero_tomo)
    print(len(numeros))
    #num_paginas = script_datos.numero_paginas(col_html)'''
    '''print(len(script_datos.list_numero_paginas()))
    #precios = script_datos.list_precios_tomos()
    print(len(script_datos.list_precios_tomos()))
    #enlaces = script_datos.list_portadas_tomos()
    print(len(script_datos.list_portadas_tomos()))'''

    #res = []
    #res_tomos = [(i,str(j),k,str(l),str(m)) for i in script_datos.list_titulo_obra_per_tomo() for j in script_datos.list_portadas_tomos() for k in script_datos.list_numero_tomos() for l in script_datos.list_numero_paginas() for m in script_datos.list_precios_tomos()]


    '''for m,l,i,j,k in zip(titulo_obra_per_tomo,enl_portadas,numero_tomo,num_paginas,precios_tomos):
        #res_tomos.append((str(m),str(l),str(i),str(j),str(k)))
        print(i)'''
    
    #res_tomos = [(titulo_per_obra1[i],enl_portadas1[i],numero_tomo1[i],num_paginas1[i],precios_tomos1[i]) for i in range(0,len(titulo_per_obra1))]
    #res_tomos = [()]

    #print(script_datos.res_tomos())
    #cursor.executemany("INSERT INTO `tomos`(`coleccion`, `enlace_portada_tomo`, `tomo`, `paginas_tomo`, `precio_tomo`) VALUES (%s,%s,%s,%s,%s)", script_datos.res_tomos())
    #conn.commit()
    #print("Se han añadido los datos correctamente")

except mysql.connector.Error as e:
    print("Failed to insert record into MySQL table {}".format(error))
except IncompleteRead:
    pass
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("MySQL connection is closed")