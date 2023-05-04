import json
import os
from logic.classes.sell import Sell

PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class SellController(object):
    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'sell_storage.json')

    def add(self, sell: Sell = Sell()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['sell'].append(sell.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return sell.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object
