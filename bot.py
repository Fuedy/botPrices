# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from backports import csv
import io
import time


listaVendedores = ['Vendedores']
listaPrecos = []

#Define as op��es do Chrome
chrome_options = Options()
chrome_options.add_argument("--headless") #Ativa o modo sem janelas
chrome_options.add_argument("--window-size=1920x1080") #Define a resolu��o da janela
browser = webdriver.Chrome(options=chrome_options, executable_path='./chromedriver') #Inicia o browser passando as op��es e o caminho do browser

f = open("codigo.txt","r")
codigoProduto = f.read()

print("Buscando pre�os do produto: " + codigoProduto + "... Deve demorar alguns segundos")

browser.get('https://www.google.com.br/search?tbm=shop&hl=pt-BR&q='+ codigoProduto) #Navega at� a p�gina pedida
time.sleep(1)
browser.find_element_by_class_name("sh-dlr__thumbnail").click() #Procura o elemento e clica
time.sleep(1)
browser.find_element_by_class_name("_-bw").click() #Procura o elemento e clica

vendedores = browser.find_element_by_id('os-sellers-table').find_elements_by_class_name('os-seller-name') #Pega todos os nomes de vendedores e coloca num vetor
precos = browser.find_element_by_id('os-sellers-table').find_elements_by_class_name('os-price-col') #Pega todos os pre�os e coloca num vetor

#Extrai apenas os textos dos elementos
for vendedor in vendedores:
    listaVendedores.append(vendedor.text)

#Extrai apenas os textos dos elementos
for preco in precos:
    listaPrecos.append(preco.text)

#Cria o CSV com os vetores de vendedores e pre�os
with io.open(codigoProduto + '.csv', 'w', newline='', encoding='utf-8') as f:
	writer = csv.writer(f)
	for i in range(0,len(vendedores)):
		writer.writerow([listaVendedores[i], listaPrecos[i]])

print("Arquivo " + codigoProduto + ".csv criado na pasta")

#Fecha o browser
browser.close()
