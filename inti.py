from PIL import Image
import os
import shutil

class Photo:
    def __init__(self, name, path):
        self.id_ = name[:-4]
        self.name = name
        self.path = path
        self.real_dir = os.path.join(path,name)
    def __repr__(self):
        return self.name
    def move(self, new_real_dir):
        shutil.move(self.real_dir,new_real_dir)
        self.real_dir = new_real_dir



fm_filepath = r"C:\Users\Harru\Documents\Sports Interactive\Football Manager 2017\graphics\players"
folder_list = os.listdir(fm_filepath)
photo_list = []
for folder in folder_list:
    face_filepath = os.path.join(fm_filepath, folder)
    for photo in os.listdir(face_filepath):
        photo_list.append(Photo(photo,face_filepath))

new_folder_name = []
for j in range(50):
    current_folder_name = 'newface'+str(j)
    current_folder_dir = os.path.join(fm_filepath,current_folder_name)
    new_folder_name.append(current_folder_dir)
    if not os.path.exists(current_folder_dir):
        os.mkdir(current_folder_dir)
    for i in range(20000):
        photo_list[0].move(os.path.join(current_folder_dir,photo_list[0].name))
        photo_list.pop(0)
        
        

# with Image.open(fm_filepath) as img:
#     width, height = img.size
