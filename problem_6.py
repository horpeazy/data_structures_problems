class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def sortedMerge(self, node1, node2):
        node = None

        if node1 == None:
            return node2
        if node2 == None:
            return node1

        if node1.value is None or node2.value is None:
            raise TypeError("Linked list contains none")

        if node1.value <= node2.value:
            node = node1
            node.next = self.sortedMerge(node1.next, node2)
        else:
            node = node2
            node.next = self.sortedMerge(node2.next, node1)
        return node

    def getMiddle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next

        return slow

    def mergeSort(self, head):
        if head == None or head.next == None:
            return head
        
        middle = self.getMiddle(head)
        nexttomiddle = middle.next

        middle.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(nexttomiddle)

        sortedlist = self.sortedMerge(left, right)
        self.head = sortedlist
        return self.head

def union(llist_1, llist_2):
    # Your Solution Here
    llist = LinkedList()

    if not llist_1 or not llist_2:
        return None

    node_1 = llist_1.mergeSort(llist_1.head)
    node_2 = llist_2.mergeSort(llist_2.head)

    while (node_1 and node_2):
        # Skip repetition
        if node_1.next:
            while node_1.next and (node_1.value == node_1.next.value):
                node_1 = node_1.next
        if node_2.next:
            while node_2.next and (node_2.value == node_2.next.value):
                node_2 = node_2.next

        if (node_1.value < node_2.value):
            llist.prepend(node_1.value)
            node_1 = node_1.next
        elif node_1.value > node_2.value:
            llist.prepend(node_2.value)
            node_2 = node_2.next
        else:
            llist.prepend(node_1.value)
            node_1 = node_1.next
            node_2 = node_2.next

    
    while node_1:
        # Skip repetition
        if node_1.next:
            while node_1.next and (node_1.value == node_1.next.value):
                node_1 = node_1.next
        llist.prepend(node_1.value)
        node_1 = node_1.next

    while node_2:
        # Skip repetition
        if node_2.next:
            while node_2.next and (node_2.value == node_2.next.value):
                node_2 = node_2.next
        llist.prepend(node_2.value)
        node_2 = node_2.next

    return llist

def intersection(llist_1, llist_2):
    llist = LinkedList()

    if not llist_1 or not llist_2:
        return None

    node_1 = llist_1.mergeSort(llist_1.head)
    node_2 = llist_2.mergeSort(llist_2.head)

    while node_1 and node_2:
        if node_1.next:
            while node_1.next and (node_1.value == node_1.next.value):
                node_1 = node_1.next
        if node_2.next:
            while node_2.next and (node_2.value == node_2.next.value):
                node_2 = node_2.next
        if node_1.value < node_2.value:
            node_1 = node_1.next
        elif node_1.value > node_2.value:
            node_2 = node_2.next
        else:
            llist.prepend(node_1.value)
            node_1 = node_1.next
            node_2 = node_2.next

    return llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.prepend(i)

for i in element_2:
    linked_list_2.prepend(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
print()

# # Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.prepend(i)

for i in element_2:
    linked_list_4.prepend(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
print()

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1, 6, 5, 3, 6, 0]
element_2 = [0, 23, 53, 5, -1]

for i in element_1:
    linked_list_5.prepend(i)

for i in element_2:
    linked_list_6.prepend(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))
print()

# 53 -> 23 -> 6 -> 5 -> 3 -> 1 -> 0 -> -1 ->
# 5 -> 0 ->

# Test Case 2

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [1, None, 5, 3, 6, 0]
element_2 = [0, 23, 53, 5, None]

for i in element_1:
    linked_list_7.prepend(i)

for i in element_2:
    linked_list_8.prepend(i)

print (union(linked_list_7,linked_list_8))
print (intersection(linked_list_7,linked_list_8))
print()

# Traceback (most recent call last):
# ...
# TypeError: Linked list contains none

# Test Case 3

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = [7]
element_2 = []

for i in element_1:
    linked_list_9.prepend(i)

for i in element_2:
    linked_list_10.prepend(i)

print (union(linked_list_9,linked_list_10))
print (intersection(linked_list_9,linked_list_10))
print()

# 7 ->
#                                      //Empty Line
