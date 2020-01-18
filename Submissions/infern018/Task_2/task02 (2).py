import os
import shutil

rootpath='C:\\Users\\lenovo-\\Desktop\\opencode_projects\\Monty_Python_Class\\Task_2\\My_Files\\'
os.chdir(rootpath)
for folder in ['C','CPP','HTML','RAR','TXT','PDF','CSV','XLSX','XML','IMG','JPG','PNG','ODT','JAVA','JS','PY','RSS','MD','RST','GIF','RTF','SVG','DOC','DOCX','PSD','ICO','SQL']:
    os.mkdir(folder)

for filename in os.listdir():

    if '.' in filename:
        shutil.move('C:\\Users\\lenovo-\\Desktop\\opencode_projects\\Monty_Python_Class\\Task_2\\My_Files\\'+filename,'C:\\Users\\lenovo-\\opencode_projects\\Monty_Python_Class\\Task_2\\My_Files\\'+filename.split('.')[1].upper())
