from selenium import webdriver
import time
import spacy
url="http://www.latercera.com/el-deportivo/noticia/nadal-tuve-poco-suerte-paron-la-lluvia/196026/"

selenium=webdriver.Chrome()
selenium.get(url)
selenium.set_page_load_timeout(30)
biga=selenium.find_elements_by_tag_name('a')
for a in biga:
    print(type(a.get_attribute('href')))
