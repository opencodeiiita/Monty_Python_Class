import os, shutil

# path = "C:/Users/Aaryan/Desktop/Inconspicuous Folder/IT/Python/lol"

# try:
# 	os.mkdir(path)
# except OSError:
# 	print("Creation of the directory %s failed." %path)
# else:
# 	print("Successfully created the directory %s." %path)

entries = os.listdir('../../../Task_2/My_Files')

for entry in entries:
	# print(entry)
	file_name,file_extension = os.path.splitext('../../../Task_2/My_Files/%s' %entry)
	# print(file_extension)
	if os.path.exists("../../../Task_2/My_Files/%s" %str(file_extension)[1:]):
		shutil.move("../../../Task_2/My_Files/%s" %entry, "../../../Task_2/My_Files/%s" %str(file_extension)[1:])
	else:
		path = "../../../Task_2/My_Files/%s" %str(file_extension[1:])
		try:
			os.mkdir(path)
		# except OSError:
		# 	print("Creation of the directory %s failed." %path)
		# else:
		# 	print("Successfully created the directory %s." %path)
		shutil.move("../../../Task_2/My_Files/%s" %entry, "../../../Task_2/My_Files/%s" %str(file_extension)[1:])



