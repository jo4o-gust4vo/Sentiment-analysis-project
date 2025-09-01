import os
import json
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from bs4 import BeautifulSoup
import ast

load_dotenv()
#cookies = os.getenv('COOKIE_1')
#dicionarios_cookies = json.dumps(cookies)

#meu_dicionario_formatado = ast.literal_eval(cookies)

#print(type(meu_dicionario_formatado))



navegador = webdriver.Firefox()

navegador.get('https://www.instagram.com/')

for i in range(1,9):
    string = 'COOKIE_{}'.format(i)

    cookie = os.getenv(string)
    cookie_formatado = ast.literal_eval(cookie)

    navegador.add_cookie(cookie_formatado)
    

navegador.refresh()



