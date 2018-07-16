def remove_dupes(ll):
    values = []
    current_node = ll['head']
    placeholder_node = ll['head']
    is_skipping = False

    while current_node is not None:
        if current_node['val'] not in values:
            if is_skipping:
                placeholder_node['next'] = current_node
                placeholder_node = current_node
            else:
                values.append(current_node['val'])
                placeholder_node = current_node
        else:
            if not is_skipping:
                is_skipping = True
        
        current_node = current_node['next']
    
    if is_skipping:
        placeholder_node['next'] = None
    
    return ll

print('** remove_dupes **')
print(remove_dupes({'head': {'val': 1, 'next': {'val': 2, 'next': {'val': 3, 'next': {'val': 1, 'next': {'val': 3, 'next': {'val': 5, 'next': None}}}}}}}))
print(remove_dupes({'head': {'val': 1, 'next': {'val': 2, 'next': {'val': 3, 'next': {'val': 1, 'next': {'val': 3, 'next': {'val': 2, 'next': None}}}}}}}))

def remove_dupes_without_buffer(ll):
    pointer1 = ll['head']
    pointer2 = pointer1['next']

    

print('** remove_dupes_without_buffer **')
print(remove_dupes_without_buffer({'head': {'val': 1, 'next': {'val': 2, 'next': {'val': 3, 'next': {'val': 1, 'next': {'val': 3, 'next': {'val': 5, 'next': None}}}}}}}))
print(remove_dupes_without_buffer({'head': {'val': 1, 'next': {'val': 2, 'next': {'val': 3, 'next': {'val': 1, 'next': {'val': 3, 'next': {'val': 2, 'next': None}}}}}}}))