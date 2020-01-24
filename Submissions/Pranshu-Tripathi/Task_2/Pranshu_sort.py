import os,shutil
path="../../../Task_2/My_Files"
entries=os.listdir(path)
for entry in entries:
    filename,file_extension=os.path.splitext(entry)
    file_extension=file_extension[1:]
    if os.path.exists(os.path.join(path,file_extension)):
        shutil.copy(os.path.join(path,entry),os.path.join(path,file_extension))
    else:
        try:
            Real_Path=path+"/"+file_extension
            os.makedirs(Real_Path)
            shutil.copy(os.path.join(path,entry),os.path.join(path,file_extension))
        except OSError:
            print("Moving file failed")
        else:
            print("Moved Succesfully",path)
        shutil.copy(os.path.join(path,entry),os.path.join(path,file_extension))
for entry in entries:
    Remove_file_path="../../../Task_2/My_Files"+"/"+entry
    os.remove(Remove_file_path)

