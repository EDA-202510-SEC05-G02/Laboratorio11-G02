from DataStructures.List import array_list as lt
from DataStructures.Priority_queue import index_pq_entry as pqe

def new_heap(is_min_pq=True):
    """Crea un cola de prioridad indexada orientada a menor o mayor 
    dependiendo del valor de is_min_pq
Se crea una cola de prioridad con los siguientes atributos:
    elements: Lista de elementos. Se inicializa como una lista vacia de tipo array_list.
    size: Tamaño de la cola de prioridad. Se inicializa en 0.
    cmp_function: La funcion de comparacion. Si es una cola de prioridad 
    orientada a menor is_min_pq = True, 
    se inicializa con la funcion default_compare_lower_value. Si es una cola 
    de prioridad orientada a mayor 
    is_min_pq = False, se inicializa con la funcion default_compare_higher_value.
Al crear la cola de prioridad, se agrega un elemento None en la posición 0 de la
lista de elementos. Esto es 
útil para poder utilizar la propiedad de los heaps, donde el padre de un nodo en la 
posición i se encuentra en la 
posición i//2, y los hijos se encuentran en las posiciones 2*i y 2*i + 1.
Parameters:
    is_min_pq (bool) – Indica si la cola de prioridad es orientada a menor o mayor. Por defecto es True.
Returns:
    Una nueva cola de prioridad indexada
Return type:
    priority_queue
    """
    priority_queue = {
        "elements": lt.new_list(),
        "size": 0,
        "cmp_function": default_compare_lower_value if is_min_pq else default_compare_higher_value
    }
    lt.add_first(priority_queue["elements"], None)
    return priority_queue

 
def  default_compare_higher_value(father_node, child_node):
    """Función de comparación por defecto para el heap orientado a mayor.
Compara la llave key de los nodos father_node y child_node. Si el nodo 
padre tiene mayor o igual prioridad que el nodo hijo, retorna True. En caso 
contrario, retorna False.
Parameters:
        father_node (pq_entry) – El nodo padre
        child_node (pq_entry) – El nodo hijo
Returns:
    True si el nodo padre tiene mayor prioridad que el nodo hijo. False en caso contrario.
Return type:
    bool
    """
    if pqe.get_key(father_node) >= pqe.get_key(child_node):
        return True
    return False

def default_compare_lower_value(father_node, child_node):
    """Función de comparación por defecto para el heap orientado a menor.
Compara la llave key de los nodos father_node y child_node. Si el nodo padre 
tiene menor o igual prioridad que el nodo hijo, retorna True. En caso contrario, retorna False.
Parameters:
        father_node (pq_entry) – El nodo padre
        child_node (pq_entry) – El nodo hijo
Returns:
    True si el nodo padre tiene menor prioridad que el nodo hijo. False en caso contrario.
Return type:
    bool
    """
    if pqe.get_key(father_node) <= pqe.get_key(child_node):
        return True
    return False

def priority(my_heap, parent, child):
    """Indica si el parent tiene mayor prioridad que child.
Nota
Esta función es utilizada por las funciones swim() y sink() para dejar el 
elemento en la posición correcta.
Important
La prioridad se define por la función de comparación del heap. Si es un heap orientado a 
menor, la prioridad es menor si el parent es menor que el child. Si es un heap orientado a 
mayor, la prioridad es mayor si el parent es mayor que el child.
Parameters:
        my_heap (priority_queue) – El heap a revisar
        parent (any) – El elemento padre
        child (any) – El elemento hijo a comparar
Returns:
    True si el parent tiene mayor prioridad que el child. False en caso contrario.
Return type:
    bool
    """
    cmp = my_heap["cmp_function"](parent, child)
    if cmp > 0:
        return True
    return False

def insert(my_heap, value, key):
    """Agrega una nueva entrada llave-valor al heap. Inserta la llave key 
    con prioridad value  en el heap al final de la lista de elementos y luego 
    se hace swim para dejar el elemento en la posición correcta.
Importante
Esta función usa la función swim() para dejar el elemento en la posición correcta.
Parameters:
        my_heap (priority_queue) – El heap sobre el cual se realiza la operación
        element (int) – El valor de la llave
        key (any) – La llave a insertar
Returns:
    El heap con la nueva paraja insertada
Return type:
    priority_queue
    """
    
    lt.add_last(my_heap["elements"], pqe.new_pq_entry(key, value))
    my_heap["size"] += 1
    swim(my_heap, my_heap["size"])

    return my_heap
    
