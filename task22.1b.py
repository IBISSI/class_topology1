from pprint import pprint
from data import topology_example


class Topology:
    def __init__(self, topology_dict):
        self.topology=self._normalize(topology_dict)

    def _normalize(self,topology_dict):
        normalized_topology ={}
        for box, neighbor in topology_dict.items():
            if not neighbor in normalized_topology:
                normalized_topology[box] = neighbor
        return normalized_topology

    def delete_link(self, from_port, to_port):
        if self.topology.get(from_port) ==to_port:
            del self.topology[from_port]
        elif self.topology.get(to_port) == from_port:
            del self.topology[to_port]
        else:
            print("Такого соединения нет")

if __name__=="__main__":
    top = Topology(topology_example)
    top.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))
    top.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))
    pprint(top.topology)