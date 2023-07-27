from queue import Queue


class Node:
    def __init__(self, interval, left=None, right=None):
        self.interval = interval
        self.data = []
        self.left = left
        self.right = right

class IntervalTree:
    def __init__(self, tab):
        self.root = None
        self.tab = tab

    def make_tree(self):
        leaves = set()
        for i in range(len(self.tab)):
            leaves.add(self.tab[i][0])
            leaves.add(self.tab[i][1])

        curr_node_level = []
        prev_node_level = []
        buff = float('-inf')
        for limes in leaves:
            prev_node_level.append(Node([buff, limes]))
            buff = limes
        prev_node_level.append(Node([buff, float('inf')]))

        while len(prev_node_level) > 1:
            for i in range(0, len(prev_node_level), 2):
                if i+1 == len(prev_node_level):
                    buff = Node([float('inf'), float('inf')])
                    curr_node_level.append(Node([prev_node_level[i].interval[0], buff.interval[1]], prev_node_level[i], buff))
                else:
                    curr_node_level.append(Node([prev_node_level[i].interval[0], prev_node_level[i+1].interval[1]], prev_node_level[i], prev_node_level[i+1]))
            prev_node_level = curr_node_level
            curr_node_level = []
        self.root = prev_node_level[0]

    def insert_intervals(self):
        for interval in self.tab:
            que = Queue()
            que.put((self.root, interval, interval))
            while not que.empty():
                node, [a, b], orginal = que.get()
                if node.interval == [a, b]:
                    node.data.append(orginal)
                else:
                    if a < node.left.interval[1] and b > node.right.interval[0]:
                        que.put((node.left, [a, node.left.interval[1]], orginal))
                        que.put((node.right, [node.right.interval[0], b], orginal))
                    elif a < node.left.interval[1]:
                        que.put((node.left, [a, b], orginal))
                    else:
                        que.put((node.right, [a, b], orginal))

    def print_tree(self):
        que = Queue()
        que.put((self.root, 0))
        prev_level = -1
        while not que.empty():
            node, level = que.get()
            if prev_level != level:
                prev_level = level
                print("\n", node.interval, end="\t")
            else:
                print(node.interval, end="\t")

            if node.left is not None:
                que.put((node.left, level + 1))
            if node.right is not None:
                que.put((node.right, level + 1))

    def print_content(self):
        que = Queue()
        que.put((self.root, 0))
        prev_level = -1
        while not que.empty():
            node, level = que.get()
            if prev_level != level:
                prev_level = level
                print("Next level:\n{}: {}".format(node.interval, node.data))
            else:
                print("{}: {}".format(node.interval, node.data))

            if node.left is not None:
                que.put((node.left, level + 1))
            if node.right is not None:
                que.put((node.right, level + 1))

    def in_point(self, point):
        result = set()
        que = Queue()
        que.put(self.root)
        while not que.empty():
            node = que.get()
            for i in node.data:
                result.add(i)
            if node.left is not None and point <= node.left.interval[1]:
                que.put(node.left)
            if node.right is not None and point >= node.right.interval[0]:
                que.put(node.right)
        return result

x = IntervalTree([(1, 6), (3, 4), (5, 6), (2, 5)])
x.make_tree()
x.print_tree()
print()
x.insert_intervals()
x.print_content()
print()
print(x.in_point(5))
