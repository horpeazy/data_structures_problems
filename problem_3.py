import sys

class Node:
    """
        Node class reprensting a character and it's
        frequency
    """
    def __init__(self, char, frequency) -> None:
        self.char = char
        self.frequency = frequency
        self.leftChild = None
        self.rightChild = None

    def isLeaf(self):
        if not self.leftChild and not self.rightChild:
            return True

        return False

    def __str__(self) -> str:
        str_ = ""
        return "{}: {}".format(self.char, self.frequency)

class  MinHeap:
    """
        This is a class definition for a min-heap
        and it based on 1 -indexing
    """
    def __init__(self, maxsize: int) -> None:
        self.maxsize = maxsize
        self.heap = [Node(None, sys.maxsize)] * (self.maxsize + 1)
        self.front = 1
        self.heap[0] = Node(None, -1 * sys.maxsize)
        self.size = 0

    def parent(self, pos):
        """Returns the parent of a node in the array"""
        return pos // 2

    def leftChild(self, pos):
        """Returns the left child of a node in the array"""
        return 2 * pos

    def rightChild(self, pos):
        """Returns the right child of a node in the array"""
        return (2 * pos ) + 1

    def isLeaf(self, pos):
        """method to check if node is a leaf node"""
        return 2 * pos > self.size

    def swap(self, fpos, spos):
        """Swap the nodes"""
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def minHeapify(self, pos):
        """
            Places the element as pos in the right index in the array
            to ensure it sticks to the rules of min heap
        """
        if not self.isLeaf(pos):
            if (self.heap[pos].frequency > self.heap[self.leftChild(pos)].frequency or 
                self.heap[pos].frequency > self.heap[self.rightChild(pos)].frequency):
                if self.heap[self.leftChild(pos)].frequency <= self.heap[self.rightChild(pos)].frequency:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
    
    def insert(self, element):
        """Inserts an element into the heap"""
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.heap[self.size] = element

        current = self.size

        while self.heap[current].frequency < self.heap[self.parent(current)].frequency:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def minHeap(self):
        """
            Loops through nodes to ensure they don't break the minheap rules
        """
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)

    def pop(self):
        """Removes and returns the least node"""
        if self.size == 0:
            return "Heap is empty"

        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.minHeapify(self.front)
        return popped

    def __str__(self) -> str:
        str_ = ""
        for i in range(1, (self.size//2)+1):
            str_ += str("PARENT : "+ 
                        str(self.heap[i])+" LEFT CHILD : " + 
                        str(self.heap[2 * i])+" RIGHT CHILD : " +
                        str(self.heap[2 * i + 1]) + "\n")

        return str_[:-1]

def assign_bit(node):
    """Traverse the Tree and assign bits to the nodes"""
    if node.leftChild:
        node.leftChild.bit = 0
        assign_bit(node.leftChild)
    if node.rightChild:
        node.rightChild.bit = 1
        assign_bit(node.rightChild)
    return

def get_binary_code(node, code_map, code):
    """Traverse the Tree and get the binary code for the leaf nodes"""
    if node.isLeaf():
        code_map[node.char] = code
        return
    if node.leftChild:
        code += "0"
        get_binary_code(node.leftChild, code_map, code)
        code = code[:-1]
    if node.rightChild:
        code += "1"
        get_binary_code(node.rightChild, code_map, code)
        code = code[:-1]
    return

def get_char(node, data, index):
    """Traverses the node and returns the character at the leaf node"""
    if node.isLeaf():
        return node.char, index

    if data[index] == "0":
        return get_char(node.leftChild, data, index + 1)
    return get_char(node.rightChild, data, index + 1)


def huffman_encoding(data):
    char_freq = dict({})
    heap = MinHeap(100)
    codes_map = dict({})
    encoded_data = ""

    if not data:
        return None, None

    for char in str(data):
        char_freq[char] = char_freq.setdefault(char, 0) + 1

    for char, freq in char_freq.items():
        heap.insert(Node(char, freq))

    # heap.minHeap()
    while heap.size > 1:
        s_node = heap.pop()
        b_node = heap.pop()
        freq = s_node.frequency + b_node.frequency
        node = Node(None, freq)
        node.leftChild = s_node
        node.rightChild = b_node
        heap.insert(node)

    tree = heap.pop()
    assign_bit(tree)
    get_binary_code(tree, codes_map, "")
    for char in str(data):
        encoded_data += codes_map[char]

    return encoded_data , tree

def huffman_decoding(data,tree):
    decoded_data = ""
    index = 0
    node = tree

    if not data or not tree:
        return None

    while index < len(data):
        char, index = get_char(node, data, index)
        if char:
            decoded_data += char

    return decoded_data


#Test case 1
text = "Data Strcutures and Algorithm"
encoded_data, tree = huffman_encoding(text)
decoded_data = huffman_decoding(encoded_data, tree)
print ("{}\n".format(encoded_data))
print ("{}\n".format(decoded_data))

# Output 
# 101100011100010001010011001001100111011011100101010110001000001011110110100010010100110111011110010111111101000010111
# Data Strcutures and Algorithm

#Test case 2
text = None
encoded_data, tree = huffman_encoding(text)
decoded_data = huffman_decoding(encoded_data, tree)
print ("{}\n".format(encoded_data))
print ("{}\n".format(decoded_data))

# Output 
# None
# None

#Test case 3
text = 2342349238
encoded_data, tree = huffman_encoding(text)
decoded_data = huffman_decoding(encoded_data, tree)
print ("{}\n".format(encoded_data))
print ("{}\n".format(decoded_data))

# Output 
# 1011001011000101011011
# 2342349238

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "Udacity is the best!!!"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))