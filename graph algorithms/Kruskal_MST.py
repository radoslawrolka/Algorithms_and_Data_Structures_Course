# Kruskal Algorithm - MST (minimal spanning trees) [ O(E*logV) ]

# Node approach [ edge-array: (vertex_1, vertex_2, value) ]
class Node:
    def __init__(self, val):
        self.parent = self
        self.rank = 0
        self.value = val

def findset(x):
    if x.parent != x:
        x.parent = findset(x.parent)
    return x.parent

def union(x, y):
    x_root = findset(x)
    y_root = findset(y)
    if x_root == y_root:
        return False
    if x_root.rank > y_root.rank:
        y_root.parent = x_root
    else:
        x_root.parent = y_root
        if x_root.rank == y_root.rank:
            y_root.rank += 1
    return True

def Kruskal_MST_node(graph, num_of_vertices):
    MST = []
    total_cost = 0

    veritces_nodes = [Node(_) for _ in range(num_of_vertices)]
    graph.sort(key=lambda x: x[2])
    for v_1, v_2, cost in graph:
        added_edge = union(veritces_nodes[v_1], veritces_nodes[v_2])
        if added_edge:
            total_cost += cost
            MST.append((v_1, v_2))

    return total_cost, MST


# Objective approach
class FindUnion:
    def __init__(self, num_of_vertices):
        self.parent = [_ for _ in range(num_of_vertices)]
        self.rank = [0 for _ in range(num_of_vertices)]

    def find_root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_root(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find_root(x)
        y_root = self.find_root(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[y_root] += 1
        return True

def Kruksal_MST_object(graph, num_of_vertices):
    MST = []
    total_cost = 0

    fin_uni_obj = FindUnion(num_of_vertices)
    graph.sort(key=lambda x: x[2])
    for v_1, v_2, cost in graph:
        added_edge = fin_uni_obj.union(v_1, v_2)
        if added_edge:
            total_cost += cost
            MST.append((v_1, v_2))

    return total_cost, MST
