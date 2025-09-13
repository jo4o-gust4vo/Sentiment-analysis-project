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
from classes.Instagram.login import Login
from classes.Instagram.scrapy import Scrape
from classes.process.pnl import Pnl
from classes.visualization.plot_word_cloud import Plot_word_cloud
from classes.visualization.plot_bar import Plot_bar
from classes.process.analyze_sentiment  import Analyzer
from pathlib import Path

ROOT_PATH = Path(__file__).parent

#login = Login.inicializarNavegador('https://www.instagram.com/p/DOfFca2jP5W/')

#Scrape.scroll_comments(login)

#html_page = Scrape.Scraping(login)

#list_comments = Scrape.get_comments(html_page)

#for comment in list_comments:
#   print(comment)


#with open(ROOT_PATH / 'database' / 'comentarios.csv', 'w',encoding='utf-8') as arquivo:
      
   #   for comment in list_comments:
   #      arquivo.write(comment+'\n')


df = Pnl.get_comment('comentarios.csv')
#Plot_bar.plot(df)
Plot_word_cloud.plot(Pnl.apply_stop_word(df))

#Plot_word_cloud.plot(Pnl.apply_stop_word(df))


#time.sleep(3)

#Plot_bar.plot(df)
