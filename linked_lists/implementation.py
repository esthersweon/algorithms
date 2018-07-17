class SinglyLinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def append(self, val):
        self.next = SinglyLinkedListNode(val)

class DoublyLinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
    def append(self, val):
        self.next = DoublyLinkedListNode(val)
        self.next.prev = self
    
    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev

class LinkedList:
    def __init__(self, head):
        self.head = head

    def append_to_tail(self, val):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.append(val)
    
    def get_vals(self):
        vals = []
        current_node = self.head

        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        
        return vals

    def get_length(self):
        counter = 0
        current_node = self.head

        while current_node is not None:
            counter += 1
            current_node = current_node.next
        return counter

first_node = SinglyLinkedListNode(1)
my_sll = LinkedList(first_node)
my_sll.append_to_tail(2)

# print('Singly Linked List:', my_sll)
# print('Head:', my_sll.head)
# print('Head Value:', my_sll.head.val)
# print('Next Node:', my_sll.head.next)
# print('Next Node Value:', my_sll.head.next.val)
# print('Next Node:', my_sll.head.next.next)
# print('Total Length:', my_sll.get_length())

third_node = DoublyLinkedListNode(3)
my_dll = LinkedList(third_node)
my_dll.append_to_tail(4)
my_dll.append_to_tail(5)

# print('\nDoubly Linked List:', my_dll)
# print('Head:', my_dll.head)
# print('Head Value:', my_dll.head.val)
# print('Next Node:', my_dll.head.next)
# print('Next Node Value:', my_dll.head.next.val)
# print("Next Node's Previous (Head Node):", my_dll.head.next.prev)
# print("Next Node's Previous Value (Head Value):", my_dll.head.next.prev.val)
# print('Next Node:', my_dll.head.next.next)
# print('Next Node Value:', my_dll.head.next.next.val)
# print('Total Length:', my_dll.get_length())

# print('\nDeleted 2nd Node')
my_dll.head.next.delete()

# print('\nNew Doubly Linked List:', my_dll)
# print('Head:', my_dll.head)
# print('Head Value:', my_dll.head.val)
# print('Next Node:', my_dll.head.next)
# print('Next Node Value:', my_dll.head.next.val)
# print("Next Node's Previous (Head Node):", my_dll.head.next.prev)
# print("Next Node's Previous Value (Head Value):", my_dll.head.next.prev.val)
# print('Next Node:', my_dll.head.next.next)