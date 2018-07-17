from implementation import SinglyLinkedListNode, LinkedList

# Helper function
def create_singly_linked_list(vals):
    my_node = SinglyLinkedListNode(vals[0])
    my_sll = LinkedList(my_node)

    for val in vals[1:]:
        my_sll.append_to_tail(val)

    return my_sll

my_sll = create_singly_linked_list([1, 2, 2, 2, 4])

# Problems
def remove_dupes(ll):
    values = []
    current_node = ll.head
    placeholder_node = ll.head
    is_skipping = False

    while current_node is not None:
        if current_node.val not in values:
            if is_skipping:
                placeholder_node.next = current_node
                placeholder_node = current_node
            else:
                values.append(current_node.val)
                placeholder_node = current_node
        else:
            if not is_skipping:
                is_skipping = True
        
        current_node = current_node.next
    
    if is_skipping:
        placeholder_node.next = None
    
    return ll

print('** remove_dupes **')
print('Started with', my_sll.get_length(), 'nodes')
print('Removed duplicates:', remove_dupes(my_sll))
print('Ended with', my_sll.get_length(), 'nodes')

# def remove_dupes_without_buffer(ll):
#     pointer1 = ll.head
#     pointer2 = pointer1.next

# print('** remove_dupes_without_buffer **')
# print(remove_dupes_without_buffer(my_dll)

def get_kth_to_last_node(k, sll):
    ll_length = sll.get_length()
    kth_to_last_node = ll_length - k

    if kth_to_last_node <= 0:
        return 'Linked list is not long enough to get {} from last node'.format(k)
    else:
        counter = 1
        current_node = sll.head

        while counter is not kth_to_last_node:
            current_node = current_node.next
            counter += 1
        return current_node.val

my_sll = create_singly_linked_list([0, 1, 2, 3])

print('** get_kth_to_last_node **')
print('get_kth_to_last_node(0, my_sll):', get_kth_to_last_node(0, my_sll))
print('get_kth_to_last_node(2, my_sll):', get_kth_to_last_node(2, my_sll))
print('get_kth_to_last_node(3, my_sll):', get_kth_to_last_node(3, my_sll))
print('get_kth_to_last_node(4, my_sll):', get_kth_to_last_node(4, my_sll))

my_sll = create_singly_linked_list([0, 1, 2, 3])

def delete_middle_node(val, sll):
    placeholder_node = sll.head
    current_node = sll.head.next

    while current_node is not None:
        if current_node.val == val:
            placeholder_node.next = current_node.next
        placeholder_node = current_node
        current_node = current_node.next
    
    return sll

print('** delete_middle_node **')
print('delete_middle_node(1, my_sll):', delete_middle_node(1, my_sll).get_vals())
print('delete_middle_node(2, my_sll):', delete_middle_node(2, my_sll).get_vals())

my_sll = create_singly_linked_list([3, 5, 8, 5, 10, 2, 1])

def partition(sll, partition):
    nodes_over = []
    current_node = sll.head
    
    while current_node is not None:
        if current_node.val >= partition:
            
        current_node = current_node.next

print('** partition **')
print('partition(1, my_sll):', partition(my_sll, 5).get_vals())