from pprint import pprint
from data1 import data


class Switch:
    def __init__(self, topology_dict):
        self.switch = self._normalize(topology_dict)
        for key, value in topology_dict.items():
            if key not in self.switch.keys():
                self.switch[key] = value

    def _normalize(self, topology_dict):
        normolaze_switch = {}
        for key, value in topology_dict.items():
            if key not in normolaze_switch.keys():
                normolaze_switch[key] = value
        return normolaze_switch

    def delete_switch(self, sw_name):
        if sw_name in self.switch.keys():
            del self.switch[sw_name]
        else:
            print("Такого устройства нет")

    def delete_property(self, prop_title, prop_value):
        for i in range(len(self.switch)):
            for k in self.switch.keys():
                if self.switch[k][prop_title] == prop_value:
                    del self.switch[k]
                    break

    def add_switch(self, sw_name, sw_prop):
        if not sw_name in self.switch:
            self.switch[sw_name] = sw_prop
        else:
            print("Такое устройство существует")


if __name__ == "__main__":
    top = Switch(data)
    top.add_switch("TE100-S5", {"title": "5-Port 10/100Mbps Fast Ethernet Switch",
                                "ports": "5x", "Capacity": "1Gbps", "MAC": "2k"})
    top.add_switch("TE111-S5", {"title": "5-Port 10/100Mbps Fast Ethernet Switch",
                                "ports": "5x", "Capacity": "1Gbps", "MAC": "2k"})
    pprint(top.switch)
