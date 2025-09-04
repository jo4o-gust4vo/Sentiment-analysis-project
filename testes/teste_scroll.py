from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get('https://www.selenium.dev/selenium/web/scrolling_tests/frame_with_nested_scrolling_frame_out_of_view.html')

elemento = driver.find_element(By.TAG_NAME, 'body')


driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

time.sleep(2)
scrollable_div = driver.find_element(By.TAG_NAME,'iframe')

script = '''
// Pega o primeiro elemento iframe na página
var iframe = document.getElementsByTagName("iframe")[0];

// Acessa a janela de conteúdo do iframe
var iframeWindow = iframe.contentWindow;    

// Agora, você pode obter a altura de rolagem do documento *dentro* do iframe
var y = iframeWindow.document.body.scrollHeight;

// Rola até o final do conteúdo do iframe
iframeWindow.scrollTo(0, y);


                        
                    '''


driver.execute_script(script)

#driver.execute_script("window.scrollTo(0 ,document.getElementsByClassName('iframe').scrollHeight)")