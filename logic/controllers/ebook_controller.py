import json
import os
from logic.classes.ebook import Ebook

PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)

class EBookController(object):
    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'ebook_storage.json')

    def add(self, ebook: Ebook = Ebook()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['ebook'].append(ebook.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return ebook.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object
