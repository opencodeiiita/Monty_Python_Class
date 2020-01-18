import os
import shutil

rootpath=os.path.getcwd()
os.chdir(rootpath)
for folder in ['C','CPP','HTML','RAR','TXT','PDF','CSV','XLSX','XML','IMG','JPG','PNG','ODT','JAVA','JS','PY','RSS','MD','RST','GIF','RTF','SVG','DOC','DOCX','PSD','ICO','SQL']:
    os.mkdir(folder)

for filename in os.listdir():

    if '.' in filename:
        shutil.move(os.path.getcwd()+filename,os.path.getcwd()+filename.split('.')[1].upper())
