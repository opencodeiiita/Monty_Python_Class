import os,shutil

pathvar ='..\Monty_Python_Class\Task_2\My_Files'

names=os.listdir(pathvar)
# for x in range(0,2):
#     if not os.path.exists(path + folder_name[x]):
#         os.makedirs(path + folder_name[x])


for files in names:
    extension, ext = os.path.splitext(files)
    ext=ext[1:]
    # print(files)
    if ext=='':
        continue
    
    
    if os.path.exists((os.path.join(pathvar,ext))):
        
        shutil.move(os.path.join(pathvar,files),os.path.join(pathvar,ext,files))
    else:
        os.makedirs(os.path.join(pathvar,ext))
        shutil.move(os.path.join(pathvar,files),os.path.join(pathvar,ext,files))
       
      
  



