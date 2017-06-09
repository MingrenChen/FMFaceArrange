import os
from inti import*


if __name__ == "__main__":
    fm_filepath = r"C:\Users\Harru\Documents\Sports Interactive\Football Manager 2017\graphics\players"
    t = open(r"C:\Users\Harru\Documents\Sports Interactive\Football Manager 2017\graphics\players\template.xml",'r')
    files = os.listdir(fm_filepath)
    folders_list = []
    photo_list = []
    for folder in files:
        face_filepath = os.path.join(fm_filepath, folder)
        if os.path.isdir(face_filepath):
            folders_list.append(Folder(face_filepath))
    for f in folders_list:
        f.creat_config()
