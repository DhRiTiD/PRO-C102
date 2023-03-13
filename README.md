# PRO-C102
---
. . . .

## project - Automatic File Segregation C102 with whjr
- in this class the concept of `os` & `shutil` was introduced
- in this class we created a simple automatic segregation system to move items from the given path to the provided destination 
- used `os.path.exists(path)` to check the existance of a certain path
- used `os.listdir(path)` to check the list of directorties in the given path
- used `os.path.splitext(path)` to split the given path into `root` and `extention`
- used `shutil.move(path1, path3)` to move the item permanently from path1 to path3
- used `os.makedirs(path2)` to create the directory when required

## class project
- the project was updated to a better version to accomodate moving files of more than one type from a single file
- also now the `from` destination can be chosen from anywhere in the DOWNLOADS folder
- and the `to` destination can be chosen from anywhere in the DESKTOP folder
- expected output :

    ![image](https://user-images.githubusercontent.com/74966124/224760835-c47c572f-a37e-4f0a-ae35-9fd57d1d2aac.png)
