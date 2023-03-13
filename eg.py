import os
import shutil

import time

os.getcwd() # to find the dir we are currently working in

path = 'C:/Users/Dell/OneDrive/Desktop/pthon whjr/C102_automatic_file_segregation/organizer.py'

#checking the existance of the path entered
is_exists = os.path.exists(path)
print(is_exists)

#splitting the text to root and extention and displaying the same
root, ext = os.path.splitext(path)
print('root: ', root)
print('extention: ', ext)

#printing list of files and folders inside the given path
#print(os.listdir(path)) 
#only works if the given path is that of a folder
