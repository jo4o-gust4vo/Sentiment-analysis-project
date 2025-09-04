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
from classes.login import Login
from classes.scrapy import Scrape



#Login.inicializarNavegador('https://www.instagram.com/p/DNgZkDXuFmZ/')
login = Login.inicializarNavegador('https://www.instagram.com/p/DNgZkDXuFmZ/')

Scrape.scroll_comments(login)

html_page = Scrape.Scraping(login)

list_comments = Scrape.get_comments(html_page)

for comment in list_comments:
   print(comment)