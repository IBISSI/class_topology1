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

if __name__=="__main__":
    top = Topology(topology_example)
    pprint(top.topology)