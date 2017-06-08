import inti
import os



if __name__ == "__main__":
    fm_filepath = r"C:\Users\Harru\Documents\Sports Interactive\Football Manager 2017\graphics\players"
    t = open(r"C:\Users\Harru\Documents\Sports Interactive\Football Manager 2017\graphics\players\template.xml",'r')
    folder_list = os.listdir(fm_filepath)
    photo_list = []
    for folder in folder_list:
        face_filepath = os.path.join(fm_filepath, folder)
        for photo in os.listdir(face_filepath):
            if photo[-3:] == 'png':
                photo_list.append(Photo(photo,face_filepath))
    template_list = t.readlines()
    line = template_list[18].split('/')