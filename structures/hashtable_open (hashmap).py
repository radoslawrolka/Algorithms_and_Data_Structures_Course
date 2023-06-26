# open approach, maintains the hashmap filled in between 0.4 - 0.75 of the total capacity.
# if cell is taken, insert data in next free cell
# self.array[i][0] >= 0: normal key, if not equal - search next cell
# self.array[i][0] = -1: empty, end search
# self.array[i][0] = -2: empty, but content was removed, search next cell
from random import randint
class Hashmap:
    def __init__(self, size=1):
        self.array = [[-1, None] for _ in range(size)]
        self.size = size
        self.full = 0
        self.hash_data_a = randint(4804, 21043985)
        self.hash_data_b = randint(6573, 24062002)

    def hash_func(self, key):
        return (self.hash_data_a*key + self.hash_data_b) % self.size

    def get_data(self, key):
        hash_key = self.hash_func(key)
        if self.array[hash_key][0] == key:
            return self.array[hash_key][1]
        elif self.array[hash_key][0] == -1:
            return None
        else:
            for i in range(hash_key+1, self.size):
                if self.array[i][0] == key:
                    return self.array[i][1]
                elif self.array[i][0] == -1:
                    return None
            for i in range(0, hash_key):
                if self.array[i][0] == key:
                    return self.array[i][1]
                elif self.array[i][0] == -1:
                    return None
            return None

    def insert(self, key, data):
        hash_key = self.hash_func(key)
        if self.array[hash_key][0] in [-1, -2]:
            self.array[hash_key] = [key, data]
            self.full += 1
            self.reset_hash()
        else:
            for i in range(hash_key+1, self.size):
                if self.array[i][0] in [-1, -2]:
                    self.array[i] = [key, data]
                    self.full += 1
                    self.reset_hash()
                    return True
            for i in range(0, hash_key):
                if self.array[i][0] in [-1, -2]:
                    self.array[i] = [key, data]
                    self.full += 1
                    self.reset_hash()
                    return True
            return False

    def remove(self, key):
        hash_key = self.hash_func(key)
        if self.array[hash_key][0] == key:
            self.array[hash_key] = [-2, None]
            self.full -= 1
            self.reset_hash()
            return True
        elif self.array[hash_key][0] == -1:
            return False
        else:
            for i in range(hash_key+1, self.size):
                if self.array[i][0] == key:
                    self.array[i] = [-2, None]
                    self.full -= 1
                    self.reset_hash()
                    return True
                elif self.array[i][0] == -1:
                    return False
            for i in range(0, hash_key):
                if self.array[i][0] == key:
                    self.array[i] = [-2, None]
                    self.full -= 1
                    self.reset_hash()
                    return True
                elif self.array[i][0] == -1:
                    return False
            return False

    def reset_insert(self, array, key, data):
        hash_key = self.hash_func(key)
        if array[hash_key][0] == -1:
            array[hash_key] = [key, data]
        else:
            for i in range(hash_key + 1, self.size):
                if array[i][0] == -1:
                    array[i] = [key, data]
                    return True
            for i in range(0, hash_key):
                if array[i][0] == -1:
                    array[i] = [key, data]
                    return True
            return False

    def reset_hash(self):
        if self.full/self.size > 0.75:
            self.size *= 2
            new_array = [[-1, None] for _ in range(self.size)]
            self.hash_data_a = randint(4804, 21043985)
            self.hash_data_b = randint(6573, 24062002)

            for i in range(self.size//2):
                if self.array[i][0] >= 0:
                    self.reset_insert(new_array, self.array[i][0], self.array[i][1])
            self.array = new_array

        elif self.full/self.size < 0.4:
            self.size //= 2
            new_array = [[-1, None] for _ in range(self.size)]
            self.hash_data_a = randint(4804, 21043985)
            self.hash_data_b = randint(6573, 24062002)

            for i in range(self.size*2):
                if self.array[i][0] >= 0:
                    self.reset_insert(new_array, self.array[i][0], self.array[i][1])
            self.array = new_array
