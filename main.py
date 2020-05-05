import script_datos
import novedades_datos
import mysql.connector
import sys
from itertools import zip_longest
from urllib.request import urlopen

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
    html_nov= urlopen("http://www.listadomanga.es/novedades.php")
    conn = mysql.connector.connect(host="localhost",port=3306,db="mydb",user="root",password="")
    cursor = conn.cursor()
    children_col = script_datos.html_data()
    col_html = script_datos.html_data_col()
    print("Connection established sucessfully")

    #DATOS NOVEDADES PARA LA BBDD
    novedades = novedades_datos.novedades(html_nov)
    ind2 = 0
    cont = 0
    for i in novedades:
        ind = novedades.index(i)
        if str(i).find("Novedades ") == 0:
            novedades_pal.append(i)
            x = True
            cont = cont + 1
        else:
            for j in novedades_pal:
                
                if x is True:
                    if cont == 1:
                        novedades_commit.append((ind, str(novedades_pal[ind2]) ,str(i)))
                        x = False
                    else:
                        ind2 = ind2 + 1
                        novedades_commit.append((ind, str(novedades_pal[ind2]) ,str(i)))
                        x = False
                        break
                else:
                    novedades_commit.append((ind, str(novedades_pal[ind2]) ,str(i)))
                    break
    cursor.executemany("INSERT INTO `novedades`(`Id.novedad`, `fecha_novedad`, `enlace_portada_novedad`) VALUES (%s,%s,%s)", novedades_commit)
    conn.commit()
    print("Se han añadido los datos correctamente!!!!")
    #DATOS TOMOS PARA LA BBDD

    print("Se han añadido correctamente todas los datos")
    conn.commit()
except mysql.connector.Error as e:
    print("Failed to insert record into MySQL table {}".format(error))
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("MySQL connection is closed")

