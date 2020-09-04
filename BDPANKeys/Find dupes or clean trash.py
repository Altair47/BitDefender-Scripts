from Func import unloaddata,loaddata,appenddata,fetusdeletus,cleartrash,dupl,cleartrash2


#cleartrash2('Export.txt','exportfinal.txt')

f=loaddata('2exportactiv.txt',0)
k=loaddata('keystest.txt',0)
list_dif = [i for i in k + f if i not in k or i not in f]
print (list_dif)
#with sets
#c=list()
#c=(list(set(k) - set(f))) 
unloaddata('newnew.txt',list_dif,0)