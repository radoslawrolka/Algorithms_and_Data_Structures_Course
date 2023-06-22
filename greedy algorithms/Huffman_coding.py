# taking two least frequent chars in string and combining them into a tree
from queue import PriorityQueue


class Node:
    def __init__(self, letter=None, left=None, right=None):
        self.letter = letter
        self.left = left
        self.right = right


def huffman_code(code):

    # count the occurrence of each letter
    frequency = {}
    def count_frequncy():
        nonlocal code, frequency
        m = set(code)
        for i in m:
            frequency[i] = 0
        for char in code:
            frequency[char] += 1
    count_frequncy()

    # making node for each letter
    que = PriorityQueue()
    for char in frequency:
        que.put((frequency[char], char, Node(char)))

    # setting huffman coding tree
    while que.qsize() > 1:
        quantity_1, char_1, node_1 = que.get()
        quantity_2, char_2, node_2 = que.get()
        que.put((quantity_1 + quantity_2, char_2 + char_2, Node(None, node_1, node_2)))

    # saving root of the tree
    quantitiy_orginal, _, head = que.get()

    # setting key for each letter [frequency is now a key]
    def set_coding(node, code_char):
        nonlocal frequency
        if node.letter is not None:
            frequency[node.letter] = code_char
        if node.right is not None:
            set_coding(node.right, code_char + "1")
        if node.left is not None:
            set_coding(node.left, code_char + "0")
    set_coding(head, "")

    # saving the result of huffman coding
    result = ""
    for char in code:
        result += frequency[char]

    print("Saved memory (in bits):", quantitiy_orginal * 8 - len(result))
    print("Entry:\t", code)
    print("Result:\t", result)
    print("Key:\t", frequency)
    return result, head


def huffman_decode(code, tree_key):
    n = len(code)
    decoded = ""
    com = tree_key
    for i in code:
        if i == "1":
            com = com.right
        else:
            com = com.left

        if com.letter is not None:
            decoded += com.letter
            com = tree_key

    print("Code:\t", code)
    print("Decode:\t", decoded)
    return decoded

x = "abbccccddddd"
y, tree_key = huffman_code(x)

huffman_decode(y, tree_key)
