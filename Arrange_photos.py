from inti import*

if __name__ == "__main__":
    fm_filepath = r"C:\Users\Harru\Documents\
    Sports Interactive\Football Manager 2017\graphics\players"
    folder_list = os.listdir(fm_filepath)
    photo_list = []
    for folder in folder_list:
        face_filepath = os.path.join(fm_filepath, folder)
        if os.path.isdir(face_filepath):
            for photo in os.listdir(face_filepath):
                if photo[-3:] == 'png':
                    photo_list.append(Photo(photo, face_filepath))
    new_folder_name = []
    for j in range(50):
        current_folder_name = 'face'+str(j)
        current_folder_dir = os.path.join(fm_filepath, current_folder_name)
        new_folder_name.append(current_folder_dir)
        if not os.path.exists(current_folder_dir):
            os.mkdir(current_folder_dir)
        for i in range(20000):
            photo_list[0].move(os.path.join(current_folder_dir,
                                            photo_list[0].name))
            photo_list.pop(0)
