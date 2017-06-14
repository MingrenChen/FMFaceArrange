from inti import*
import os

if __name__ == "__main__":
    fm_filepath = r"C:\Users\Harru\Documents\Sports Interactive\Football Manager 2017\graphics\players"
    files = os.listdir(fm_filepath)
    folders_list = []
    photo_list = []
<<<<<<< HEAD
    i = 0
=======
>>>>>>> 7c32a925f0833e30ee75e14fb10b13c095286e56
    for folder in files:
        face_filepath = os.path.join(fm_filepath, folder)
        if os.path.isdir(face_filepath):
            folders_list.append(Folder(face_filepath))
    for f in folders_list:
        f.write_txt()
<<<<<<< HEAD
=======

>>>>>>> 7c32a925f0833e30ee75e14fb10b13c095286e56
