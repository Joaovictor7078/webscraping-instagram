# IMPORTE O SELENIUM

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# IMPORTE OUTROS

import os
import wget

''' A variavel abaixo "driver" esta usando o mudulo webdriver do selenium,
que usando o Chome, é necessario dizer que eu quero usar esse modulo para executar
o driver "executable_path" e passa o PATH do executavel em formato de str.'''

driver = webdriver.Chrome(executable_path="C:/Users/secde/chromedriver_win32/chromedriver.exe")
driver.get('https://www.instagram.com/') # usando o modulo get para acessar a página

# selecionar os campos de login
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# serve para limpar os campos, caso tiver alguma coisa digitada
username.clear() 
password.clear()

# inserindo o (usuario) e (senha)
username.send_keys("cyb311y") 
password.send_keys("cybelly@echo") 


log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click() # clickar em logar
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Agora não')]"))).click() # não salvar os dados de login
disable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Agora não')]"))).click() # não ligar as notificação

searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()
Keyword = "#cat"
searchbox.send_keys(Keyword)
searchbox.send_keys(Keys.ENTER)
