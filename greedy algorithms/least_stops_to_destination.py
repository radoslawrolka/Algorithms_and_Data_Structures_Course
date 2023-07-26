# time: O( nlogn )
from queue import PriorityQueue
def frog(tab):
    n = len(tab)
    stop = 0
    que = PriorityQueue()

    que.put(-tab[0])
    i = 0
    while not que.empty():
        energy = -que.get()
        stop += 1
        if i+energy >= n:
            return stop
        while energy > 0:
            i += 1
            energy -= 1
            if tab[i] != 0:
                que.put(-tab[i])

    return float('inf')
