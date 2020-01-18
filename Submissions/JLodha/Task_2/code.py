import os 
import shutil 

source = './My_Files'

data = os.listdir(source) 

for entry in data: 
    name, l = os.path.splitext(entry) 

    l = l[1:] 

    if l == '': 
        continue

    if os.path.exists(source+'/'+l): 
       shutil.move(source+'/'+entry, source+'/'+l+'/'+entry) 

    else: 
        os.makedirs(source+'/'+l) 
        shutil.move(source+'/'+entry, source+'/'+l+'/'+entry) 