import json
import os
from logic.classes.administrator import Administrator


PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class AdministratorController(object):

    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'administrator_storage.json')

    def add(self, administrator: Administrator = Administrator()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['administrator'].append(administrator.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return administrator.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object
