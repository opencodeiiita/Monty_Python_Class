import os, shutil
path = 'C:/Users/Aaryan/Desktop/Inconspicuous Folder/FOSS/Monty_Python_Class/Task_2/My_Files'
entries = os.listdir(path)
for entry in entries:
	file_name,file_extension = os.path.splitext(entry)
	file_extension = file_extension[1:]
	if os.path.exists(os.path.join(path,file_extension)):
		shutil.move(os.path.join(path,entry), os.path.join(path,file_extension))
	else:
		try:
			os.mkdir(path)
		except OSError:
			print("Creation of the directory %s failed." %path)
		else:
			print("Successfully created the directory %s." %path)
		shutil.move(os.path.join(path,entry), os.path.join(path,file_extension))



