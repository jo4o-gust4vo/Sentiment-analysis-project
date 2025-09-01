import os
import json
from dotenv import load_dotenv
from selenium import webdriver
import ast
import time



class Login:
    load_dotenv()
    def __init__(self):
        pass

    @classmethod    
    def inicializarNavegador(cls, url):
        navegador = webdriver.Firefox()
        navegador.get(url)

        for i in range(1,9):
            string = 'COOKIE_{}'.format(i)

            cookie = os.getenv(string)
            cookie_formatado = ast.literal_eval(cookie)

            navegador.add_cookie(cookie_formatado)
        
        
        navegador.refresh()
        time.sleep(3)

        return navegador