import json
import os
from logic.classes.magazine import Magazine

PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class MagazineController(object):
    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'magazine_storage.json')

    def add(self, magazine: Magazine = Magazine()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['magazine'].append(magazine.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return magazine.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object
