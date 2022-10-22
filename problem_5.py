import hashlib
from time import gmtime, strftime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.next = None
        self.hash = self.calc_hash()

    @property
    def timestamp(self):
        return self.__timestamp
    
    @property
    def data(self):
        return self.__data
    
    @property
    def previous_hash(self):
        return self.__previous_hash

    @timestamp.setter
    def timestamp(self, timestamp):
        self.__timestamp = timestamp

    @data.setter
    def data(self, data):
        if not data or isinstance(data, int):
            raise TypeError("Invalid data")
        self.__data = data

    @previous_hash.setter
    def previous_hash(self, previous_hash):
        self.__previous_hash = previous_hash

    def calc_hash(self):
        sha = hashlib.sha256()

        timestamp = self.timestamp.encode('utf-8')
        data = self.data.encode('utf-8')
        previous_hash = self.previous_hash.encode('utf-8')

        sha.update(timestamp)
        sha.update(data)
        sha.update(previous_hash)

        return sha.hexdigest()

class BlockChain:
    def __init__(self) -> None:
        self.head = None

    def add_block(self, data):
        if self.head is None:
            self.head = Block(strftime("%z", gmtime()), data, "0")
            return
        previous_hash = self.head.hash
        block = Block(strftime("%z", gmtime()), data, previous_hash)
        block.next = self.head
        self.head = block

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


# Test case 1
blockchain = BlockChain()
blockchain.add_block(data="Transaction 1")
blockchain.add_block(data="Transaction 2")
blockchain.add_block(data="Transaction 3")

for block in blockchain:
    print(block.hash)

# Output
# fb84b0df5f3f9b41686f8a3bd97ffdc1891e7e6b94e89711411e01fd43a77fdb
# 0da787e51501cf5b105a13db7a42324095f423e1811fd4aa0161cd1ea5de43f7
# 9ac190ef50b7229e7c44e2016ce18ead4093293017b7278a2598725e9a42ada8

# Test case 2
blockchain = BlockChain()
blockchain.add_block(data=None)
blockchain.add_block(data="Transaction 2")
blockchain.add_block(data="Transaction 3")

for block in blockchain:
    print(block.hash)

# Ouput
# Traceback (most recent call last):
# ...
# TypeError: Invalid data

# Test case 3
blockchain = BlockChain()
blockchain.add_block(data=123)
blockchain.add_block(data="Transaction 2")
blockchain.add_block(data="Transaction 3")

for block in blockchain:
    print(block.hash)

# Ouput
# Traceback (most recent call last):
# ...
# TypeError: Invalid data