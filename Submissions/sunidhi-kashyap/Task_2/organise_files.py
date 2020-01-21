
import os 
import shutil 


path = r"C:\Users\hp\Desktop\Monty_Python_Class\Task_2\My_Files"


l= os.listdir(path) 

for x in l:
    n, ex = os.path.splitext(x) 

    #print(ex)	
    ex = ex[1:] 

	
    if os.path.exists(path+'/'+ex):
        shutil.move(path+'/'+x, path+'/'+ex+'/'+x) 

	
    else:
        os.makedirs(path+'/'+ex) 
        shutil.move(path+'/'+x, path+'/'+ex+'/'+x) 

