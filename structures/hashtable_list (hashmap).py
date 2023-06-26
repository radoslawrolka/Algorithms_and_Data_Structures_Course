# maintains the hashmap filled in between 0.4 - 0.75 of the total capacity.
# array and Node approach, faster to rehash whole hashmap
from random import randint

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None

class Hashmap:
    def __init__(self, size=4):
        self.array = [None for _ in range(size)]
        self.size = size
        self.full = 0
        self.hash_data_a = randint(4804, 21043985)
        self.hash_data_b = randint(6573, 24062002)

    def hash_func(self, key):
        return (self.hash_data_a*key + self.hash_data_b) % self.size

    def get_data(self, key):
        com = self.array[self.hash_func(key)]
        while com is not None:
            if com.key == key:
                return com.data
            com = com.next
        return None

    def remove(self, key):
        com = self.array[self.hash_func(key)]
        prev = None
        if com.next is None:
            self.array[self.hash_func(key)] = None
            self.full -= 1
            self.reset_hash()
            return True
        if com.key == key:
            self.array[self.hash_func(key)] = com.next
            self.full -= 1
            self.reset_hash()
            return True
        while com is not None:
            if com.key == key:
                prev.next = com.next
                self.full -= 1
                self.reset_hash()
                return True
            prev = com
            com = com.next
        return False

    def insert(self, key, data):
        com = self.array[self.hash_func(key)]
        if com is None:
            self.array[self.hash_func(key)] = Node(key, data)
            self.full += 1
        else:
            prev = None
            while com is not None:
                if com.key == key:
                    com.data = data
                    return
                prev = com
                com = com.next
            prev.next = Node(key, data)
            self.full += 1

        self.reset_hash()

    def reset_hash(self):
        if self.full/self.size > 0.75:
            self.hash_data_a = randint(4804, 21043985)
            self.hash_data_b = randint(6573, 24062002)
            self.size *= 2
            new_array = [None for _ in range(self.size)]

            for i in range(self.size//2):
                com = self.array[i]
                while com is not None:
                    if new_array[self.hash_func(com.key)] is None:
                        new_array[self.hash_func(com.key)] = com
                    else:
                        buff = new_array[self.hash_func(com.key)]
                        prev = None
                        while buff is not None:
                            prev = buff
                            buff = buff.next
                        prev.next = com
                    nex = com.next
                    com.next = None
                    com = nex

            self.array = new_array

        elif self.full/self.size < 0.4:
            self.hash_data_a = randint(4804, 21043985)
            self.hash_data_b = randint(6573, 24062002)
            self.size //= 2
            new_array = [None for _ in range(self.size)]

            for i in range(self.size*2):
                com = self.array[i]
                while com is not None:
                    if new_array[self.hash_func(com.key)] is None:
                        new_array[self.hash_func(com.key)] = com
                    else:
                        buff = new_array[self.hash_func(com.key)]
                        prev = None
                        while buff is not None:
                            prev = buff
                            buff = buff.next
                        prev.next = com
                    nex = com.next
                    com.next = None
                    com = nex
            self.array = new_array
