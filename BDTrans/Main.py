from selenium import webdriver
import time
from bs4 import BeautifulSoup
from config import *
from googletrans import Translator
#Engage Driver
driver = webdriver.Chrome()
#Translator
translator = Translator()

#Logging in
time.sleep(1)
fpage=input("Input site to start: ")
driver.get(fpage)
print(driver.current_url)
print(driver.title)

driver.find_element_by_id('id_username').send_keys(DATACOUP_USERNAME)
driver.find_element_by_id('id_password').send_keys(DATACOUP_PASSWORD)
driver.find_element_by_xpath('//*[@id="login-form"]/form/div[3]/button').click()

#Items to ignore: <#ProductName#>,[Product],

while 1:
	txttr=driver.find_element_by_id('id_rawsource').get_property("value");
	print('+Source: ',txttr)

	trns=translator.translate(txttr, dest='el')
	trnsf=trns.text

	print('=Translated: ',trnsf)
	driver.find_element_by_id('id_translation').clear()
	driver.find_element_by_id('id_translation').send_keys(trnsf)

	x=input('Press any key continue. Type N/n to stop.')
	if x=='N' or x=='n': break

	driver.find_element_by_xpath('//*[@id="pagecontent"]/div[1]/div/form/div[2]/button[1]').click()