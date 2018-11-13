import bs4 as bs
from urllib import request
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
from selenium.webdriver.chrome.options import Options
import multiprocessing
import time

"""Funciones para scrapear"""

def obt_links_primera_capa(url):
    domain=request.urlopen(url)
    data=domain.read()
    bse=bs.BeautifulSoup(data, 'html.parser')
    biga=set(bse.findAll('a', href=True))
    links=[a['href'] for a in biga if url in a['href']]
    return links

def obt_links_internos(url):
    todoslinks=[] #donde iran todos los links del dominio
    i=-1    #para iterar while
    capas=[] #capas de links

    domain=request.urlopen(url)
    data=domain.read()
    bse=bs.BeautifulSoup(data, 'html.parser')
    biga=set(bse.findAll('a', href=True))
    links=[a['href'] for a in biga if url in a['href']]

    capas.append(links)

    while i < len(todoslinks):
        for lista in capas:
            for link in lista:
                if link not in todoslinks:
                    if url in link:
                        todoslinks.append(link)
                        capa=obt_links_primera_capa(link)
                        capas.append(capa)
        i=i+1
    """Retorna todos los links internos de la página"""
    return todoslinks

def obtener_p(lista_links):
    lista_noticias=[]
    for link in lista_links:
        domain=request.urlopen(link)
        data=domain.read()
        bse=bs.BeautifulSoup(data, 'html.parser')
        bigp=set(bse.findall('p'))
        for p in bigp:
            lista_noticias.append()

def obt_links_primera_capa_jssup(url, selenium):
    selenium.get(url)
    selenium.implicitly_wait(10)
    biga=selenium.find_elements_by_tag_name('a')
    links=[]
    for a in biga:
        string=a.get_attribute('href')
        links.append(string)
    return links

def obt_links_internos_jssup(url,selenium, timeout=100):
    todoslinks=[] #donde irán todos los links del dominio
    i=-1    #para iterar while
    capas=[] #capas de links

    selenium.get(url)
    selenium.implicitly_wait(10)
    biga=selenium.find_elements_by_tag_name('a')
    links=[]
    for a in biga:
        string=a.get_attribute('href')
        links.append(string)
    url=url.lstrip(r"http://\S+")
    capas.append(links)
    print("links")
    print(links)
    print("capas")
    print(capas)

    tiempo_principio=time.time()

    try:
        while i < len(todoslinks):
            tiempo_pasado=time.time()-tiempo_principio
            print(tiempo_pasado)
            if tiempo_pasado>timeout:
                break
            else:
                for lista in capas:
                    for link in lista:
                        if link not in todoslinks:
                            print(link)
                            if link!=None:
                                if url in link:
                                    print(link)
                                    todoslinks.append(link)
                                    tiempo_pasado=time.time()-tiempo_principio
                                    print(tiempo_pasado)
                                    if tiempo_pasado>timeout:
                                        break
                                    else:
                                        capa=obt_links_primera_capa_jssup(link, selenium)
                                        capas.append(capa)
                i=i+1
    except:
        pass
    return todoslinks

def obtener_p_jssup(url, selenium, min_chars=10):
    selenium.get(url)
    selenium.implicitly_wait(10)
    bigp=selenium.find_elements_by_tag_name('p')

    string=""
    for p in bigp:
        if len(p.text)>min_chars:
            para=p.text
            string=string+" "+para
    return string

def obtener_p_lista_links_jssup(listaurl,selenium, min_chars=10):
    listastrings=[]
    for url in listaurl:
        selenium.get(url)
        selenium.implicitly_wait(10)
        bigp=selenium.find_elements_by_tag_name('p')

        string=""
        for p in bigp:
            if len(p.text)>min_chars:
                para=p.text
                string=string+" "+para
        listastrings.append(string)

    return listastrings
