import json
import os
from logic.classes.address import Address


PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class AddressController(object):

    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'address_storage.json')

    def add(self, address: Address = Address()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['address'].append(address.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return address.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object
