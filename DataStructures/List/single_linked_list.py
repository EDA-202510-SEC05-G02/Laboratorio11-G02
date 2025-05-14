def new_list():
    newlist = {
        'first': None,
        'last': None,
        'size': 0
    }
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    """

    Args:
        my_list (_type_): _description_
        element (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    new_node = {
        'info': element,
        'next': my_list['first']
    }
    my_list['first'] = new_node
    if my_list['size'] == 0:
        my_list['last'] = new_node
    my_list['size'] += 1
    return my_list

def add_last(my_list, element):
    """

    Args:
        my_list (_type_): _description_
        element (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    new_node = {
        'info': element,
        'next': None
    }
    if my_list['size'] == 0:  
        my_list['first'] = new_node
        my_list['last'] = new_node  
    else:
        if my_list['last'] is not None: 
            my_list['last']['next'] = new_node
        my_list['last'] = new_node 
        
    my_list['size'] += 1
    return my_list


def size(my_list):
    """

    Args:
        my_list (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    size = my_list['size']
    
    return size


def first_element(my_list):
    """

    Args:
        my_list (_type_): _description_

    Returns:
        _type_: _description_
    """    
    
    if my_list['first'] is not None:
        return my_list['first']['info']
    else:
        return None
    
def is_empty(my_list):
    
    if my_list['size'] == 0:
        return True
    else:
        return False
    
    
def last_element(my_list):
    
    if my_list['last'] is not None:
        return my_list['last']['info']
    else:
        return None
    

def remove_first(my_list):
    
    if my_list['size'] == 0:
        raise IndexError("list index out of range")
    
    removed_element = my_list['first']['info']
    my_list['first'] = my_list['first']['next']
    my_list['size'] -= 1
    
    if my_list['size'] == 0:
        my_list['last'] = None
        
    return removed_element

def remove_last(my_list):
    
    if my_list['size'] == 0:
        raise IndexError("list index out of range")
    
    removed_element = my_list['last']['info']
    
    if my_list['size'] == 1:
        my_list['first'] = None
        my_list['last'] = None
    else:
        current = my_list['first']
        while current['next'] != my_list['last']:
            current = current['next']
        current['next'] = None
        my_list['last'] = current
    
    my_list['size'] -= 1
    
    return removed_element

def insert_element(my_list, element, pos):
    
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    
    new_node = {
        'info' : element,
        'next': None
    }
    
    if pos == 0:
        new_node['next'] = my_list['first']
        my_list['first'] = new_node
        if my_list['size'] == 0:
            my_list['last'] = new_node
    else:
        current = my_list['first']
        for _ in range(pos - 1):
            current = current['next']
        new_node['next'] = current['next']
        current['next'] = new_node
        if new_node['next'] is None:
            my_list['last'] = new_node
    
    my_list['size'] += 1
    
    return my_list

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list['size']:
        raise IndexError('list index out of range')
    
    if pos == 0:
        remove_first(my_list)
    else:
        current = my_list['first']
        for _ in range(pos - 1):
            current = current['next']
        
        removed_element = current['next']['info']
        current['next'] = current['next']['next']
        
        if current['next'] is None:
            my_list['last'] = current
        
        my_list['size'] -= 1
    
    return my_list
    
def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list['size']:
        raise IndexError('list index out of range')
    
    current = my_list['first']
    for _ in range(pos):
        current = current['next']
    
    current['info'] = new_info
    
    return my_list
    
def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= my_list['size'] or pos_2 < 0 or pos_2 >= my_list['size']:
        raise IndexError('list index out of range')
    
    if pos_1 == pos_2:
        return my_list
    
    current_1 = my_list['first']
    for _ in range(pos_1):
        current_1 = current_1['next']
    
    current_2 = my_list['first']
    for _ in range(pos_2):
        current_2 = current_2['next']
    
    current_1['info'], current_2['info'] = current_2['info'], current_1['info']
    
    return my_list

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos > my_list['size']:
        raise IndexError('list index out of range')
    
    sublist = new_list()
    if pos == my_list['size']:
        return sublist

    current = my_list["first"]
    for _ in range(pos):
        current = current["next"]

    for _ in range(num_elements):
        if current is None:
            break
        add_last(sublist, current["info"])
        current = current["next"]

    return sublist

            
    
#Algoritmos de ordenamiento iterativo 

def default_sort_criteria(elemento_1, elemento_2):
    """Función de comparación por defecto para ordenar elementos.
    Compara dos elementos y retorna True si el primer elemento es 
    menor que el segundo y False en caso contrario.

    Args:
        elemento_1 (any): Primer elemento a comparar.
        elemento_2 (any): Segundo elemento a comparar.

    Returns:
        bool: True si el primer elemento es menor que el segundo, 
        False en caso contrario.
    """
    is_sorted = False
    if elemento_1 < elemento_2:
      is_sorted = True
    return is_sorted


def selection_sort(my_list, sort_crit):
    """Ordena una lista utilizando el algoritmo de ordenamiento Selecion Sort.
        Se recorre la lista y se selecciona el elemento más pequeño y se intercambia 
        con el primer elemento. Luego se selecciona el segundo elemento más pequeño y 
        se intercambia con el segundo elemento, y así sucesivamente.

    Args:
        my_list (array_list o single_linked_list): Lista a ordenar.
        sort_crit (function): Función de comparación.

    Returns:
        array_list o single_linked_list: Lista ordenada.

    """
    
    if not my_list or my_list["size"] <= 1:
        return my_list

    nodo_actual = my_list["first"]

    while nodo_actual:
        nodo_minimo = nodo_actual
        nodo_siguiente = nodo_actual["next"]

        while nodo_siguiente:
            if sort_crit(nodo_siguiente["info"], nodo_minimo["info"]):
                nodo_minimo = nodo_siguiente
            nodo_siguiente = nodo_siguiente["next"]

        # Intercambiar los valores de los nodos
        temp = nodo_actual["info"]
        nodo_actual["info"] = nodo_minimo["info"]
        nodo_minimo["info"] = temp

        nodo_actual = nodo_actual["next"]

    return my_list

def insertion_sort(my_list, sort_crit):
    """Ordena una lista enlazada simple utilizando el algoritmo de ordenamiento Insertion Sort.

    Args:
        my_list (single_linked_list): Lista enlazada simple a ordenar.
        sort_crit (function): Función de comparación.

    Returns:
        single_linked_list: Lista enlazada simple ordenada.
    """

    if my_list['size'] <= 1:
        return my_list

    sorted_list = new_list()
    current = my_list['first']

    while current:
        next_node = current['next']
        if sorted_list['first'] is None:
            sorted_list['first'] = current
            sorted_list['last'] = current
            current['next'] = None
        else:
            if sort_crit(current['info'], sorted_list['first']['info']):
                current['next'] = sorted_list['first']
                sorted_list['first'] = current
            else:
                search = sorted_list['first']
                while search['next'] and sort_crit(search['next']['info'], current['info']):
                    search = search['next']
                current['next'] = search['next']
                search['next'] = current
                if current['next'] is None:
                    sorted_list['last'] = current
        current = next_node
        sorted_list['size'] += 1
    my_list['first'] = sorted_list['first']
    my_list['last'] = sorted_list['last']
    return my_list


def shell_sort(my_list, sort_crit):
    if my_list['size'] <= 1:
        return my_list

    n = my_list['size']
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = get_element(my_list, i)
            j = i
            while j >= gap and sort_crit(temp, get_element(my_list, j - gap)):
                change_info(my_list, j, get_element(my_list, j - gap))
                j -= gap
            change_info(my_list, j, temp)
        gap //= 2
    return my_list

def merge_sort():
    pass

def quick_sort(my_list, sort_crit: callable):
    """Ordena una lista utilizando el algoritmo recursivo de ordenamiento Quick Sort.
    Se selecciona un elemento como pivote y se colocan los elementos menores a la izquierda 
    y los mayores a la derecha de este elemento pivote. Si la lista es vacía o tiene un solo 
    elemento, se retorna la lista original.

    Args:
        my_list (array_list o single_linked_list): Lista a ordenar.
        sort_crit (function): Función de comparación.

    Returns:
        array_list o single_linked_list: Lista ordenada."""
        
    if not my_list or my_list["size"] <= 1:
        return my_list

    _quick_sort(my_list, 0, my_list["size"] - 1, sort_crit)
    return my_list

def _quick_sort(my_list: dict, low: int, high: int, sort_crit: callable):
    if low < high:
        pivot = _partition(my_list, low, high, sort_crit)
        _quick_sort(my_list, low, pivot - 1, sort_crit)
        _quick_sort(my_list, pivot + 1, high, sort_crit)

def _partition(my_list: dict, low: int, high: int, sort_crit: callable) -> int:
    follower = leader = low
    pivot_element = get_element(my_list, high)

    while leader < high:
        current_element = get_element(my_list, leader)
        if sort_crit(current_element, pivot_element):
            exchange(my_list, follower, leader)
            follower += 1
        leader += 1

    exchange(my_list, follower, high)
    return follower


    
