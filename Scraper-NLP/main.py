import bs4 as bs
import pandas as pd
from urllib import request
from selenium import webdriver
from scraper import obt_links_primera_capa
from scraper import obt_links_internos
from scraper import obtener_p
from scraper import obt_links_primera_capa_jssup
from scraper import obt_links_internos_jssup
from os import path
from multiprocessing import Manager
import multiprocessing
import time
from scraper import obtener_p_lista_links_jssup

if __name__=="__main__":
    url="http://www.latercera.com"
    addblock_path=r"/home/alonso/Escritorio/Librerias/CHROMEDRIVER_SCRAPER/extension_3_1_0_0.crx"
    chop =webdriver.ChromeOptions()
    chop.add_extension(path.abspath(addblock_path))
    selenium=webdriver.Chrome(chrome_options=chop)
    links=obt_links_internos_jssup(url, selenium, 200)
    texto=obtener_p_lista_links_jssup(links, min_chars=30, selenium=selenium)
