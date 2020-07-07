from bs4 import BeautifulSoup

def loaddata(k,f):
	tmp = open(k,'r')
	f = tmp.readlines() #Imported in a list
	tmp.close()
	if f==1:
		for i in range(len(f)):
			f[i]=f[i].strip('\n')
	return f

'''print(f)
tmp = open('file.txt','a')
tmp.writelines(f)
tmp.close()'''

def unloaddata(j,f,k):
	with open(j, 'w') as tmp:
		if k == 1:
			for item in f:
				tmp.write("%s\n" % item)
		else:
			for item in f:
				tmp.write(item)
	print("Finished exporting data to: ",j)

def appenddata(f):
	tmp = open('appended.txt','a+')
	for item in f:
				tmp.write("%s\n" % item)
	tmp.close()


def fetusdeletus(f,k):
	bannedbois = [' ','@bitdefender.com','@bluesoft.gr','class=']
	with open(f) as oldfile, open(k, 'w') as newfile:
		for line in oldfile:
			if not any(bannedbois in line for bannedbois in bannedbois):
				newfile.write(line)

def cleartrash(f,j):
	tmp = open(f,'r')
	k = tmp.readlines() #Imported in a list
	tmp.close()
	
	for i in range(len(k)):
		k[i]=k[i].replace('<td>','')
	for i in range(len(k)):
		k[i]=k[i].replace('</td>','')
		print(k[i])
	unloaddata(j,k,0)

def dupl():
	f=loaddata('keystest.txt',0)
	k=list()
	if len(f) == len(set(f)):
		print("No Duplicate")
	else:
		print("Yes there are duplicates:")
	for i in range(len(f)):
		for j in range(i+1,len(f)):
			if f[i]==f[j]:
				print(f[i])
				k.append(f[i])
				k.append(i+1)
	return(k)

#Shorting techniques
'''
tmp = open('keystest.txt','r')
k = tmp.readlines() #Imported in a list
tmp.close()

kk=k
stor=list()
print(len(k))
print(len(k[0]))
print(isinstance(k, list))
temp=list()
i=0
for ele in kk: 
	if len(ele) < 11 and ele!=kk[-1]:
		stor.append(kk.index(ele)+i)
		kk.remove(ele)
		i=+1
print(stor)

i=0

while i < len(kk):
	temp.append(kk[i])
	if (i%10 == 9) or (i == len(kk)-1):
		print (temp)
		del temp[:]
	i+=1'''

'''print(kk)
print(stor)

for i in stor:
	kk[i] = 'kekw'
print(kk)
kk.extend(k)
mylist = list(dict.fromkeys(kk))
print(mylist)
print('----')
print(kk)
#-------------------
i=0
while i < len(kk):
	if i%10 == 0 or i == len(kk):
		print('----')
	print(kk[i])
	i+=1'''