from selenium import webdriver
import time
from bs4 import BeautifulSoup
from config import *
from googletrans import Translator
import sys
#Engage Driver
driver = webdriver.Chrome()
#Translator
translator = Translator()

#Logging in
time.sleep(1)
fpage=input("Input entry to start: ")
driver.get(fpage)
print(driver.current_url)
print(driver.title)

driver.find_element_by_id('id_username').send_keys(DATACOUP_USERNAME)
driver.find_element_by_id('id_password').send_keys(DATACOUP_PASSWORD)
driver.find_element_by_xpath('//*[@id="login-form"]/form/div[3]/button').click()

#Items to ignore: <#ProductName#>,[Product],

while 1:
	try:
		txttr=driver.find_element_by_id('id_rawsource').get_property("value");
		print('+Source: ',txttr)
	
		trns=translator.translate(txttr, dest='el')
		trnsf=trns.text

		a_dict = {
			'[Προϊόν]': '​[Product]​',
			'[Κεντρική]':'​[Central]​',
			'<a> <b> <c /> </b> </a>':'​​<a>​ ​<b>​ ​<c/>​ ​</b>​ ​</a>',
			'<b> <c> <d /> </c> </b>':'​​<b> <c> <d/> </c> </b>',
			'{ημερομηνία}':'​​{date}',
			'\"{info}\"':'​​\'​{info}\'',
			'{{factory_name}}':'​​{{manufacturer_​name}}',
			'\ n':'\\n',
			'<span class = "text-primer"> {{phone}} </span>':'<span class="text-primary">​{{phone}}​</span>​',
			'<span class = "text-primer nowrap"> {{phone}} </span>':'<span class="text-primary nowrap">​{{phone}}​</span>',
			'<span class = "text-primer"> {{number}} </span>':'<span class="text-primary">​{{number}}​</span>​',
			'</ p >','</p>'}
		
		driver.find_element_by_id('id_translation').clear()
		#trnsf=trnsf.replace('[Προϊόν]','​[Product]​')
		#trnsf=trnsf.replace('[Κεντρική]','​[Central]​')
		#trnsf=trnsf.replace('<a> <b> <c /> </b> </a>','​​<a>​ ​<b>​ ​<c/>​ ​</b>​ ​</a>')
		#trnsf=trnsf.replace('<b> <c> <d /> </c> </b>','​​<b> <c> <d/> </c> </b>')
		#trnsf=trnsf.replace('{ημερομηνία}','​​{date}')
		#trnsf=trnsf.replace('\"{info}\"','​​\'​{info}\'')
		#trnsf=trnsf.replace('{{factory_name}}','​​{{manufacturer_​name}}')
		#trnsf=trnsf.replace('\ n','\\n')
		for key in a_dict:
			trnsf=trnsf.replace(str(key),str(a_dict[key]))
		print('=Translated: ',trnsf)

		driver.find_element_by_id('id_translation').send_keys(trnsf)
	
		x=input('Press any key continue. Type N/n to stop.')
		if x=='N' or x=='n': break
	
		driver.find_element_by_xpath('//*[@id="pagecontent"]/div[1]/div/form/div[2]/button[1]').click()
	except:
		print("End of the line.\n", sys.exc_info()[0], "occurred.")
		fpage=input("Input n/N o stop or input another entry to start: ")
		if fpage=='N' or fpage=='n': break
		driver.get(fpage)