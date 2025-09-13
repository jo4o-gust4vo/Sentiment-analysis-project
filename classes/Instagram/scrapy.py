from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

        
class Scrape:
    def __init__(self):
        pass

    @classmethod    
    def Scraping(cls, objeto_navegador):
        siteHtml = BeautifulSoup(objeto_navegador.page_source,'html.parser')

        
        
        objeto_navegador.quit()

        return siteHtml

    @classmethod
    def get_comments(cls, html):
        '''
            retorna uma lista com os comentários do post do instagram
        '''
        comments = html.find_all('span','x1lliihq x1plvlek xryxfnj x1n2onr6 xyejjpt x15dsfln x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xl565be xo1l8bm x5n08af x10wh9bi xpm28yp x8viiok x1o7cslx')
        list_comments = []
        for comment in comments:
          #  print(comment.text.strip()) 
            list_comments.append(comment.text.strip())

        return list_comments
    
    @classmethod
    def scroll_comments(cls,driver):
        script = '''
            // Pega o primeiro elemento iframe na página
            var iframe = document.getElementsByClassName("x5yr21d xw2csxc x1odjw0f x1n2onr6")[0];
            var y = iframe.scrollHeight;
            iframe.scrollTo(0,y)
                '''
        height_script = '''
            iframe = document.getElementsByClassName("x5yr21d xw2csxc x1odjw0f x1n2onr6")[0];
            return iframe.scrollHeight;
                        
                        '''
        

        height = driver.execute_script(height_script)
        while True:
            #time.sleep(3)
            height = driver.execute_script(height_script)
            driver.execute_script(script)
            time.sleep(10)
            height_new = '''
            iframe = document.getElementsByClassName("x5yr21d xw2csxc x1odjw0f x1n2onr6")[0];
            return iframe.scrollHeight;     
            '''

            if height == driver.execute_script(height_new):
                print('Scrollado com sucesso!')
                break
            
       
       
       
       


 