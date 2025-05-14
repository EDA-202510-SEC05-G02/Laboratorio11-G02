def new_queue():
    return {'size': 0, 'elements': []}

def enqueue(my_queue, element):
    """Agrega un elemento al final de la cola."""
    my_queue['elements'].append(element)
    my_queue['size'] += 1
    return my_queue

def dequeue(my_queue):
    """Elimina y retorna el primer elemento de la cola."""
    if my_queue['size'] == 0:
        raise Exception('EmptyStructureError: queue is empty')
    else:
        deleted_element = my_queue['elements'].pop(0)
        my_queue['size'] -= 1
    
    return deleted_element

def peek(my_queue):
    
    first_element = my_queue['elements'][0]
    
    return first_element

def is_empty(my_queue):
    
    if my_queue['size'] == 0:
        return True
    else:
        return False

def size(my_queue):
    
    size = my_queue['size']
    
    return size



        
    