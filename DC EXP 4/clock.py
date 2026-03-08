import random

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        # each node starts with a slightly different clock
        self.clock = random.randint(0, 100)

    def get_time(self):
        return self.clock

    def adjust_time(self, offset):
        self.clock += offset


class BerkeleyAlgorithm:

    def __init__(self, num_nodes):
        self.master = Node("Master")
        self.nodes = [Node(i) for i in range(num_nodes)]

    def show_clocks(self):
        print("\nCurrent Clock Times")
        print("Master Clock:", self.master.get_time())
        for node in self.nodes:
            print(f"Node {node.node_id} Clock:", node.get_time())

    def synchronize(self):

        print("\nSynchronizing Clocks...\n")

        times = []

        master_time = self.master.get_time()
        times.append(master_time)

        for node in self.nodes:
            times.append(node.get_time())

        avg_time = sum(times) / len(times)

        print("Average Time Calculated:", avg_time)

        master_offset = avg_time - self.master.get_time()
        self.master.adjust_time(master_offset)

        for node in self.nodes:
            offset = avg_time - node.get_time()
            node.adjust_time(offset)


# MAIN PROGRAM

num_nodes = 4
system = BerkeleyAlgorithm(num_nodes)

print("Before Synchronization")
system.show_clocks()

system.synchronize()

print("\nAfter Synchronization")
system.show_clocks()