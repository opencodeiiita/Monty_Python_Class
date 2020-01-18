import os,sys,shutil
def make(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
            print ('error') 
x=sys.argv[1]
y=os.listdir(x)
extension=[]
for i in y:
     p=i.find('.')
     if i[p+1:] not in extension:
         extension.append(i[1+p:]) 

for file in extension:
    make('./'+x+'/'+file+'/')              
for i in y:
   p=i.find('.')
   for j in extension:
       if(i[p+1:]==j):
        source=('./'+x+'/'+i)
        path=('./'+x+'/' +j+'/')  
        shutil.move(source, path)