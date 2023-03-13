import os
import shutil

import time

#choice of destination
initial = input('from where in DOWNLOADS do you want to move items?')
final = input('to where on DESKTOP do you want to move the items?')

from_dir='c:/Users/Dell/Downloads/' + initial 
to_dir='c:/Users/Dell/OneDrive/Desktop/' + final

#choice of file type
print('''-images
-docs
-mp3
-mp4
-all''')

file_type = input('enter file type from the above choices:')

if file_type == 'images':
    ext_list = ['.gif', '.png', '.jpg', '.jpeg','.jfif']
elif file_type == 'docs':
    ext_list = ['.txt', '.pdf', '.doc', '.docx', '.md', '.py', '.xlsx']
elif file_type == 'mp3':
    ext_list = ['.mp3']
elif file_type == 'mp4':
    ext_list = ['.mp4']
elif file_type == 'all':
    ext_list = ['.gif', '.png', '.jpg', '.jpeg','.jfif', '.txt', '.pdf', '.doc', '.docx', '.mp3', '.mp4']


list_of_items = os.listdir(from_dir)

for item in list_of_items:

    root, ext = os.path.splitext(item)
    #print('root and ext: ', root, ',' , ext)

    if ext in ext_list:

        path1 = from_dir + '/' + item
        path2 = to_dir + '/' + file_type
        path3 = to_dir + '/' + file_type + '/' + item
    
        if os.path.exists(path2):
            print('moving',item,'....')
            time.sleep(2)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print('path created')

            print('moving',item,'....')
            time.sleep(2)
            shutil.move(path1, path3)

print('all items moved successfully!!')