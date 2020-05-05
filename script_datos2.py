#!/usr/bin/python
# -*- coding: utf-8 -*-
from urllib.request import urlopen
import urllib
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from collections import OrderedDict
import re
import time
from functools import wraps
from http.client import IncompleteRead
import csv
import script_datos


enlaces= []
children_col = []
titulos = []
titulos_col= []
titulos_obras = []

etiquetas_manga = []
descripcion = []


def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

try:
    def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
    
        def deco_retry(f):

            @wraps(f)
            def f_retry(*args, **kwargs):
                mtries, mdelay = tries, delay
                while mtries > 1:
                    try:
                        return f(*args, **kwargs)
                    except ExceptionToCheck as e:
                        msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                        if logger:
                            logger.warning(msg)
                        else:
                            print(msg)
                        time.sleep(mdelay)
                        mtries -= 1
                        mdelay *= backoff
                return f(*args, **kwargs)

            return f_retry  # true decorator

        return deco_retry

    @retry(URLError, tries=4, delay=3, backoff=2)
    def urlopen_with_retry(req):
        return urlopen(req)
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")

else:
    def html_data():
        res2 = []
        req = urllib.request.Request('http://www.listadomanga.es/lista.php', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
        res = BeautifulSoup(urlopen_with_retry(req).read(), "html.parser")
        children = res.findAll("td",{"class":"izq"})
        enlaces=[]
        for child in children:
            res = child.find_all("a")
            for res1 in res:
                res1.attrs['href'] = "http://www.listadomanga.es/" + res1.attrs['href']
                enlaces.append(res1.attrs['href'])
    
        for i in enlaces:
            col_html = BeautifulSoup(urlopen_with_retry(i).read(),"html.parser")
            res2 = col_html.findAll("td",{"class":"izq"})
            for j in res2:
                yield j
    
    res = html_data()
    def html_data_col():  
        res2 = []
        req = urllib.request.Request('http://www.listadomanga.es/lista.php', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
        res = BeautifulSoup(urlopen_with_retry(req).read(), "html.parser")
        children = res.findAll("td",{"class":"izq"})
        enlaces=[]
        for child in children:
            res = child.find_all("a")
            for res1 in res:
                res1.attrs['href'] = "http://www.listadomanga.es/" + res1.attrs['href']
                enlaces.append(res1.attrs['href'])
    
        for i in enlaces:
            req2 = urllib.request.Request(i, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
            col_html = BeautifulSoup(urlopen_with_retry(req2).read(),"html.parser")
            res2 = col_html.find_all("td",{"class":"cen"})
            for j in res2:
                yield j

    res2 = html_data_col()
    def titulo_obra_per_tomo():
            req = urllib.request.Request('http://www.listadomanga.es/lista.php', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
            res = BeautifulSoup(urlopen_with_retry(req).read(), "html.parser")
            children = res.findAll("td",{"class":"izq"})
            for child in children:
                res = child.find_all("a")
                for res1 in res:
                    res1.attrs['href'] = "http://www.listadomanga.es/" + res1.attrs['href']
                    enlaces.append(res1.attrs['href'])
                    titulos.append(res1.string)
            for i in range(len(enlaces)):
                req2 = urllib.request.Request(str(enlaces[i]), headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
                col_html = BeautifulSoup(urlopen_with_retry(req2).read(), "html.parser")
                children_col = col_html.findAll("td",{"class":"izq"})
                for child_col in children_col:
                    for titulo_col in child_col.find_all("h2"):
                        if titulo_col.string.capitalize().find("Sinopsis") != -1 or titulo_col.string.capitalize().find("Cofre") != -1 or titulo_col.string.capitalize().find("Regalo") != -1 or titulo_col.string.capitalize().find("Números") != -1 or titulo_col.string.capitalize().find("Ficha") != -1 or titulo_col.string.capitalize().find("Carta") != -1 or titulo_col.string.capitalize().find("Preview") != -1 or titulo_col.string.capitalize().find("Promo") != -1 or titulo_col.string.capitalize().find("Ilustración") != -1 or titulo_col.string.capitalize().find("Títulos") != -1 or titulo_col.string.capitalize().find("Otras ediciones") != -1:
                            pass
                        else:
                            titulos_obras.append(titulo_col.string)
                            #yield titulos_obras[-1]
                for datos_tomos in col_html.find_all("td",{"class":"cen"}):
                    yield titulos_obras[-1]
    
    def txt_titulos():
        outputFile = open("output_titulos.txt","w",encoding="utf-8")
        for i in titulo_obra_per_tomo():
            string = str(i)
            outputFile.write(string + "\n")
        outputFile.close()
    
    #txt_titulos()

    def list_titulo_obra_per_tomo():
        lista = []
        for i in titulo_obra_per_tomo():
            lista.append(i)
        print("Longitud titulos: " + str(len(lista)))
        return lista
    
    

    def numero_tomos(col_html):
        num_tomos = []
        for datos_tomos in col_html:
            html_datos = str(datos_tomos)
            #div_pos = html_datos.find("<br")
            split_datos = html_datos.split("<br/>")
            str1 = ' '.join(s for s in split_datos)
            str1 = "".join(str1.splitlines())
            #u = datos_tomos.get_text()
            #print(html_datos)
            u = BeautifulSoup(str1,"html.parser").get_text()
            w = u.find(" página")
            n = u.find("nº")
            inicio = 0
            pesetas = u.find("Ptas.")
            pag_bn = u.find("B/N")
            pag_color = u.find("color")
            euros = u.find(" €")
            resta_ind = w - n
            #print(u)
            if n != -1:
                if w != -1:
                    if pesetas == -1 and euros != -1:
                        if resta_ind == 6:
                            num_tomos.append(u[0:n+3])
                        elif resta_ind == 7:
                            num_tomos.append(u[0:n+4])
                else:
                    num_tomos.append(u[0:len(u)])
            else:
                if w != -1:
                    if pesetas == -1 and euros != -1:
                        num_tomos.append(u[0:w-3])
                else:
                    num_tomos.append("")
            lista_nueva = []
            lista_nueva2 = []
            lista_nueva.append(num_tomos[-1])
            lista_nueva2 = f7(lista_nueva)
            for i in lista_nueva2:
                yield i
    for i in script_datos.numero_tomos(res2):
        print(i)

    def txt_numeros():
        outputFile = open("output_numeros.txt","w",encoding="utf-8")
        for i in numero_tomos(res2):
            string = str(i)
            outputFile.write(string + "\n")
        outputFile.close()
    
    #txt_numeros()
    
    def list_numero_tomos():
        lista = []
        for i in numero_tomos(res2):
            lista.append(i)
        print("Longitud numeros: " + str(len(lista)))
        return lista
    


    def numero_paginas(col_html):
        num_paginas = []
        for datos_tomos in col_html:
            u = datos_tomos.get_text()
            w = u.find(" página")
            n = u.find("nº")
            inicio = 0
            pesetas = u.find("Ptas.")
            pag_bn = u.find("B/N")
            pag_color = u.find("color")
            euros = u.find(" €")
            resta_ind = w - n
            if n != -1:
                if w != -1:
                    if pesetas == -1 and euros != -1:
                        if resta_ind == 6:
                            if pag_bn != -1 and pag_color != -1 or pag_color != -1:
                                num_paginas.append(u[n+3:pag_color+5])
                            elif pag_bn != -1:
                                num_paginas.append(u[n+3:pag_bn+3])
                        elif resta_ind == 7:
                            if pag_bn != -1 and pag_color != -1 or pag_color != -1:
                                num_paginas.append(u[n+4:pag_color+5])
                            elif pag_bn != -1:
                                num_paginas.append(u[n+4:pag_bn+3])
                else:
                    num_paginas.append("")
            else:
                if w != -1:
                    if pesetas == -1 and euros != -1:
                        if pag_bn != -1 and pag_color != -1 or pag_color != -1:
                            num_paginas.append(u[w-3:pag_color+5])
                        elif pag_bn != -1:
                            num_paginas.append(u[w-3:pag_bn+3])
                else:
                    num_paginas.append("")
            yield num_paginas[-1]
    
    def list_numero_paginas():
        lista = []
        for i in numero_paginas(res2):
            lista.append(i)
        print("Longitud paginas: " + str(len(lista)))
        return lista

    
    def precios_tomos(col_html):
        precio_tomos = []
        for datos_tomos in col_html:
            u = datos_tomos.get_text()
            w = u.find(" página")
            n = u.find("nº")
            inicio = 0
            pesetas = u.find("Ptas.")
            pag_bn = u.find("B/N")
            pag_color = u.find("color")
            euros = u.find(" €")
            resta_ind = w - n
            #print(u)
            if n != -1:
                if w != -1:
                    if pesetas == -1 and euros != -1:
                        if resta_ind == 6:
                            if pag_bn != -1 and pag_color != -1 or pag_color != -1:
                                precio_tomos.append(u[pag_color+5:euros+1])
                            elif pag_bn != -1:
                                precio_tomos.append(u[pag_bn+3:euros+1])
                        elif resta_ind == 7:
                            if pag_bn != -1 and pag_color != -1 or pag_color != -1:
                                precio_tomos.append(u[pag_color+5:euros+1])
                            elif pag_bn != -1:
                                precio_tomos.append(u[pag_bn+3:euros+1])
                    elif pesetas != -1 and euros == -1:
                        precio_tomos.append("")
            else:
                if w != -1:
                    if pesetas == -1 and euros != -1:
                        if pag_bn != -1 and pag_color != -1 or pag_color != -1:
                            precio_tomos.append(u[pag_color+5:euros+1])
                        elif pag_bn != -1:
                            precio_tomos.append(u[pag_bn+3:euros+1])
                    elif pesetas != -1 and euros == -1:
                        precio_tomos.append("")
                else:
                    precio_tomos.append("")
            yield precio_tomos[-1]
    
    def list_precios_tomos():
        lista = []
        for i in precios_tomos(res2):
            lista.append(i)
        print("Longitud precios: " + str(len(lista)))
        return lista
    def portadas_tomos(col_html):
        imgs_tomos = []
        for datos_tomos in col_html:
            for img_nov in datos_tomos.find_all("img"):
                img_nov['src'] = "http://www.listadomanga.es/" + img_nov['src']
                imgs_tomos.append(img_nov['src'])
            yield imgs_tomos[-1]
    
    def list_portadas_tomos():
        lista = []
        for i in portadas_tomos(res2):
            lista.append(i)
        print("Longitud portadas: " + str(len(lista)))
        return lista

    def res_datos():
        res_datos = []
        res_datos2 = []
        res_datos.append(list_titulo_obra_per_tomo(),list_portadas_tomos(),list_numero_tomos(),list_numero_tomos(),list_precios_tomos())
        for i in range(len(res_datos[0])):
            for j in range(len(res_datos)):
                print(res_datos[j][i], end="")
                res_datos2.append(res_datos[j][i])
    



