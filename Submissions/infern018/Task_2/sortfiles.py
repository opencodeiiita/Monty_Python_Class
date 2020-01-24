import shutil,os,re


lst=list(os.walk("../../../Task_2/My_Files"))
ptrn_to_find=r'.\w+'

from os import path

for i in lst[0][2]:
	ext=re.findall(ptrn_to_find,i)
	file=ext[1][1:].upper()

	if path.exists(file):
		shutil.move(os.path.join("..","..","..","Task_2","My_Files",i), os.path.join(os.getcwd(),file))

	else:
		os.mkdir(file)
		shutil.move(os.path.join("..","..","..","Task_2","My_Files",i), os.path.join(os.getcwd(),file))

