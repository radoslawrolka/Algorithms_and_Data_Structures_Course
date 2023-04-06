class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


def insert(lst, val):
    com = lst
    if lst is None:
        lst = Node(val)
    elif lst.next is None:
        lst.next = Node(val)
    else:
        while com.next is not None:
            if com.next.value > val:
                new = Node(val)
                new.next = com.next
                com.next = new
                break
            com = com.next
        else:
            com.next = Node(val)


# separates [ lst from max(lst) ] <- this is returned
def separate(lst):
    com = lst
    maks = lst
    prev = None
    while com.next is not None:
        if maks.value < com.next.value:
            maks = com.next
            prev = com
        com = com.next
    if prev is not None:
        prev.next = maks.next
    else:
        lst = maks.next
    maks.next = None
    return maks, lst


def sort(lst):
    s_lst = None
    top = s_lst
    while lst is not None:
        head = lst
        lst = lst.next
        head.next = None
        insert(s_lst, head)
    return top


x = Node(4)
x.next = Node(1)
x.next.next = Node(8)
x.next.next.next = Node(3)

y = sort(x)
print(y.value)
print(y.next.value)
print(y.next.next.value)
print(y.next.next.next.value)