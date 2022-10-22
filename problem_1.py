class Node():
    def __init__(self, value, key) -> None:
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add(self, value, key):
        if self.head is None:
            self.head = Node(value, key)
            self.tail = self.head
            return self.head
        node = Node(value, key)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        return self.tail

    def remove(self, node):
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
            return

        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            return

        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        return


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = dict({})
        self.dlist = DoublyLinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        item = self.cache.get(key)

        if item is None:
            return -1

        self.dlist.remove(item)
        self.dlist.add(item.value, item.key)
        return item.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key is None or key == "":
            return -1

        if self.cache.get(key) is None:
            if len(self.cache) == self.capacity:
                lru_item = self.dlist.head
                self.dlist.remove(lru_item)
                self.cache.pop(lru_item.key)
                new_item = self.dlist.add(value, key)
                self.cache[key] = new_item
            else:
                new_item = self.dlist.add(value, key)
                self.cache[key] = new_item
            return
        else:
            return -1

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1) )      # returns 1
print(our_cache.get(2) )      # returns 2
print(our_cache.get(9) )     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3)   )   # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(our_cache.set("", "Udacity") )
print(our_cache.get("") )            
# -1
# -1

# Test Case 2
print(our_cache.set(None, "Data Structures") ) 
print(our_cache.get(1000))                            
# -1
# -1

# Test Case 3
new_cache = LRU_Cache(3)

new_cache.set("course", "data structures")
new_cache.set("school", "Udacity")
new_cache.set("name", "Hope")
new_cache.set("profession", "software engineer")

print(new_cache.get("course") )
print(new_cache.get("school"))   
new_cache.set("nationality", "Nigeria")
print(new_cache.get("name"))                   

# -1
# Udacity
# -1