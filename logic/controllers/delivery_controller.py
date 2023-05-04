import json
import os
from logic.classes.delivery import Delivery

PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class DeliveryController(object):
    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'delivery_storage.json')

    def add(self, delivery: Delivery = Delivery()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['delivery'].append(delivery.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return delivery.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object
