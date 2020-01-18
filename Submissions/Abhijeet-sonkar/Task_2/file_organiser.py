import os,shutil
def make(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
            print ('error')    
        
files=os.scandir('My_Files/')
extension=[]
for i in files:
     a=str(i.name)
     i=a.find('.')
     if a[i+1:] not in extension:
         extension.append(a[1+i:])

for file in extension:
    make('./'+file+'/') 

files=os.scandir('My_Files/')
for i in files:
   a=str(i.name)
   y=a.find('.')
   for j in extension:
       if(a[y+1:]==j):
        source=('/home/arthas/Desktop/python/My_Files/'+i.name)
        path=('/home/arthas/Desktop/python/' +j)  
        shutil.copy(source,path)


