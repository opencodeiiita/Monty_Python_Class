
import os,shutil
   

main_file = '../../../Task_2/My_Files'
  
  

new = os.listdir(main_file) 
   
 
for extension in new: 
    name, ext = os.main_file.splitext(extension) 
  
 
    ext = ext[1:] 
  

    if ext == '': 
        continue
  

    if os.main_file.exists(main_file+'/'+ext): 
       shutil.move(main_file+'/'+extension, main_file+'/'+ext+'/'+extension) 
  

    else: 
        os.makedirs(main_file+'/'+ext) 
        shutil.move(main_file+'/'+extension, main_file+'/'+ext+'/'+extension) 




