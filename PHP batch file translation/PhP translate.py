# https://github.com/Altair47
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from re import sub
from re import compile as rcomp
from googletrans import Translator
import sys
import os
translator = Translator()



def translatefile(tinput,toutput):
    regix=rcomp(r'\s\s+')

    tmp = open(tinput,'r',encoding="utf-8")
    f = tmp.read()
    kek=str(f)
    soup = BeautifulSoup(f, 'lxml')
    tags=sub(regix,'\n',soup.text)
    f = tags.split('\n')
    trns=[]
    trnsf=[]

    for pp in range(len(f)):
        trns=translator.translate(f[pp], dest='el')
        trnsf.append(str(trns.text))
        print(f[pp])
        print(trnsf[pp])
    print(len(f),' ',len(trnsf))
    for i in range(len(f)):
        if f[i].startswith('@'):
            continue
        kek=kek.replace(str(f[i]+'<'),str(trnsf[i]+'<'))
        kek=kek.replace(str(f[i]+' <'),str(trnsf[i]+' <'))
        kek=kek.replace(str(f[i]+'\n'),str(trnsf[i]+'\n'))
        kek=kek.replace(str(f[i]+' \n'),str(trnsf[i]+' \n'))


    bitch=open(toutput,'w',encoding="utf-8")
    bitch.write(kek)
    bitch.close()

mdr=[]

for dirs in os.listdir():
    if os.path.isdir(dirs):
        mdr.append(dirs)
for dirs in mdr:
    os.chdir(dirs)
    print(os.getcwd())
    for en in os.listdir():
        if en.endswith('en.blade.php'):
            gr=en.replace('en.blade.php','gr.blade.php')
            print(en,gr)
            translatefile(en,gr)
    os.chdir('..')