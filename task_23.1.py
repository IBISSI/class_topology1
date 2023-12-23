from pprint import pprint
from data1 import data


class Switch:
    def __init__(self, topology_dict):
        self.switch={}
        for key, value in topology_dict.items():
            if key not in self.switch.keys():
                self.switch[key]= value


if __name__=="__main__":
    top = Switch(data)
    pprint(top.switch)