from PIL import Image
import pickle
import os
import shutil


class Photo:
    """
    init a png file for fm players.
    """
    def __init__(self, name, path, width=0, height=0):
        self.id_ = name[:-4]
        self.name = name
        self.path = path
        self.real_dir = os.path.join(path, name)
        if width != 0:
            with Image.open(self.real_dir) as img:
                self.width, self.height = img.size
        else:
            self.width = width
            self.height = height
        with Image.open(self.real_dir) as img:
            self.width, self.height = img.size

    def __repr__(self):
        return self.name

    def move(self, new_real_dir):
        """
        move current photo to another folder.
        """
        shutil.move(self.real_dir, new_real_dir)
        self.real_dir = new_real_dir

    def __eq__(self, other):
        if self.id_ == other.id:
            return self.width == other.width and self.height == other.height

    def absorb(self, photo):
        """
        move a photo to it's origin and delete the older one.
        :param photo:Photo
        :type photo:Photo
        :return:None
        :rtype:None
        """
        if os.path.getctime(self.real_dir) < os.path.getctime(photo.real_dir):
            pass
        else:
            shutil.move(photo.real_dir, self.real_dir)


class Folder:
    """
    init a folder contains fm players' photo.
    """
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.file = []
        self.num = 0
        if "config.p" not in os.listdir(path):
            for file in os.listdir(path):
                if file[-3:] == 'png':
                    self.file.append(Photo(file, path))
                    self.num += 1
            save = open(os.path.join(self.path, 'config.p'), 'wb')
            pickle.dump(self.file, save)
            save.close()
        else:
            save = open(os.path.join(self.path, 'config.p'), 'rb')
            self.file = pickle.load(save)
            save.close()

    def __repr__(self):
        return self.name

    def creat_config(self):
        """
        create config file for each folder under main folder.
        """
        c = os.path.join(self.path, 'config.xml')
        config = open(c, 'w')
        for i in ['<record>\n', '\t<!-- resource manager options -->\n',
                  '\n', '\t<!-- dont preload anything in this folder -->\n',
                  '\t<boolean id="preload" value="false"/>\n', '\n',
                  '\t<!-- turn off auto mapping -->\n',
                  '\t<boolean id="amap" value="false"/>\n', '\n',
                  '\t<!-- logo mappings -->\n', '\t<!-- the following XML maps '
                                                'pictures inside this folder '
                                                'into other positions\n',
                  '\t\t\t in the resource system, which allows this folder to'
                  ' be dropped into any\n', '\t\t\t place in the graphics '
                                            'folder and still have the'
                                            ' game pick up the graphics\n',
                  '\t\t\t files from the correct places\n',
                  '\t-->\n', '\n', '\t<list id="maps">\n',
                  '\t\t<!-- Auto generated by Mingren Chen -->\n']:
            config.writelines(i)
        for photo in self.file:
            write_stuff = '\t\t<record from="0" to="graphics' \
                          '/pictures/person/0/portrait"/>\n'
            write_list = write_stuff.split("/")
            write_list[-3] = photo.id_
            write_stuff = '/'.join(write_list)
            write_list = write_stuff.split("\"")
            write_list[1] = photo.id_
            config.writelines('\"'.join(write_list))
        config.writelines('/'.join(['\t</list>\n', '</record>']))
        config.close()

    def include(self, photo):
        """
        return if a photo is in the folder.
        :param photo: a photo's name
        :type photo: Photo
        :return: None
        :rtype: None
        """
        if photo in self.file:
            return True
        return False
