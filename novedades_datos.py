from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from collections import OrderedDict
import re



def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

try:
    html= urlopen("http://www.listadomanga.es/novedades.php")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    def novedades(html):
        titulos_nov = []
        imgs_nov = []
        enlaces = []
        imgs_editoriales =[]
        lista_nueva =[]
        res = []

        res2 = BeautifulSoup(html.read(), "html.parser")
        children = res2.findAll("td",{"class":"cen"})
        for child in children:
            for titulo_nov in child.find_all("h2"):
                if titulo_nov.string.capitalize().find("Novedades") != -1:
                    titulos_nov.append(titulo_nov.string)
            for img_nov in child.find_all("img"):
                img_nov['src'] = "http://www.listadomanga.es/" + img_nov['src']
                #print(img_nov['src'])
                imgs_nov.append(img_nov['src'])
        
        lista_nueva = f7(imgs_nov)

        for img in lista_nueva:
            ind = lista_nueva.index(img)
            ind2 = img.find("editorial")
            if ind2 != -1:
                imgs_editoriales.append(img)
                lista_nueva.pop(ind)
        titulos_nov += lista_nueva
        res = titulos_nov
        for idx, elem in enumerate(res):
            thiselem = elem
            nextelem = res[(idx + 1) % len(res)]
            if thiselem.find("Novedades ") == 0 and nextelem.find("Novedades ") == 0:
                return titulos_nov
            
        children2 = res2.findAll("td",{"class":"der"})
        for child in children2:
            for res1 in child.find_all("a"):
                res1.attrs['href'] = "http://www.listadomanga.es/" + res1.attrs['href']
                mes_siguiente = res1.attrs['href']
                html2 = urlopen(mes_siguiente)
                return titulos_nov + novedades(html2)

    novedades(html)
    
    
    
    
    