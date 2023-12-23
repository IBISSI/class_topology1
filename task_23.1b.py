from pprint import pprint
from data1 import data


class Switch:
    def __init__(self, topology_dict):
        self.switch=self._normalize(topology_dict)
        for key, value in topology_dict.items():
            if key not in self.switch.keys():
                self.switch[key]= value

    def _normalize(self,topology_dict):
        normolaze_switch ={}
        for key, value in topology_dict.items():
            if key not in normolaze_switch.keys():
                normolaze_switch[key]= value
        return normolaze_switch

    def delete_switch(self, sw_name):
        if sw_name in self.switch.keys():
            del self.switch[sw_name]
        else:
            print("Такого устройства нет")

if __name__=="__main__":
    top = Switch(data)
    top.delete_switch('TE100-S8')
    top.delete_switch('TE200-S8')
    pprint(top.switch)