def swim(my_heap, pos):
    """Deja en la posición correcta un elemento ubicado en la última posición del heap
Se realiza un recorrido hacia arriba en el heap, comparando el elemento con su padre. 
Si el elemento tiene mayor prioridad que su padre, se intercambian los elementos y se 
continúa el recorrido hacia arriba.
Nota
Esta función es utilizada por la función insert() para dejar el elemento en la posición 
correcta.
Parameters:
        my_heap (priority_queue) – El heap sobre el cual se realiza la operación
        pos (int) – La posición del elemento a revisar
    """
    while pos > 1:
        parent = lt.get_element(my_heap['elements'], int(pos / 2))
        element = lt.get_element(my_heap['elements'], pos)
        if not priority(my_heap, parent, element):
            lt.exchange(my_heap['elements'], pos, int(pos / 2))
        pos = pos // 2


def size(my_heap):
    """Obtiene el número de elementos en el heap.
Parameters:
    my_heap (priority_queue) – El heap del cual se quiere saber la cantidad de elementos
Returns:
    El número de elementos
Return type:
    int
    """
    return my_heap['size']
  
def is_empty(my_heap):
    """Verifica si la cola de prioridad está vacía.
Retorna True si el heap está vacío, False en caso contrario. Si el heap tiene un 
tamaño de 0, se considera vacío.
Parameters:
    my_heap (priority_queue) – El heap del cual se quiere saber si está vacío
Returns:
    True si el heap está vacío, False en caso contrario.
Return type:
    bool
    """
    return (my_heap['size'] == 0)


def get_first_priority(my_heap):
    """Obtiene el elemento de mayor prioridad del heap sin eliminarlo.
Retorna el primer elemento del heap, es decir el elemento con mayor prioridad sin eliminarlo.
Importante
Si el heap es orientado a menor, el primer elemento es el de menor valor. Si el heap es 
orientado a mayor, el primer elemento es el de mayor valor.
Parameters:
    my_heap (priority_queue) – El heap del cual se quiere obtener el primer elemento
Returns:
    El value asociada elemento de mayor prioridad. Si el heap está vacío, retorna None.
Return type:
    any
    """
    if my_heap['size'] == 0:
        return None
    return lt.get_element(my_heap['elements'], 1)['value']

def remove(my_heap):
    """Retorna el elemento del heap de mayor prioridad y lo elimina. Se reemplaza el 
    primer elemento del heap por el último elemento y se hace sink para dejar el elemento 
    en la posición correcta.
Importante
Esta función usa la función sink() para dejar el elemento en la posición correcta.
Parameters:
    my_heap (priority_queue) – El heap a revisar
Returns:
    value del elemento de mayor prioridad. Si el heap está vacío, retorna None.
Return type:
    any
    """
    if (my_heap['size'] > 0):
        min = lt.get_element(my_heap['elements'], 1)
        last = lt.get_element(my_heap['elements'], my_heap['size'])
        lt.change_info(my_heap['elements'], 1, last)
        lt.remove_last(my_heap['elements'])  
        my_heap['size'] -= 1
        sink(my_heap, 1)
        return min['value']
    return None
    
    
def sink(my_heap, pos):
    """Deja en la posición correcta un elemento ubicado en la raíz del heap
Se realiza un recorrido hacia abajo en el heap, comparando el elemento con sus hijos. 
Si el elemento tiene menor prioridad que alguno de sus hijos, se intercambian los elementos 
y se continúa el recorrido hacia abajo.
Nota
Esta función es utilizada por la función remove() para dejar el elemento en la posición correcta.
Parameters:
        my_heap (priority_queue) – El heap sobre el cual se realiza la operación
        pos (int) – La posición del elemento a revisar
    """
    size = my_heap['size']

    while 2 * pos <= size:
        j = 2 * pos
        if j < size:
            left = lt.get_element(my_heap['elements'], j)
            right = lt.get_element(my_heap['elements'], j + 1)
            if priority(my_heap, left, right):
                j += 1
        if priority(my_heap, lt.get_element(my_heap['elements'], pos), lt.get_element(my_heap['elements'], j)):
            break
        lt.exchange(my_heap['elements'], pos, j)
        pos = j
