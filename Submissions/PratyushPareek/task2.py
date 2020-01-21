import shutil
import os

 
for folders, subfolders ,files in os.walk('D:\\Shit I made\\Monty_Python_Class\\Task_2\\My_Files\\'):
    for file in files:
        name, ext = os.path.splitext(file)
        if os.path.exists('D:\\Shit I made\\Monty_Python_Class\\Task_2\\My_Files\\'+ (ext.upper())[1:]):
            shutil.move('D:\\Shit I made\\Monty_Python_Class\\Task_2\\My_Files\\'+str(file), 'D:\\Shit I made\\Monty_Python_Class\\Task_2\\My_Files\\'+(ext.upper())[1:])
        else:
            os.mkdir('D:\\Shit I made\\Monty_Python_Class\\Task_2\\My_Files\\'+(ext.upper())[1:])
            shutil.move('D:\\Shit I made\\Monty_Python_Class\\Task_2\\My_Files\\'+str(file), 'D:\\Shit I made\\Monty_Python_Class\\Task_2\\My_Files\\'+(ext.upper())[1:])




