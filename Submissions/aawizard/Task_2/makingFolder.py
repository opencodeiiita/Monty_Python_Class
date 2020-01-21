import os,shutil

path ='..\Monty_Python_Class\Task_2\My_Files'
pathfinal =r'..\Monty_Python_Class\Submissions\aawizard\Task_2'
names=os.listdir(path)
# for x in range(0,2):
#     if not os.path.exists(path + folder_name[x]):
#         os.makedirs(path + folder_name[x])


for files in names:
    extension, ext = os.path.splitext(files)
    ext=ext[1:]
    # print(files)
    if ext=='':
        continue
    
    
    if os.path.exists(pathfinal+'/'+ext):
        
        shutil.move(path+'/'+files,pathfinal+'/'+ext+'/'+files)
    else:
        os.makedirs(pathfinal+'/'+ext)
        shutil.move(path+'/'+files,pathfinal+'/'+ext+'/'+files)
       
    #    shutil.move(path+'/'+files,path2+'/'+ext+'/'+files)    
  



