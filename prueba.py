# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from collections import OrderedDict
import re

enlaces= []
titulos = []
titulos_col= []
titulos_obras=[]
etiquetas_manga = []
descripcion = []
guion = []
dibujo = []
ed_americana = []
ed_francesa = []
ed_japonesa = []
ed_española = []
generos = []
formatos = []
sentido_lectura = []
num_japones = []
num_español = []
num_tomos = []
num_paginas = []
precio_tomos = []
imgs_tomos = []
k = []
lista_nueva2 = []

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

try:
    html= urlopen("http://www.listadomanga.es/lista.php")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    
        
    res = BeautifulSoup(html.read(), "html.parser")
    children = res.findAll("td",{"class":"izq"})
    for child in children:
        res = child.find_all("a")
        for res1 in res:
            res1.attrs['href'] = "http://www.listadomanga.es/" + res1.attrs['href']
            enlaces.append(res1.attrs['href'])
            titulos.append(res1.string)
    for i in range(len(enlaces)):
        html2 = urlopen(enlaces[i])
        col_html = BeautifulSoup(html2.read(),"html.parser")
        children_col = col_html.findAll("td",{"class":"izq"})
        for child_col in children_col:
            #titulo_col = child_col.find_all("h2")
            #resto_titulos_col = child_col.find_all("b")
            enlaces_valor_col = child_col.find_all("a")
        
            for titulo_col in child_col.find_all("h2"):
                if titulo_col.string.capitalize().find("Sinopsis") != -1 or titulo_col.string.capitalize().find("Cofre") != -1 or titulo_col.string.capitalize().find("Regalo") != -1 or titulo_col.string.capitalize().find("Números") != -1 or titulo_col.string.capitalize().find("Ficha") != -1 or titulo_col.string.capitalize().find("Carta") != -1 or titulo_col.string.capitalize().find("Preview") != -1 or titulo_col.string.capitalize().find("Promo") != -1 or titulo_col.string.capitalize().find("Ilustración") != -1 or titulo_col.string.capitalize().find("Títulos") != -1 or titulo_col.string.capitalize().find("Otras ediciones") != -1:
                    pass
                else:
                    titulos_obras.append(titulo_col.string)
                    #print(titulos_obras[-1])
            x = child_col.get_text()
            j = x.split("\n")
            
            for campo in j:
                ind = j.index(campo)
                if campo.find("Otras ediciones de ") == 0 or campo.find("Números editados") == 0 or campo.find("Números no editados") == 0 or campo.find("Números en preparación")==0:
                    j.pop(ind)
            #print(j)
            for campo in j: 
                ind = j.index(campo)
                #print("El campo es:" + campo + " y su INDICE es el siguiente:" + str(ind))
                if ind==0 or ind%5 == 0:
                    sinopsis=campo
                    if sinopsis.find("Sinopsis de") == 0:
                        sinopsis += "\n"
                        #print(sinopsis)
                if ind==2:
                    titulo_str = campo
                    if titulo_str.find("Título original:") == 0:
                        titulo_org = titulo_str.split("Título original:")
                        #print(titulo_org[-1])
                if ind==3:
                    descripcion = campo.split(":")
                    str1 = ' '.join(s for s in descripcion)
                    str1 = str1.replace("Desde el Berlín de 1936 al Israel de 1983 no hay tregua para el lector que quiera dejarse llevar por este folletín de corte humanista a través de la locura de los totalitarismos.", "")
                    #print(str1)
                    #print(descripcion)
                #if ind==4 or i%9 == 0:
                    #sinopsis = campo.split("Sinopsis de " + manga)
                
                    script = str1.find("Guion ")
                    #if script != 0:
                        #script = script - 1
                    #print(script)
                    f = str1.find("Dibujo ")
                    color = str1.find("Color ")
                    hist_original = str1.find("Historia original ")
                    dis_pers = str1.find("Diseño de personajes ")
                    sup = str1.find("Supervisión ")
                    prod = str1.find("Producción ")
                    colab = str1.find("Colaborador ")
                    concep_art = str1.find("Concepción artistica original ")
                    diseños = str1.find("Diseños ")
                    escenarios = str1.find("Escenarios ")
                    #print(f)
                    ed_amer = str1.find("Editorial americana ")
                    ed_fran = str1.find("Editorial francesa ")
                    r = str1.find("Editorial japonesa ") 
                    ej = str1.find("Editorial española ") 
                    es = str1.find("Colección ") 
                    gn = str1.find("Formato ") 
                    form = str1.find("Sentido de lectura ")
                    sent_lec = str1.find("Números en japonés ")
                    num_jap = str1.find("Números en español ")
                    if f != -1:
                        guion.append(str1[script + 6:f])
                    else:
                        guion.append("")
                    #print(guion[-1])
                    if f != -1:
                        if dis_pers != -1 and hist_original != -1 or dis_pers != -1:
                            dibujo.append(str1[f+6:dis_pers])
                        elif hist_original != -1 and sup != -1 or hist_original != -1:
                            dibujo.append(str1[f+6:hist_original])
                        elif hist_original != -1 and color != -1:
                            dibujo.append(str1[f+6:hist_original])
                        elif sup != -1 and colab != -1 or sup != -1:
                            dibujo.append(str1[f+6:sup])
                        elif color != -1:
                            dibujo.append(str1[f+6:color])
                        elif prod != -1:
                            dibujo.append(str1[f+6:prod])
                        elif colab != -1:
                            dibujo.append(str1[f+6:colab])
                        elif concep_art != -1:
                            dibujo.append(str1[f+6:concep_art])
                        elif diseños != -1:
                            dibujo.append(str1[f+6:diseños])
                        elif escenarios != -1:
                            dibujo.append(str1[f+6:escenarios])
                        else:
                            dibujo.append(str1[f+6:r])
                    else:
                        dibujo.append("")
                    #print(dibujo[-1])
                    if ed_fran != -1:
                        ed_francesa.append(str1[ed_fran+19:ej])
                    else:
                        ed_francesa.append("")
                    if ed_amer != -1:
                        ed_americana.append(str1[ed_amer+19:ej])
                    else:
                        ed_americana.append("")
                    #print(ed_francesa[-1])
                    if r != -1:
                        ed_japonesa.append(str1[r+18:ej])
                    else:
                        ed_japonesa.append("")
                    #print(ed_japonesa[-1])
                    if ej != -1:
                        ed_española.append(str1[ej+18:es])
                    else:
                        ed_española.append("")
                    #print(ed_española[-1])
                    if es != -1:
                        generos.append(str1[es+9:gn])
                    else:
                        generos.append("")
                    #print(generos[-1])
                    if gn != -1:
                        formatos.append(str1[gn+7:form])
                    else:
                        formatos.append("")
                    #print(formatos[-1])
                    if form != -1:
                        sentido_lectura.append(str1[form+18:sent_lec])
                    else:
                        sentido_lectura.append("")
                    #print(sentido_lectura[-1])
                    if sent_lec != -1:
                        num_japones.append(str1[sent_lec+18:num_jap])
                    else:
                        num_japones.append("")
                    #print(num_japones[-1])
                    if num_jap != -1:
                        num_español.append(str1[num_jap+18:len(str1)])
                    else:
                        num_español.append("")
                    #print(num_español[-1])
        for child_col in children_col:
            for titulo_col in child_col.find_all("h2"):
                if titulo_col.string.capitalize().find("Sinopsis") != -1 or titulo_col.string.capitalize().find("Cofre") != -1 or titulo_col.string.capitalize().find("Regalo") != -1 or titulo_col.string.capitalize().find("Números") != -1 or titulo_col.string.capitalize().find("Ficha") != -1 or titulo_col.string.capitalize().find("Carta") != -1 or titulo_col.string.capitalize().find("Preview") != -1 or titulo_col.string.capitalize().find("Promo") != -1 or titulo_col.string.capitalize().find("Ilustración") != -1 or titulo_col.string.capitalize().find("Títulos") != -1 or titulo_col.string.capitalize().find("Otras ediciones") != -1:
                    pass
                else:
                    titulos_obras.append(titulo_col.string)
        for datos_tomos in col_html.find_all("td",{"class":"cen"}):
            for img_nov in datos_tomos.find_all("img"):
                img_nov['src'] = "http://www.listadomanga.es/" + img_nov['src']
                #print(img_nov['src'])
                imgs_tomos.append(img_nov['src'])
            u = datos_tomos.get_text()
            w = u.find(" página")
            n = u.find("nº")
            inicio = 0
            pesetas = u.find("Ptas.")
            pag_bn = u.find("B/N")
            pag_color = u.find("color")
            euros = u.find(" €")
            resta_ind = w - n
            resta_ind2 = w-inicio
            #print(u)
            if n != -1:
                if w != -1:
                    if pesetas == -1 and euros != -1:
                        if resta_ind == 6:
                            num_tomos.append(u[0:n+3])
                            if pag_bn != -1 and pag_color != -1 or pag_color != -1:
                                num_paginas.append(u[n+3:pag_color+5])
                                precio_tomos.append(u[pag_color+5:euros+1])
                            elif pag_bn != -1:
                                num_paginas.append(u[n+3:pag_bn+3])
                                precio_tomos.append(u[pag_bn+3:euros+1])
                        elif resta_ind == 7:
                            num_tomos.append(u[0:n+4])
                            if pag_bn != -1 and pag_color != -1 or pag_color != -1:
                                num_paginas.append(u[n+4:pag_color+5])
                                precio_tomos.append(u[pag_color+5:euros+1])
                            elif pag_bn != -1:
                                num_paginas.append(u[n+4:pag_bn+3])
                                precio_tomos.append(u[pag_bn+3:euros+1])
                    elif pesetas != -1 and euros == -1:
                        precio_tomos.append("")
                else:
                    num_tomos.append(u[0:len(u)])
                    num_paginas.append("")
            else:
                if w != -1:
                    if pesetas == -1 and euros != -1:
                        num_tomos.append(u[0:w-3])
                        if pag_bn != -1 and pag_color != -1 or pag_color != -1:
                            num_paginas.append(u[w-3:pag_color+5])
                            precio_tomos.append(u[pag_color+5:euros+1])
                        elif pag_bn != -1:
                            num_paginas.append(u[w-3:pag_bn+3])
                            precio_tomos.append(u[pag_bn+3:euros+1])
                    elif pesetas != -1 and euros == -1:
                        precio_tomos.append("")
                else:
                    num_tomos.append("")
                    num_paginas.append("")
                    precio_tomos.append("")
            lista_nueva = []
            lista_nueva.append(num_tomos[-1])
            lista_nueva2 = f7(lista_nueva)
        #print(imgs_tomos[-1])
            print(lista_nueva2)
            print(titulos_obras[-1])
        #print(precio_tomos[-1])
        #print(num_paginas[-1])
__all__ = ['titulos_obras','sinopsis','titulo_org','guion','dibujo','ed_francesa','ed_americana','ed_japoensa','ed_española','generos','formatos','sentido_lectura','num_japones','num_español','imgs_tomos','num_paginas','precio_tomos','lista_nueva2']

    


            
        


            
                  

                

            

            




        