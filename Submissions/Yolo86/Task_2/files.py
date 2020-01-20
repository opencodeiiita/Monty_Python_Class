import os
import shutil

os.chdir('../../../Task_2/My_Files/')
b = os.getcwd()

for fi in os.listdir():
	try:
		fna,fext = fi.split('.')
		if os.path.exists(b+'/'+fext):
			shutil.move(b+'/'+fi,b+'/'+fext+'/'+fi)
		else:
			os.makedirs(b+'/'+fext)
			shutil.move(b+'/'+fi,b+'/'+fext+'/'+fi)
	except ValueError:
		continue