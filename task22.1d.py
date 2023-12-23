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

    def delete_node(self, node):
        original_size = len(self.topology)
        for src, dest in list(self.topology.items()):
            if node in src or node in dest:
                del self.topology[src]
        if original_size == len(self.topology):
            print("Такого устройства нет")

    def add_link(self, src, dest):
        keys_and_values= set(self.topology.keys() | set(self.topology.values()))
        if self.topology.get(src) == dest or self.topology.get(dest) ==src:
            print("Такое соединение существует")
        elif src in keys_and_values or dest in keys_and_values:
            print("Соединение с одним из портов существует")
        else:
            self.topology[src]=dest


if __name__=="__main__":
    top = Topology(topology_example)
    top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
    pprint(top.topology)