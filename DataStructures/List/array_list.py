from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as lt
from typing import Callable

def new_list():
    newlist = {
        'elements':[],
        'size': 0,
    }
    return newlist


def get_element(my_list, index):
    if my_list is None or "elements" not in my_list or index >= len(my_list["elements"]):
        return None
    return my_list["elements"][index]
    
   


def is_present(my_list, element, cmp_function):
    
    size = my_list['size']
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list['elements'][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break 
        if keyexist:
            return keypos
    return -1 


def add_first(my_list, element):
    """

    Args:
        my_list (_type_): _description_
        element (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    my_list['elements'].insert(0, element)
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
    
    my_list['elements'].append(element)
    my_list['size'] += 1
    
    return my_list



def size(my_list):
    """

    Args:
        my_list (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    return my_list['size']



def first_element(my_list):
    """

    Args:
        my_list (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    if my_list['size'] > 0:
        return my_list['elements'][0]
    else:
        return None
    
def last_element(my_list):
    if my_list['size'] > 0:
        return my_list['elements'][-1]
    else:
        return None
    
    
def is_empty(my_list):
    
    if my_list['size'] == 0:
        return True
    else:
        return False
    
def remove_first(my_list):
    
    if my_list['size'] > 0:
        x = my_list['elements'].pop(0)
        my_list['size']-=1
    
    return x

def remove_last(my_list):
    
    if my_list['size'] > 0:
        x = my_list['elements'].pop(-1)
        my_list['size'] -= 1
    
    return x

def insert_element(my_list, element, pos):
    
    if pos > my_list['size'] or pos < 0:
        raise IndexError("Pos out of range")
    
    my_list['elements'].insert(pos, element)
    my_list['size'] += 1
    return my_list

def delete_element(my_list, pos):
    
    if pos > my_list['size'] or pos < 0:
        raise IndexError("Pos out of range")
    
    my_list['elements'].pop(pos)
    my_list['size'] -= 1
    
    return my_list

def change_info(my_list, pos, new_info):
    
    if pos > my_list['size'] or pos < 0:
        raise IndexError("Pos out of range")
    
    my_list['elements'][pos] = new_info
    
    return my_list

def exchange(my_list, pos_1, pos_2):
    
    if pos_1 > my_list['size'] or pos_1 < 0 or pos_2 > my_list['size'] or pos_2 < 0:
        raise IndexError("Pos out of range")
    
    element = my_list['elements'][pos_1]
    my_list['elements'][pos_1] = my_list['elements'][pos_2]
    my_list['elements'][pos_2] = element
    
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i > my_list['size']:
        raise IndexError("list index out of range")
    
    if num_elements < 0:
        raise ValueError('num_elements must be a positive value')
    
    sub_list = {
        'elements' : my_list['elements'][pos_i:pos_i + num_elements],
        'size' : min(num_elements, my_list['size']-pos_i)
    }
    
    return sub_list

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
    
    if not my_list:  
        return my_list
    if my_list["size"] <= 1:
        return my_list

    elements = my_list["elements"]
    m = my_list["size"]

    for i in range(m):
        elemento_menor = i
        for j in range(i + 1, m):
            if sort_crit(elements[j], elements[elemento_menor]):
                elemento_menor = j
        exchange(my_list,i,j)
    return my_list
    

def insertion_sort(my_list, sort_crit):
    """Ordena una lista utilizando el algoritmo de ordenamiento Insertion Sort.
        Se recorre la lista y se inserta cada elemento en su posición correcta.
        Se compara cada elemento con los elementos anteriores y se intercambia 
        hasta que el elemento esté en su posición correcta.

    Args:
        my_list (array_list o single_linked_list): Lista a ordenar.
        sort_crit (function): Función de comparación.

    Returns:
        array_list o single_linked_list: Lista ordenada.

    """

    if not my_list:
        return my_list
    if my_list["size"] <= 1:
        return my_list

    elements = my_list["elements"]
    m = my_list["size"]

    for i in range(1, m):
        key = elements[i]
        j = i - 1
        while j >= 0 and sort_crit(key, elements[j]):
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
    return my_list

def shell_sort(my_list, sort_crit):
    if not my_list or my_list['size'] <= 1:
        return my_list

    elements = my_list['elements']
    n = my_list['size']
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = elements[i]
            j = i
            while j >= gap and sort_crit(temp, elements[j - gap]):
                elements[j] = elements[j - gap]
                j -= gap
            elements[j] = temp
        gap //= 2
    return my_list

def merge_sort(my_list, sort_crit):
    """Ordena una lista utilizando el algoritmo recursivo de ordenamiento Merge Sort.

    Args:
        my_list (array_list o single_linked_list): Lista a ordenar.
        sort_crit (function): Función de comparación.

    Returns:
        array_list o single_linked_list: Lista ordenada.
    """

    if not my_list or my_list['size'] <= 1:
        return my_list

    elements = my_list['elements']
    size = my_list['size']
    mid = size // 2

    left_list = {'elements': elements[:mid], 'size': mid}
    right_list = {'elements': elements[mid:], 'size': size - mid}

    left_list = merge_sort(left_list, sort_crit)
    right_list = merge_sort(right_list, sort_crit)
    
    merged = merge(left_list, right_list, sort_crit)

    my_list['elements'] = merged['elements']
    my_list['size'] = merged['size']

    return my_list

def merge(left_list, right_list, sort_crit):
    """Función auxiliar para mezclar dos listas ordenadas."""

    merged_list = new_list()
    left_index, right_index = 0, 0

    while left_index < left_list['size'] and right_index < right_list['size']:
        if sort_crit(left_list['elements'][left_index], right_list['elements'][right_index]):
            add_last(merged_list, left_list['elements'][left_index])
            left_index += 1
        else:
            add_last(merged_list, right_list['elements'][right_index])
            right_index += 1

    while left_index < left_list['size']:
        add_last(merged_list, left_list['elements'][left_index])
        left_index += 1

    while right_index < right_list['size']:
        add_last(merged_list, right_list['elements'][right_index])
        right_index += 1

    return merged_list

#quick_sort segun phillipus
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


    


