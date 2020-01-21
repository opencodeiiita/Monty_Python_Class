

import os 
  
import shutil 
  
 
os.chdir(os.getcwd()) 
cwd = os.getcwd() 
   
  
l = [f for f in os.listdir(cwd) if os.path.isfile(f)]  
l2 = [] 
   
  
for  value in l: 
    s = value.split('.')[1]  
    l2.append(s) 
print(l, l2) 
  
for extension in set(l2): 
    dirname = extension  
    if os.path.exists(cwd+"\\"+extension): 
        pass
    else: 
        os.makedirs(dirname)  
  
for files, extension in zip(l, l2): 
    if extension in files: 
        if os.path.exists(cwd+"\\"+extension+"\\"+files): 
            pass
        else: 
            shutil.move(cwd+"\\"+files, cwd+"\\"+extension) 
        print(extension, files) 
    else : 
        print('error') 

