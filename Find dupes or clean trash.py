from Func import unloaddata,loaddata,appenddata,fetusdeletus,cleartrash,dupl

t=input('1 to find duplicate, 2 to clear trash from newfile to exportfinal: ')
if t==2:
	cleartrash('newfile.txt','exportfinal.txt')
else:
	dupl()