import json
import os
from logic.classes.fdelivery import FDelivery

PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class FdeliveryController(object):
    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'fdelivery_storage.json')

    def add(self, fdelivery: FDelivery = FDelivery()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['fdelivery'].append(fdelivery.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return fdelivery.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object
