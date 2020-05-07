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
import mysql.connector

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
    conn = mysql.connector.connect(host="localhost",port=3306,db="mydb",user="root",password="")
    cursor = conn.cursor()
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
    try:
        def html_data():
            res2 = []
            req = urllib.request.Request('http://www.listadomanga.es/lista.php', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
            res = BeautifulSoup(urlopen(req).read(), "html.parser")
            children = res.findAll("td",{"class":"izq"})
            enlaces=[]
            for child in children:
                res = child.find_all("a")
                for res1 in res:
                    res1.attrs['href'] = "http://www.listadomanga.es/" + res1.attrs['href']
                    enlaces.append(res1.attrs['href'])
        
            for i in enlaces:
                col_html = BeautifulSoup(urlopen(i).read(),"html.parser")
                res2 = col_html.findAll("td",{"class":"izq"})
                for j in res2:
                    yield j
        
        def html_data_col():  
            res2 = []
            res_cen = []
            res_cen2 = []
            not_ediciones = []
            ediciones_titulos = []
            req = urllib.request.Request('http://www.listadomanga.es/lista.php', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
            res = BeautifulSoup(urlopen(req).read(), "html.parser")
            children = res.findAll("td",{"class":"izq"})
            enlaces=[]
            for child in children:
                res = child.find_all("a")
                for res1 in res:
                    res1.attrs['href'] = "http://www.listadomanga.es/" + res1.attrs['href']
                    enlaces.append(res1.attrs['href'])
        
            for i in enlaces:
                req2 = urllib.request.Request(i, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
                col_html = BeautifulSoup(urlopen(req2).read(),"html.parser")
                not_ediciones = col_html.find_all("td",{"class":"izq"})
                res2 = col_html.find_all("td",{"class":"cen"})
                '''for edicion in not_ediciones:
                    for ed in edicion.find_all("h2"):
                        ediciones_titulos.append(ed.string)
                for td in res2:
                    res_cen.append(td)
                for ed,cen in zip(ediciones_titulos,res_cen):
                    #if ed.string.capitalize().find("Otras ediciones") == -1:
                            #res_cen2.append(cen)
                    print(ed,cen)'''
                for x in res2:
                    yield x

        
        def titulo_obras(children_col):
            titulos_obras=[]
            for child_col in children_col:
                #titulo_col = child_col.find_all("h2")
                #resto_titulos_col = child_col.find_all("b")
                enlaces_valor_col = child_col.find_all("a")
            
                for titulo_col in child_col.find_all("h2"):
                    if titulo_col.string.capitalize().find("Sinopsis") != -1 or titulo_col.string.capitalize().find("Cofre") != -1 or titulo_col.string.capitalize().find("Regalo") != -1 or titulo_col.string.capitalize().find("Números") != -1 or titulo_col.string.capitalize().find("Ficha") != -1 or titulo_col.string.capitalize().find("Carta") != -1 or titulo_col.string.capitalize().find("Preview") != -1 or titulo_col.string.capitalize().find("Promo") != -1 or titulo_col.string.capitalize().find("Ilustración") != -1 or titulo_col.string.capitalize().find("Títulos") != -1 or titulo_col.string.capitalize().find("Otras ediciones") != -1:
                        pass
                    else:
                        titulos_obras.append(titulo_col.string)
                        #print(titulos_obras)
                        yield titulos_obras[-1]

        
        def titulo_obras2():
            lista = []
            req = urllib.request.Request('http://www.listadomanga.es/lista.php', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
            res = BeautifulSoup(urlopen(req).read(), "html.parser")
            children = res.findAll("td",{"class":"izq"})
            enlaces=[]
            for child in children:
                res = child.find_all("a")
                for i in res:
                    enl_name = i.string
                    yield enl_name
        
                        
        res = html_data()
        res2 = html_data_col()

        def txt_titulos():
            outputFile = open("output_titulos_obras.txt","w",encoding="utf-8")
            for i in titulo_obras2():
                string = str(i)
                outputFile.write(string + "\n")
            outputFile.close()
        
        def list_titulos_obras():
            f = open("output_titulos_obras.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s

                        
        def sinopsis_obras(children_col):
            lista = []
            for child_col in children_col:
                x = child_col.get_text()
                j = x.split("\n")

                
                for campo in j:
                    print(campo)
                    ind = j.index(campo)
                    u = "".join(campo.splitlines())
                    if campo.find("Otras ediciones de ") == 0 or campo.find("Números editados") == 0 or campo.find("Números no editados") == 0 or campo.find("Números en preparación")==0:
                        j.pop(ind)
                #print(j)
                for campo in j: 
                    ind = j.index(campo)
                    #print("El campo es:" + campo + " y su INDICE es el siguiente:" + str(ind))
                    if ind==0 or ind%5 == 0:
                        u = "".join(campo.splitlines())
                        sinopsis=u
                        if sinopsis.find("Sinopsis de") == 0:
                            sinopsis += "\n"
                            lista.append(sinopsis)
                        elif sinopsis.find("Sinopsis de") == -1:
                            lista.append("\n")
                        yield lista[-1]
                        
        def txt_sinopsis():
            outputFile = open("output_sinopsis.txt","w",encoding="utf-8")
            for i in sinopsis_obras(res):
                string = str(i)
                outputFile.write(string)
            outputFile.close()

        #txt_sinopsis()
            
        def tit_original(children_col):
            for child_col in children_col:
                x = child_col.get_text()
                j = x.split("\n")

                
                for campo in j:
                    ind = j.index(campo)
                    if campo.find("Otras ediciones de ") == 0 or campo.find("Números editados") == 0 or campo.find("Números no editados") == 0 or campo.find("Números en preparación")==0:
                        j.pop(ind)
                #print(j)
                for campo in j: 
                    ind = j.index(campo)
                    if ind==2:
                        titulo_str = campo
                        if titulo_str.find("Título original:") == 0:
                            titulo_org = titulo_str.split("Título original:")
                            yield titulo_org[-1]
        
        def txt_titulo_org():
            outputFile = open("output_titulos_org.txt","w",encoding="utf-8")
            for i in tit_original(res):
                string = str(i) + "\n"
                outputFile.write(string)
            outputFile.close()

        def list_tit_original():
            f = open("output_titulos_org.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s


        def guion_obras(children_col):
            guion = []
            lista = []
            for child_col in children_col:
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
                    if ind==3:
                        descripcion = campo.split(":")
                        str1 = ' '.join(s for s in descripcion)
                        str1 = str1.replace("Desde el Berlín de 1936 al Israel de 1983 no hay tregua para el lector que quiera dejarse llevar por este folletín de corte humanista a través de la locura de los totalitarismos.", "")
                        f = str1.find("Dibujo ")
                        script = str1.find("Guion ")
                        autores = str1.find("Autores")
                        ilustracion = str1.find("Ilustraciones")
                        ilustraciones_compl = str1.find("Ilustraciones Completas")
                        ed_jap = str1.find("Editorial japonesa")
                        ed_esp = str1.find("Editorial española")
                        if script != -1:
                            guion.append(str1[script + 6:f])
                            yield guion[-1]
                        elif script == -1 and f != -1:
                            guion.append("")
                            yield guion[-1]
                        elif script == -1  and f == -1 and autores != -1:
                            guion.append("")
                            yield guion[-1]
                        elif ilustraciones_compl != -1:
                            pass
                        elif script == -1  and f == -1 and autores == -1 and ilustracion != -1:
                            guion.append("")
                            yield guion[-1]
                        elif script == -1  and f == -1 and autores == -1 and ilustracion == -1 and ed_jap != -1:
                            guion.append("")
                            yield guion[-1]
                        elif script == -1  and f == -1 and autores == -1 and ilustracion == -1 and ed_jap == -1 and ed_esp != -1:
                            guion.append("")
                            yield guion[-1]
                        
                        
        
        def txt_guion():
            outputFile = open("output_guion.txt","w",encoding="utf-8")
            for i in guion_obras(res):
                string = str(i) + "\n"
                outputFile.write(string)
            outputFile.close()

        #txt_guion()
        
        def list_guion():
            f = open("output_guion.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s

        
        def dibujo_obras(children_col):
            dibujo = []
            for child_col in children_col:
                x = child_col.get_text()
                j = x.split("\n")

                for campo in j:
                    ind = j.index(campo)
                    if campo.find("Otras ediciones de ") == 0 or campo.find("Números editados") == 0 or campo.find("Números no editados") == 0 or campo.find("Números en preparación")==0:
                        j.pop(ind)
                #print(j)
                for campo in j: 
                    ind = j.index(campo)
                    if ind==3:
                        descripcion = campo.split(":")
                        str1 = ' '.join(s for s in descripcion)
                        str1 = str1.replace("Desde el Berlín de 1936 al Israel de 1983 no hay tregua para el lector que quiera dejarse llevar por este folletín de corte humanista a través de la locura de los totalitarismos.", "")
                        
                    

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
                        r = str1.find("Editorial japonesa ")
                        ed_esp = str1.find("Editorial española")
                        ed_franc = str1.find("Editorial francesa")
                        autores = str1.find("Autores") 
                        ed_sing = str1.find("Editorial singapurense")
                        story = str1.find("Storyboard")
                        idea_org = str1.find("Idea Original")
                        asistentes = str1.find("Asistentes")
                        one_piece1 = str1.find("Color Walk")
                        if f != -1:
                            if dis_pers != -1 and hist_original != -1 or dis_pers != -1:
                                dibujo.append(str1[f+6:dis_pers])
                                yield dibujo[-1]
                            elif hist_original != -1 and sup != -1 or hist_original != -1:
                                dibujo.append(str1[f+6:hist_original])
                                yield dibujo[-1]
                            elif hist_original != -1 and color != -1:
                                dibujo.append(str1[f+6:hist_original])
                                yield dibujo[-1]
                            elif sup != -1 and colab != -1 or sup != -1:
                                dibujo.append(str1[f+6:sup])
                                yield dibujo[-1]
                            elif color != -1:
                                dibujo.append(str1[f+6:color])
                                yield dibujo[-1]
                            elif prod != -1:
                                dibujo.append(str1[f+6:prod])
                                yield dibujo[-1]
                            elif colab != -1:
                                dibujo.append(str1[f+6:colab])
                                yield dibujo[-1]
                            elif concep_art != -1:
                                dibujo.append(str1[f+6:concep_art])
                                yield dibujo[-1]
                            elif diseños != -1:
                                dibujo.append(str1[f+6:diseños])
                                yield dibujo[-1]
                            elif escenarios != -1:
                                dibujo.append(str1[f+6:escenarios])
                                yield dibujo[-1]
                            elif r == -1 and ed_esp != -1:
                                dibujo.append(str1[f+6:ed_esp])
                                yield dibujo[-1]
                            elif r ==-1 and ed_franc != -1:
                                dibujo.append(str1[f+6:ed_franc])
                                yield dibujo[-1]
                            elif autores != -1:
                                dibujo.append(str1[f+6:autores])
                                yield dibujo[-1]
                            elif r ==-1 and ed_sing != -1:
                                dibujo.append(str1[f+6:ed_sing])
                                yield dibujo[-1]
                            elif story != -1:
                                dibujo.append(str1[f+6:story])
                                yield dibujo[-1]
                            elif idea_org != -1:
                                dibujo.append(str1[f+6:idea_org])
                                yield dibujo[-1]
                            elif asistentes != -1:
                                dibujo.append(str1[f+6:asistentes])
                                yield dibujo[-1]
                            else:
                                dibujo.append(str1[f+6:r])
                                yield dibujo[-1]
                        else:
                            if one_piece1 != -1:
                                pass
                            elif dis_pers != -1:
                                dibujo.append("")
                                yield dibujo[-1]
                            elif dis_pers == -1 and hist_original != -1:
                                dibujo.append("")
                                yield dibujo[-1]
                            elif dis_pers == -1 and hist_original == -1 and color != -1:
                                dibujo.append("")
                                yield dibujo[-1]
                            elif dis_pers == -1 and hist_original == -1 and color == -1 and colab != -1:
                                dibujo.append("")
                                yield dibujo[-1]
                            elif dis_pers == -1 and hist_original == -1 and color == -1 and colab == -1 and prod != -1:
                                dibujo.append("")
                                yield dibujo[-1]
                            elif dis_pers == -1 and hist_original == -1 and color == -1 and colab == -1 and prod == -1 and concep_art != -1:
                                dibujo.append("")
                                yield dibujo[-1]
                            elif dis_pers == -1 and hist_original == -1 and color == -1 and colab == -1 and prod == -1 and concep_art == -1 and diseños !=-1:
                                dibujo.append("")
                                yield dibujo[-1]
                            elif dis_pers == -1 and hist_original == -1 and color == -1 and colab == -1 and prod == -1 and concep_art == -1 and diseños ==-1 and escenarios != -1:
                                dibujo.append("")
                                yield dibujo[-1]
                            elif dis_pers == -1 and hist_original == -1 and color == -1 and colab == -1 and prod == -1 and concep_art == -1 and diseños ==-1 and escenarios == -1 and r != -1:
                                dibujo.append("")
                                yield dibujo[-1]
                            elif dis_pers == -1 and hist_original == -1 and color == -1 and colab == -1 and prod == -1 and concep_art == -1 and diseños ==-1 and escenarios == -1 and r == -1 and ed_esp !=-1:
                                dibujo.append("")
                                yield dibujo[-1]
                            elif dis_pers == -1 and hist_original == -1 and color == -1 and colab == -1 and prod == -1 and concep_art == -1 and diseños ==-1 and escenarios == -1 and r == -1 and ed_esp ==-1 and ed_franc != -1:
                                dibujo.append("")
                                yield dibujo[-1]
                            elif dis_pers == -1 and hist_original == -1 and color == -1 and colab == -1 and prod == -1 and concep_art == -1 and diseños ==-1 and escenarios == -1 and r == -1 and ed_esp ==-1 and ed_franc == -1 and ed_sing != -1:
                                dibujo.append("")
                                yield dibujo[-1]
                            elif dis_pers == -1 and hist_original == -1 and color == -1 and colab == -1 and prod == -1 and concep_art == -1 and diseños ==-1 and escenarios == -1 and r == -1 and ed_esp ==-1 and ed_franc == -1 and ed_sing == -1 and autores != -1:
                                dibujo.append("")
                                yield dibujo[-1]
                            elif dis_pers == -1 and hist_original == -1 and color == -1 and colab == -1 and prod == -1 and concep_art == -1 and diseños ==-1 and escenarios == -1 and r == -1 and ed_esp ==-1 and ed_franc == -1 and ed_sing == -1 and autores == -1 and story != -1:
                                dibujo.append("")
                                yield dibujo[-1]
                            elif dis_pers == -1 and hist_original == -1 and color == -1 and colab == -1 and prod == -1 and concep_art == -1 and diseños ==-1 and escenarios == -1 and r == -1 and ed_esp ==-1 and ed_franc == -1 and ed_sing == -1 and autores == -1 and story == -1 and idea_org != -1:
                                dibujo.append("")
                                yield dibujo[-1]
                            elif dis_pers == -1 and hist_original == -1 and color == -1 and colab == -1 and prod == -1 and concep_art == -1 and diseños ==-1 and escenarios == -1 and r == -1 and ed_esp ==-1 and ed_franc == -1 and ed_sing == -1 and autores == -1 and story == -1 and idea_org == -1 and asistentes != -1:
                                dibujo.append("")
                                yield dibujo[-1]
                            




        
        def txt_dibujo():
            outputFile = open("output_dibujo.txt","w",encoding="utf-8")
            for i in dibujo_obras(res):
                string = str(i) + "\n"
                outputFile.write(string)
            outputFile.close()

        def list_dibujo():
            f = open("output_dibujo.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s



        def edicion_francesa(children_col):
            ed_francesa = []
            for child_col in children_col:
                x = child_col.get_text()
                j = x.split("\n")

                for campo in j:
                    ind = j.index(campo)
                    if campo.find("Otras ediciones de ") == 0 or campo.find("Números editados") == 0 or campo.find("Números no editados") == 0 or campo.find("Números en preparación")==0:
                        j.pop(ind)
                #print(j)
                for campo in j: 
                    ind = j.index(campo)
                    if ind==3:
                        descripcion = campo.split(":")
                        str1 = ' '.join(s for s in descripcion)
                        str1 = str1.replace("Desde el Berlín de 1936 al Israel de 1983 no hay tregua para el lector que quiera dejarse llevar por este folletín de corte humanista a través de la locura de los totalitarismos.", "")
                        ed_fran = str1.find("Editorial francesa ")
                        ej = str1.find("Editorial española ") 
                        if ed_fran != -1:
                            ed_francesa.append(str1[ed_fran+19:ej])
                            yield ed_francesa[-1]
                        elif ed_fran == -1 and ej != -1:
                            ed_francesa.append("")
                            yield ed_francesa[-1]

        def txt_ed_francesa():
            outputFile = open("output_ed_francesa.txt","w",encoding="utf-8")
            for i in edicion_francesa(res):
                string = str(i) + "\n"
                outputFile.write(string)
            outputFile.close()

        def list_ed_francesa():
            f = open("output_ed_francesa.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s


        def edicion_americana(children_col):
            ed_americana = []
            for child_col in children_col:
                x = child_col.get_text()
                j = x.split("\n")

                for campo in j:
                    ind = j.index(campo)
                    if campo.find("Otras ediciones de ") == 0 or campo.find("Números editados") == 0 or campo.find("Números no editados") == 0 or campo.find("Números en preparación")==0:
                        j.pop(ind)
                #print(j)
                for campo in j: 
                    ind = j.index(campo)
                    if ind==3:
                        descripcion = campo.split(":")
                        str1 = ' '.join(s for s in descripcion)
                        str1 = str1.replace("Desde el Berlín de 1936 al Israel de 1983 no hay tregua para el lector que quiera dejarse llevar por este folletín de corte humanista a través de la locura de los totalitarismos.", "")
                        ed_amer = str1.find("Editorial americana ")
                        ej = str1.find("Editorial española ") 
                        if ed_amer != -1:
                            ed_americana.append(str1[ed_amer+19:ej])
                            yield ed_americana[-1]
                        elif ed_amer == -1 and ej != -1:
                            ed_americana.append("")
                            yield ed_americana[-1]

        def txt_ed_americana():
            outputFile = open("output_ed_americana.txt","w",encoding="utf-8")
            for i in edicion_americana(res):
                string = str(i) + "\n"
                outputFile.write(string)
            outputFile.close()
        
        def list_ed_americana():
            f = open("output_ed_americana.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s



        def edicion_japonesa(children_col):
            ed_japonesa = []
            for child_col in children_col:
                x = child_col.get_text()
                j = x.split("\n")

                for campo in j:
                    ind = j.index(campo)
                    if campo.find("Otras ediciones de ") == 0 or campo.find("Números editados") == 0 or campo.find("Números no editados") == 0 or campo.find("Números en preparación")==0:
                        j.pop(ind)
                #print(j)
                for campo in j: 
                    ind = j.index(campo)
                    if ind==3:
                        descripcion = campo.split(":")
                        str1 = ' '.join(s for s in descripcion)
                        str1 = str1.replace("Desde el Berlín de 1936 al Israel de 1983 no hay tregua para el lector que quiera dejarse llevar por este folletín de corte humanista a través de la locura de los totalitarismos.", "")
                        ed_jap = str1.find("Editorial japonesa ")
                        ej = str1.find("Editorial española ") 
                        if ed_jap != -1:
                            ed_japonesa.append(str1[ed_jap+18:ej])
                            yield ed_japonesa[-1]
                        elif ed_jap == -1 and ej != -1:
                            ed_japonesa.append("")
                            yield ed_japonesa[-1]

        def txt_ed_jap():
            outputFile = open("output_ed_jap.txt","w",encoding="utf-8")
            for i in edicion_japonesa(res):
                string = str(i) + "\n"
                outputFile.write(string)
            outputFile.close()

        def list_ed_jap():
            f = open("output_ed_jap.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s


        def edicion_española(children_col):
            ed_española = []
            for child_col in children_col:
                x = child_col.get_text()
                j = x.split("\n")

                for campo in j:
                    ind = j.index(campo)
                    if campo.find("Otras ediciones de ") == 0 or campo.find("Números editados") == 0 or campo.find("Números no editados") == 0 or campo.find("Números en preparación")==0:
                        j.pop(ind)
                #print(j)
                for campo in j: 
                    ind = j.index(campo)
                    if ind==3:
                        descripcion = campo.split(":")
                        str1 = ' '.join(s for s in descripcion)
                        str1 = str1.replace("Desde el Berlín de 1936 al Israel de 1983 no hay tregua para el lector que quiera dejarse llevar por este folletín de corte humanista a través de la locura de los totalitarismos.", "")
                        es = str1.find("Colección ") 
                        ej = str1.find("Editorial española ") 
                        if ej != -1:
                            ed_española.append(str1[ej+18:es])
                            yield ed_española[-1]
                        elif ej == -1 and es != -1:
                            ed_española.append("")
                            yield ed_española[-1]
        def txt_ed_esp():
            outputFile = open("output_ed_esp.txt","w",encoding="utf-8")
            for i in edicion_española(res):
                string = str(i) + "\n"
                outputFile.write(string)
            outputFile.close()

        def list_ed_esp():
            f = open("output_ed_esp.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s


        def generos_obras(children_col):
            generos = []
            for child_col in children_col:
                x = child_col.get_text()
                j = x.split("\n")

                for campo in j:
                    ind = j.index(campo)
                    if campo.find("Otras ediciones de ") == 0 or campo.find("Números editados") == 0 or campo.find("Números no editados") == 0 or campo.find("Números en preparación")==0:
                        j.pop(ind)
                #print(j)
                for campo in j: 
                    ind = j.index(campo)
                    if ind==3:
                        descripcion = campo.split(":")
                        str1 = ' '.join(s for s in descripcion)
                        str1 = str1.replace("Desde el Berlín de 1936 al Israel de 1983 no hay tregua para el lector que quiera dejarse llevar por este folletín de corte humanista a través de la locura de los totalitarismos.", "")
                        es = str1.find("Colección ") 
                        gn = str1.find("Formato ") 
                        if es != -1:
                            generos.append(str1[es+9:gn])
                            yield generos[-1]
                        elif es == -1 and gn != -1:
                            generos.append("")
                            yield generos[-1]
        
        def txt_generos():
            outputFile = open("output_generos.txt","w",encoding="utf-8")
            for i in generos_obras(res):
                string = str(i) + "\n"
                outputFile.write(string)
            outputFile.close()

        def list_generos():
            f = open("output_generos.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s


        def formatos_obras(children_col):
            formatos = []
            for child_col in children_col:
                x = child_col.get_text()
                j = x.split("\n")

                for campo in j:
                    ind = j.index(campo)
                    if campo.find("Otras ediciones de ") == 0 or campo.find("Números editados") == 0 or campo.find("Números no editados") == 0 or campo.find("Números en preparación")==0:
                        j.pop(ind)
                #print(j)
                for campo in j: 
                    ind = j.index(campo)
                    if ind==3:
                        descripcion = campo.split(":")
                        str1 = ' '.join(s for s in descripcion)
                        str1 = str1.replace("Desde el Berlín de 1936 al Israel de 1983 no hay tregua para el lector que quiera dejarse llevar por este folletín de corte humanista a través de la locura de los totalitarismos.", "")
                        form = str1.find("Sentido de lectura ") 
                        gn = str1.find("Formato ") 
                        if gn != -1:
                            formatos.append(str1[gn+7:form])
                            yield formatos[-1]
                        elif gn == -1 and form != -1:
                            formatos.append("")
                            yield formatos[-1]
        
        def txt_formatos():
            outputFile = open("output_formatos.txt","w",encoding="utf-8")
            for i in formatos_obras(res):
                string = str(i) + "\n"
                outputFile.write(string)
            outputFile.close()

        def list_formatos():
            f = open("output_formatos.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s


        def sent_lectura_obras(children_col):
            sentido_lectura = []
            for child_col in children_col:
                x = child_col.get_text()
                j = x.split("\n")

                for campo in j:
                    ind = j.index(campo)
                    if campo.find("Otras ediciones de ") == 0 or campo.find("Números editados") == 0 or campo.find("Números no editados") == 0 or campo.find("Números en preparación")==0:
                        j.pop(ind)
                #print(j)
                for campo in j: 
                    ind = j.index(campo)
                    if ind==3:
                        descripcion = campo.split(":")
                        str1 = ' '.join(s for s in descripcion)
                        str1 = str1.replace("Desde el Berlín de 1936 al Israel de 1983 no hay tregua para el lector que quiera dejarse llevar por este folletín de corte humanista a través de la locura de los totalitarismos.", "")
                        form = str1.find("Sentido de lectura ") 
                        sent_lec = str1.find("Números en japonés ") 
                        if form != -1:
                            sentido_lectura.append(str1[form+18:sent_lec])
                            yield sentido_lectura[-1]
                        elif form == -1 and sent_lec != -1:
                            sentido_lectura.append("")
                            yield sentido_lectura[-1]

        def txt_sent_lectura():
            outputFile = open("output_sent_lectura.txt","w",encoding="utf-8")
            for i in sent_lectura_obras(res):
                string = str(i) + "\n"
                outputFile.write(string)
            outputFile.close()
        
        def list_sent_lectura():
            f = open("output_sent_lectura.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s

            
        def numeros_japon(children_col):
            num_japones = []
            for child_col in children_col:
                x = child_col.get_text()
                j = x.split("\n")

                for campo in j:
                    ind = j.index(campo)
                    if campo.find("Otras ediciones de ") == 0 or campo.find("Números editados") == 0 or campo.find("Números no editados") == 0 or campo.find("Números en preparación")==0:
                        j.pop(ind)
                #print(j)
                for campo in j: 
                    ind = j.index(campo)
                    if ind==3:
                        descripcion = campo.split(":")
                        str1 = ' '.join(s for s in descripcion)
                        str1 = str1.replace("Desde el Berlín de 1936 al Israel de 1983 no hay tregua para el lector que quiera dejarse llevar por este folletín de corte humanista a través de la locura de los totalitarismos.", "")
                        num_jap = str1.find("Números en español ")
                        sent_lec = str1.find("Números en japonés ") 
                        if sent_lec != -1:
                            num_japones.append(str1[sent_lec+18:num_jap])
                            yield num_japones[-1]
                        elif sent_lec == -1 and num_jap != -1:
                            num_japones.append("")
                            yield num_japones[-1]
        
        def txt_num_japon():
            outputFile = open("output_num_japon.txt","w",encoding="utf-8")
            for i in numeros_japon(res):
                string = str(i) + "\n"
                outputFile.write(string)
            outputFile.close()

        def list_num_japon():
            f = open("output_num_japon.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s



        def numeros_españa(children_col):
            num_español = []
            for child_col in children_col:
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
                    if ind==3:
                        descripcion = campo.split(":")
                        str1 = ' '.join(s for s in descripcion)
                        str1 = str1.replace("Desde el Berlín de 1936 al Israel de 1983 no hay tregua para el lector que quiera dejarse llevar por este folletín de corte humanista a través de la locura de los totalitarismos.", "")
                        num_jap = str1.find("Números en español ")
                        sent_lec = str1.find("Números en japonés ")
                        nota = str1.find("Nota")
                        if num_jap != -1 and nota != -1: 
                            num_español.append(str1[num_jap+18:nota])
                            yield num_español[-1]
                        elif num_jap != -1 and nota == -1:
                            num_español.append(str1[num_jap+18:len(str1)])
                            yield num_español[-1]
 
        
        def txt_num_españa():
            outputFile = open("output_num_españa.txt","w",encoding="utf-8")
            for i in numeros_españa(res):
                string = str(i) + "\n"
                outputFile.write(string)
            outputFile.close()

        def list_num_españa():
            f = open("output_num_españa.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s



        def res_obras():
            lista = []
            tit_obras = list_titulos_obras()
            tit_org = list_tit_original()
            dibujos = list_dibujo()
            guion = list_guion()
            ed_franc = list_ed_francesa()
            ed_amer = list_ed_americana()
            ed_jap = list_ed_jap()
            ed_esp = list_ed_esp()
            genero = list_generos()
            formato = list_formatos()
            sent_lectura = list_sent_lectura()
            tomos_jap = list_num_japon()
            tomos_españa = list_num_españa()
            

            for i in range(len(tit_obras)):
                lista.append((str(tit_obras[i]),str(tit_org[i]),str(dibujos[i]),str(guion[i]),str(ed_franc[i]),str(ed_amer[i]),str(ed_jap[i]),str(ed_esp[i]),str(genero[i]),str(formato[i]),str(sent_lectura[i]),str(tomos_jap[i]),str(tomos_españa[i])))
            cursor.executemany("INSERT INTO `colección`(`titulo_coleccion`, `titulo_original`, `dibujante`, `guionista`, `edicion_francesa`, `editorial_americana`, `editorial_japonesa`, `editorial_española`, `genero`, `formato`, `sentido_lectura`, `num_tomos_japon`, `num_tomos_españa`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",lista)
            conn.commit()
            print("Se han añadido los datos correctamente!!!!")


        #res_obras()


        def tabla_coleccion_has_tomos():
            lista = []
            #cursor.execute("SELECT `Id.tomo` FROM `tomos` LEFT JOIN `colección` ON `colección`.`titulo_coleccion` = `tomos`.`nombre_colección`")
            cursor.execute("SELECT `Id.tomo`,`nombre_colección` FROM `tomos`")
            myresult = cursor.fetchall()
            cursor.execute("SELECT `titulo_coleccion` FROM `colección`")
            myresult2 = cursor.fetchall()

            for x in myresult:
                for y in myresult2:
                    ind = myresult.index(x) + 1
                    if str(x[1]) == str(y[0]):
                        #print(y[0] + "     " + str(ind))
                        lista.append((str(y[0]),ind))
                        break
                continue
            cursor.executemany("INSERT INTO `colección_has_tomos`(`Colección_titulo_coleccion`, `Tomos_Id.tomo`) VALUES (%s,%s)",lista)
            conn.commit()
            print("Se han añadido los datos correctamente!!!!")
        tabla_coleccion_has_tomos()




        '''def prueba():
            lista1=[1,2,4]
            lista2=[1,2,3,4]
            res = []
            for x in lista1:
                for y in lista2:
                    if x == y:
                        res.append((x,y))
                        break
                continue
            print(res)
        
        prueba()'''



        
        def titulo_obra_per_tomo():
            req = urllib.request.Request('http://www.listadomanga.es/lista.php', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
            res = BeautifulSoup(urlopen(req).read(), "html.parser")
            children = res.findAll("td",{"class":"izq"})
            for child in children:
                res = child.find_all("a")
                for res1 in res:
                    res1.attrs['href'] = "http://www.listadomanga.es/" + res1.attrs['href']
                    enlaces.append(res1.attrs['href'])
                    titulos.append(res1.string)
            for i in range(len(enlaces)):
                req2 = urllib.request.Request(str(enlaces[i]), headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
                col_html = BeautifulSoup(urlopen(req2).read(), "html.parser")
                children_col = col_html.findAll("td",{"class":"izq"})
                for child_col in children_col:
                    for titulo_col in child_col.find_all("h2"):
                        if titulo_col.string.capitalize().find("Sinopsis") != -1 or titulo_col.string.capitalize().find("Cofre") != -1 or titulo_col.string.capitalize().find("Regalo") != -1 or titulo_col.string.capitalize().find("Números") != -1 or titulo_col.string.capitalize().find("Ficha") != -1 or titulo_col.string.capitalize().find("Carta") != -1 or titulo_col.string.capitalize().find("Preview") != -1 or titulo_col.string.capitalize().find("Promo") != -1 or titulo_col.string.capitalize().find("Ilustración") != -1 or titulo_col.string.capitalize().find("Títulos") != -1 or titulo_col.string.capitalize().find("Otras ediciones") != -1:
                            pass
                        else:
                            titulo_res = titulo_col.string[0:len(titulo_col.string)-2]
                            #print(titulo_res)
                            titulos_obras.append(titulo_res)
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
        
        def list_titulos():
            f = open("output_titulos.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s

        
        def compare_lists():
            for x in list_titulos():
                for y in x:
                    print(y)
            '''for x in list_titulos_obras():
                for y in list_titulos():
                    if x == y:
                        print(x + "          " + y + "   True")
                    else:
                        print(x + "   " + str(len(x))+"          " + y + "    " + str(len(y))+ "   False")'''
        #compare_lists()
        


        '''def numero_tomos(col_html):
            try:
                num_tomos = []
                for datos_tomos in col_html:
                    u = datos_tomos.get_text()
                    #print(u)
                    u = "".join(u.splitlines())
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
                            if pesetas == -1 or euros != -1:
                                if resta_ind == 6:
                                    num_tomos.append(u[0:n+3])
                                elif resta_ind == 7:
                                    num_tomos.append(u[0:n+4])
                        else:
                            num_tomos.append(u[0:len(u)])
                    else:
                        if w != -1:
                            if pesetas == -1 or euros != -1:
                                num_tomos.append(u[0:w-3])
                        else:
                            pass
                    lista_nueva = []
                    lista_nueva2 = []
                    lista_nueva.append(num_tomos[-1])
                    lista_nueva2 = f7(lista_nueva)
                    #print(lista_nueva2)
                    for i in lista_nueva2:
                        yield i
            except TypeError as e:
                print(e)'''


        def numero_tomos(col_html):
            num_tomos = []
            for datos_tomos in col_html:
                u = datos_tomos.get_text()
                u = "".join(u.splitlines())
                #print(u)
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
        
        def txt_numeros():
            outputFile = open("output_numeros.txt","w",encoding="utf-8")
            for i in numero_tomos(res2):
                string = str(i)
                outputFile.write(string + "\n")
            outputFile.close()
        
        #txt_numeros()
        
        def list_numeros():
            f = open("output_numeros.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s

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
        
        def txt_paginas():
            outputFile = open("output_paginas.txt","w",encoding="utf-8")
            for i in numero_paginas(res2):
                string = str(i)
                outputFile.write(string + "\n")
            outputFile.close()

        #txt_paginas()

        def list_paginas():
            f = open("output_paginas.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s
        
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
                                    precio_tomos.append(u[pag_color+5:euros+2])
                                elif pag_bn != -1:
                                    precio_tomos.append(u[pag_bn+3:euros+2])
                            elif resta_ind == 7:
                                if pag_bn != -1 and pag_color != -1 or pag_color != -1:
                                    precio_tomos.append(u[pag_color+5:euros+2])
                                elif pag_bn != -1:
                                    precio_tomos.append(u[pag_bn+3:euros+2])
                        elif pesetas != -1 and euros == -1:
                            precio_tomos.append("")
                else:
                    if w != -1:
                        if pesetas == -1 and euros != -1:
                            if pag_bn != -1 and pag_color != -1 or pag_color != -1:
                                precio_tomos.append(u[pag_color+5:euros+2])
                            elif pag_bn != -1:
                                precio_tomos.append(u[pag_bn+3:euros+2])
                        elif pesetas != -1 and euros == -1:
                            precio_tomos.append("")
                    else:
                        precio_tomos.append("")
                yield precio_tomos[-1]
        
        def txt_precios():
            outputFile = open("output_precios.txt","w",encoding="utf-8")
            for i in precios_tomos(res2):
                string = str(i)
                outputFile.write(string + "\n")
            outputFile.close()

        def list_precios():
            f = open("output_precios.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s
        
        #txt_precios()
        def portadas_tomos(col_html):
            imgs_tomos = []
            for datos_tomos in col_html:
                for img_nov in datos_tomos.find_all("img"):
                    img_nov['src'] = "http://www.listadomanga.es/" + img_nov['src']
                    imgs_tomos.append(img_nov['src'])
                yield imgs_tomos[-1]
        
        def txt_portadas():
            outputFile = open("output_portadas.txt","w",encoding="utf-8")
            for i in portadas_tomos(res2):
                string = str(i)
                outputFile.write(string + "\n")
            outputFile.close()
        
        #txt_portadas()

        def list_portadas():
            f = open("output_portadas.txt","r",encoding="utf-8")
            s = str(f.read()).splitlines()
            return s


        def res_tomos():
            lista = []
            paginas = list_paginas()
            precios = list_precios()
            titulos = list_titulos()
            portadas = list_portadas()
            tomos = list_numeros()
            
            for i in range(len(titulos)):
                lista.append((i,str(titulos[i]),str(portadas[i]),str(tomos[i]),str(paginas[i]),str(precios[i])))
            
            cursor.executemany("INSERT INTO `tomos`(`Id.tomo`,`nombre_colección`, `enlace_portada_tomo`, `nombre_tomo`, `paginas_tomo`, `precio_tomo`) VALUES (%s,%s,%s,%s,%s,%s)",lista)
            conn.commit()
            print("Se han añadido los datos correctamente!!!!")
        #res_tomos()
    
    except mysql.connector.Error as e:
        print("Failed to insert record into MySQL table {}".format(error))
    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

