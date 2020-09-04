from selenium import webdriver
import time
from bs4 import BeautifulSoup
from config import *
from Func import unloaddata,loaddata,appenddata,fetusdeletus,cleartrash,dupl,cleartrash2

#Engage Driver
driver = webdriver.Chrome()


#Logging in
driver.get('https://pan.bitdefender.com/login')
print(driver.current_url)
print(driver.title)


driver.find_element_by_id('UserLogin').send_keys(DATACOUP_USERNAME)
driver.find_element_by_id('UserPasswd').send_keys(DATACOUP_PASSWORD)
driver.find_element_by_xpath('//*[@id="UserLoginForm"]/div[3]/input').click()

#Searching keys


f=loaddata('keystest.txt',0)

ff=list() #temp key list
tlist=list() #temp name list
names=list()
stor=list()
storg=list()
driver.get('https://pan.bitdefender.com/Keys/unified_search')
#Remove company generated keys from loaddata

'''i=0
for ele in f: 
	if len(ele) < 11 and ele!=f[-1]:
		stor.append(f.index(ele)+i)
		storg.append(ele)
		f.remove(ele)
		i=+1
print("---Comp Gen Keys---")
print(storg)
print(stor)
print("------\n")'''

#Give keys in a 10 size list and clear it each 10 loops

i=0
while i < len(f):
	ff.append(f[i])#appends key from 'f' list to temporary 'ff' list
	#if loop ever 10 tries (to gather 10 keys), mod10==9 cause lists start at 0
	if (i%10 == 9) or (i == len(f)-1) or (len(f[i+1]) < 11):
		driver.find_element_by_id('KeysKey').clear()
		driver.find_element_by_id('KeysKey').send_keys(ff)
		driver.find_element_by_xpath('//*[@id="KeysUnifiedSearchForm"]/div[2]/input').click() #Submit
		html = driver.page_source
		soup = BeautifulSoup(html, 'html.parser')
		tags = soup.find_all('td')
		activs = soup.find_all('span')
		for activ in activs:
			if "is not activated" in activ.text: tlist.append(activ)
		for tag in tags:
			if "@" in tag.text:	tlist.append(tag)
		tlist = list(tlist)
		names.extend(tlist)
		appenddata(tlist)

		#if (len(tlist)>10) or (len(tlist)>10):
		print('---1---')
		print(ff) #Keys gathered on temp list
		print('Number of Keys entered ',len(ff))
		print('---2---')
		print(tlist)
		print('Number of Names scavenged ',len(tlist))
		print('---3---\n')

		del tlist[:] #Clear List
		del ff[:]
		time.sleep(5)
	i+=1
appenddata('----End----\n')
print(ff)
print(names)
unloaddata('export.txt',names,1)
cleartrash2('export.txt','exportactiv.txt')
fetusdeletus('export.txt','newfile.txt')
cleartrash('newfile.txt','exportfinal.txt')
print(dupl())

driver.quit()