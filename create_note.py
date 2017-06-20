from inti import*
import os
import time

if __name__ == "__main__":
    fm_filepath = r"C:\Users\Harru\Documents\Sports Interactive\Football Manager 2017\graphics\players"
    wait = r"C:\Users\Harru\Documents\Sports Interactive\Football Manager 2017\graphics\wait"
    files = os.listdir(fm_filepath)
    folders_list = []
    photo_list = []
    i = 0
    start = time.time()
    for folder in files:
        face_filepath = os.path.join(fm_filepath, folder)
        if os.path.isdir(face_filepath):
            folders_list.append(Folder(face_filepath))
    waited_folder = os.listdir(wait)
    for photo in waited_folder:
        for f in folders_list:
            if f.include(Photo(photo, waited_folder)):
                pass

    print(time.time() - start)
