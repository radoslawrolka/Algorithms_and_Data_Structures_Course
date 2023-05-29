# Radosław Rolka
from kol2testy import runtests

"""
Problem: znajdź MST, które będzie spójnym podciągiem w posortowanym ciągu krawędzi tego grafu.

Najpierw tworzę graf o reprezentacji krawędziowej oraz go sortuję odwrotnie (szybsze usuwanie z końca).
Następnie uruchamiam Kruskala dla grafu i sprawdzam, czy krawędzie które wziął występują po sobie.
Jeśli tak, to zwracam koszt tego drzewa, jeśli nie to usuwam najmniejszą krawędź w tym grafie i ponownie uruchamiam Kruskala.

Kruskal: tak jak na wykładzie + spójność (sprawdzam każdego roota wierzchołków czy są takie same). Jeśli kruskal zwraca total_cost
 to znalazł MST, jeśli -1 to nie jest spójnym podciągiem, jeśli None to już nie może powstać takie drzewo z pozostających wierzchołków. 

Złożoność: O( VE*logE )
"""

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

    def is_Connective(self):
        main = self.find_root(self.parent[0])
        for vertex in range(1, len(self.parent)):
            if self.find_root(self.parent[vertex]) != main:
                return False
        return True

def Kruksal(graph, num_of_vertices):
    total_cost = 0

    fin_uni_obj = FindUnion(num_of_vertices)
    for i in range(len(graph) - 1, -1, -1):
        v_1, v_2, cost = graph[i]
        added_edge = fin_uni_obj.union(v_1, v_2)
        if added_edge:
            total_cost += cost
        elif total_cost != 0:
            if not fin_uni_obj.spojny():
                return -1
            return total_cost
    if fin_uni_obj.is_Connective():
        return total_cost
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(beautree, all_tests=True)
