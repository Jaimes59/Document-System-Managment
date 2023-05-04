import json
import os
from logic.classes.lease import Lease

PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class LeaseController(object):
    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'lease_storage.json')

    def add(self, lease: Lease = Lease()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['lease'].append(lease.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return lease.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object
