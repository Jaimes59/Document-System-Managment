import json
import os
from logic.classes.fdoc import Fdoc

PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class FdocController(object):
    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'fdoc_storage.json')

    def add(self, fdoc: Fdoc = Fdoc()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['fdoc'].append(fdoc.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return fdoc.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object
