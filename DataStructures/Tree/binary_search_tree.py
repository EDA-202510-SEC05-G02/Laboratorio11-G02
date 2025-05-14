from DataStructures.List import array_list as al
from DataStructures.Tree import bst_node as bts
from DataStructures.List import single_linked_list as sl


def new_map():
    """Crea una nueva tabla de simbolos (map) ordenada basada en un árbol binario de búsqueda (BST).
La tabla de simbolos es creada con los siguientes atributos:
    root: raiz del árbol (inicialmente None)
Returns:
    tabla de simbolos creada
    Return type:
    binary_search_tree

    """
    binary_search_tree = {'root': None}
    return binary_search_tree

def put(my_bst, key, value):
    """Agrega un nuevo nodo llave-valor a un árbol binario de búsqueda (BST). Si la llave ya existe, se actualiza el value del nodo.
Esta función llama a la función insert_node para agregar el nodo en la posición correcta del árbol de manera recursiva.
Parameters:
        my_bst (binary_search_tree) – árbol binario de búsqueda donde se quiere agregar el nodo
        key (any) – llave del nodo
        value (any) – valor del nodo
Returns:
    árbol binario de búsqueda actualizado
Return type:
    binary_search_tree
    """
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst 

def insert_node(root, key, value):
    """    Inserta un nuevo nodo llave-valor en el árbol binario de búsqueda (BST) de manera recursiva.
    Esta función es llamada por la función put.
    Parameters:
            root (bst_node) – raiz del árbol donde se quiere agregar el nodo
            key (any) – llave del nodo
            value (any) – valor del nodo
    Returns:
        raiz del árbol binario de búsqueda actualizado
    Return type:
        bst_node
    """
    if root is None:
        return bts.new_node(key, value)

    if key < bts.get_key(root):
         root["left"] = insert_node(root["left"], key, value)
    elif key > bts.get_key(root):
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value
        
    left_size = root["left"]["size"] if root["left"] is not None else 0
    right_size = root["right"]["size"] if root["right"] is not None else 0
    root["size"] = 1 + left_size + right_size
    
    return root
    
def get(my_bst, key):
    """Busca un nodo en el árbol binario de búsqueda (BST) y devuelve su valor.
Esta función llama a la función get_node para buscar el nodo en el árbol de manera recursiva.
Parameters:
        my_bst (binary_search_tree) – árbol binario de búsqueda donde se quiere buscar el nodo
        key (any) – llave del nodo a buscar
Returns:
    valor del nodo encontrado o None si no se encuentra
Return type:
    any
    """
    
    return bts.get_value(get_node(my_bst["root"], key))
   

def get_node(root, key):
    """    Busca un nodo en el árbol binario de búsqueda (BST) de manera recursiva.
    Esta función es llamada por la función get.
    Parameters:
            root (bst_node) – raiz del árbol donde se quiere buscar el nodo
            key (any) – llave del nodo a buscar
    Returns:
        nodo encontrado o None si no se encuentra
    Return type:
        bst_node
    """
    if root is None:
        return None

    if key < bts.get_key(root):
        return get_node(root["left"], key)
    elif key > bts.get_key(root):
        return get_node(root["right"], key)
    else:
        return root

def remove(my_bst, key):
    """    Elimina la pareja llave-valor que coincida con``key``.
    Usa la función remove_node() para eliminar la pareja
    Parameters:
            my_bst (binary_search_tree) – El arbol de búsqueda
            key (any) – La llave asociada a la pareja a eliminar
    Returns:
        El arbol sin la pareja key-value
    Return type:
        binary_search_tree
    """
    
    my_bst["root"] = remove_node(my_bst["root"], key)
    return my_bst


def remove_node(root, key):
    """
    Elimina la pareja llave-valor que coincida con``key``.
    Es usada en la función remove()
    Parameters:
            root (bst_node) – La raiz del arbol a examinar
            key (any) – La llave asociada a la pareja a eliminar
    Returns:            El arbol sin la pareja key-value
    Return type:        bst_node

    """
    if root is None:
        return None

    if key < bts.get_key(root):
        root["left"] = remove_node(root["left"], key)
    elif key > bts.get_key(root):
        root["right"] = remove_node(root["right"], key)
    else:
        if root["right"] is None:
            return root["left"]
        if root["left"] is None:
            return root["right"]
        root_copia = root
        min_node = get_min_node(root_copia["right"]) 
        root = bts.new_node(min_node["key"], min_node["value"]) 
        root["right"] = delete_min_tree(root_copia["right"])  
        root["left"] = root_copia["left"]


    left_size = root["left"]["size"] if root["left"] else 0
    right_size = root["right"]["size"] if root["right"] else 0
    root["size"] = 1 + left_size + right_size

    return root

def contains(my_bst, key):
    """
    Informa si la llave key se encuentra en la tabla de hash.
    Usa la función get() para buscar la llave en el arbol
    Parameters:
            my_bst (binary_search_tree) – El arbol de búsqueda
            key (any) – La llave a buscar
    Returns:
        True si la llave está presente, False en caso contrario
    Return type:
        bool
"""
    return get(my_bst, key) is not None

def size(my_bst):
    """    Retorna el número de entradas en la tabla de simbolos
    Usa la función size_tree() para contar el número de elementos
    Parameters:
        my_bst (binary_search_tree) – El arbol de búsqueda
    Returns:
        El número de elementos en la tabla
    Return type:
        int
    """
    return size_tree(my_bst["root"])


def size_tree(root):
    """    Retornar el número de entradas en la a partir del nodo root
    Es usada en la función size()
    Parameters:
        root (bst_node) – La raiz del arbol a examinar
    Returns:
        El número de elementos en la tabla
    Return type:
        int
    """
    if root is None:
        return 0
    return root["size"]

def is_empty(my_bst):
    """    Informa si la tabla de simbolos se encuentra vacia.
    Parameters:
        my_bst (binary_search_tree) – El arbol de búsqueda
    Returns:
        True si la tabla es vacía, False en caso contrario
    Return type:
        bool
    """
    return my_bst["root"] is None

def key_set_tree(root, listirijilla):
    if root is None:
        return
    key_set_tree(root["left"], listirijilla)
    sl.add_last(listirijilla, bts.get_key(root))
    key_set_tree(root["right"], listirijilla)
    
def key_set(my_bst):
    """    Retorna una lista con todas las llaves de la tabla.
    Usa la función key_set_tree() para construir la lista de llaves
    Parameters:
        my_bst (binary_search_tree) – El arbol de búsqueda
    Returns:
        Una lista con todas las llaves de la tabla
    Return type:
        single_linked_list
    """
    listirijilla = sl.new_list()
    key_set_tree(my_bst["root"], listirijilla)
    return listirijilla
    

def value_set_tree(root, valorsillos):
    if root is None:
        return
    value_set_tree(root["left"], valorsillos)
    sl.add_last(valorsillos, bts.get_value(root))
    value_set_tree(root["right"], valorsillos)
    
def value_set(my_bst):
    """    Retorna una lista con los valores de la tabla.
    Usa la función value_set_tree() para construir la lista de valores
    Parameters:
        my_bst (binary_search_tree) – El arbol de búsqueda
    Returns:
        Una lista con todos los valores de la tabla
    Return type:
        single_linked_list
    """
    valorsillos = sl.new_list()
    value_set_tree(my_bst["root"], valorsillos)
    return valorsillos

def get_min(my_bst):
    """    Retorna la llave mas pequeña de la tabla de simbolos
    Usa la función get_min_node() para encontrar la llave más a la izquierda
    Parameters:
        my_bst (binary_search_tree) – El arbol de búsqueda
    Returns:
        La llave más a la izquierda
    Return type:
        any
    """
    node = get_min_node(my_bst["root"])
    return node["key"] if node else None

def get_min_node(root):
    """Retorna la llave mas pequeña de la tabla de simbolos
    Es usada en la función get_min()
    Parameters:
        root (bst_node) – La raiz del arbol a examinar
    Returns:
        La llave más a la izquierda
    Return type:
        any
    """
    if root is None or root["left"] is None:
        return root
    return get_min_node(root["left"])

def get_max(my_bst):
    """    Retorna la llave mas grande de la tabla de simbolos
    Usa la función get_max_node() para encontrar la llave más grande de del arbol
    Parameters:
        my_bst (binary_search_tree) – El arbol de búsqueda
    Returns:
        La llave más a la derecha
    Return type:
        any
    """
    node = get_max_node(my_bst["root"])
    return node["key"] if node else None

def get_max_node(root):
    """    Retorna la llave mas grande de la tabla de simbolos
    Es usada en la función get_max() Usa la función get_max_node() para encontrar la llave más grande
    Parameters:
        root (bst_node) – La raiz del arbol a examinar
    Returns:
        La llave más a la derecha
    Return type:
        any
    """
    if root is None or root["right"] is None:
        return root
    return get_max_node(root["right"])


def delete_min(my_bst):
    """    Encuentra y remueve la llave mas pequeña de la tabla de simbolos y su valor asociado.
    Usa la función delete_min_tree() para eliminar la llave más pequeña
    Parameters:
        my_bst (binary_search_tree) – El arbol de búsqueda
    Returns:
        El arbol de búsqueda sin la llave más pequeña
    Return type:
        binary_search_tree
    """
    my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst

def delete_min_tree(root):
    """    Encuentra y remueve la llave mas pequeña de la tabla de simbolos y su valor asociado
    Es usada en la función delete_min() Usa la función delete_min_tree() para eliminar la llave más pequeña
    Parameters:
        root (bst_node) – La raiz del arbol a examinar
    Returns:
        Retorna la raiz del arbol sin la llave más pequeña
    Return type:
        bst_node
    """
    if root is None:
        return None
    if root["left"] is None:
        return root["right"]

    root["left"] = delete_min_tree(root["left"])
    
    left_size = root["left"]["size"] if root["left"] else 0
    right_size = root["right"]["size"] if root["right"] else 0
    root["size"] = 1 + left_size + right_size
    return root

def delete_max(my_bst):
    """    Encuentra y remueve la llave mas grande de la tabla de simbolos y su valor asociado.
    Usa la función delete_max_tree() para eliminar la llave más grande
    Parameters:
        my_bst (binary_search_tree) – El arbol de búsqueda
    Returns:
        El arbol de búsqueda sin la llave más grande
    Return type:
        binary_search_tree
    """
    my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst

def delete_max_tree(root):
    """    Encuentra y remueve la llave mas grande de la tabla de simbolos y su valor asociado.
    Es usada en la función delete_max() Usa la función delete_max_tree() para eliminar la llave más grande
    Parameters:
        root (bst_node) – La raiz del arbol a examinar
    Returns:
        Retorna la raiz del arbol sin la llave más grande
    Return type:
        bst_node
    """
    if root is None:
        return None
    if root["right"] is None:
        return root["left"]

    root["right"] = delete_max_tree(root["right"])
    
    left_size = root["left"]["size"] if root["left"] else 0
    right_size = root["right"]["size"] if root["right"] else 0
    root["size"] = 1 + left_size + right_size
    return root

def floor(my_bst, key):
    """    Retorna la llave que precede a la llave key en la tabla de simbolos.
    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave predecedente más 
    cercana como si la llave key existiera en la tabla.
    Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 5.
    Usa la función floor_key() para encontrar la llave predecesora a key
    Parameters:
            my_bst (binary_search_tree) – El arbol de búsqueda
            key (any) – La llave de búsqueda
    Returns:
        La llave predecesora a key
    Return type:
        any
    """
    return bts.get_key(floor_key(my_bst["root"], key))

def floor_key(root, key):
    """    Retorna la llave que precede a la llave key en la tabla de simbolos.
    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave predecedente 
    más cercana como si la llave key existiera en la tabla.
    Es usada en la función floor() Usa la función floor_key() para encontrar la llave predecesora a key
    Parameters:
            root (bst_node) – La raiz del arbol a examinar
            key (any) – La llave de búsqueda
    Returns:
        La llave predecesora a key
    Return type:
        any
    """
    if root is None:
        return None
    if key == bts.get_key(root):
        return root
    elif key < bts.get_key(root):
        return floor_key(root["left"], key)
    else:
        resultado = floor_key(root["right"], key)
        return resultado 
    
    
def ceiling(my_bst, key):
    """    Retorna la llave que sucede a la llave key en la tabla de simbolos.
    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave sucesora más cercana como si la 
    llave key existiera en la tabla. Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6,
    la función retornará 7.
    Usa la función ceiling_key() para encontrar la llave sucesora a key
    Parameters:
            my_bst (binary_search_tree) – El arbol de búsqueda
            key (any) – La llave de búsqueda
    Returns:
        La llave sucesora a key
    Return type:
        any
    """
    return bts.get_key(ceiling_key(my_bst["root"], key))

def ceiling_key(root, key):
    """    Retorna la llave que sucede a la llave key en la tabla de simbolos.
    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave sucesora más cercana como si la llave key existiera en la tabla. 
    Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 7.
    Es usada en la función ceiling() Usa la función ceiling_key() para encontrar la llave sucesora a key
    Parameters:
            root (bst_node) – La raiz del arbol a examinar
            key (any) – La llave de búsqueda
    Returns:
        La llave sucesora a key
    Return type:
        any
    """
    if root is None:
        return None
    if key == bts.get_key(root):
        return root
    elif key > bts.get_key(root):
        return ceiling_key(root["right"], key)
    else:
        resultado = ceiling_key(root["left"], key)
        return resultado 

def select(my_bst, pos):
    """    Retorna la siguiente llave a la k-esima llave de izquierda a derecha de la tabla de simbolos.
    Usa la función select_key() para encontrar la llave en la posición pos
    Parameters:
            my_bst (binary_search_tree) – El arbol de búsqueda
            pos (int) – la pos-esima llave de izquierda a derecha
    Returns:
        La llave en la posición pos
    Return type:
        any
    """
    return bts.get_key(select_key(my_bst["root"], pos)) 

def select_key(root, key):
    """    Retorna la siguiente llave a la k-esima llave de izquierda a derecha de la tabla de simbolos.
    Es usada en la función select() Usa la función select_key() para encontrar la llave en la posición pos
    Parameters:
            root (bst_node) – La raiz del arbol a examinar
            key (int) – la llave de búsqueda
    Returns:
        La llave en la posición pos
    Return type:
        bst_node
    """
    if root is None:
        return None
    llave_izquierda = root["left"]["size"] if root["left"] else 0
    if key < llave_izquierda:
        return select_key(root["left"], key)
    elif key > llave_izquierda:
        return select_key(root["right"], key - llave_izquierda - 1)
    else:
        return root

def rank(my_bst, key):
    """    Retorna el número de llaves en la tabla que son estrictamente predecesoras 
    a key Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 3.
    Usa la función rank_keys() para encontrar el número de llaves predecesoras a key
    Parameters:
            my_bst (binary_search_tree) – El arbol de búsqueda
            key (any) – la llave de busqueda
    Returns:
        El número de llaves
    Return type:
        int
    """
    return rank_keys(my_bst["root"], key)

def rank_keys(root, key):
    """    Retorna el número de llaves en la tabla que son estrictamente predecesoras a key Por ejemplo, 
    si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 3.
    Es usada en la función rank() Usa la función rank_keys() para encontrar el número de llaves predecesoras a key
    Parameters:
            root (bst_node) – La raiz del arbol a examinar
            key (any) – la llave de busqueda
    Returns:
        El número de llaves
    Return type:
        int
    """
    if root is None:
        return 0
    if key < bts.get_key(root):
        return rank_keys(root["left"], key)
    elif key > bts.get_key(root):
        left_size = root["left"]["size"] if root["left"] else 0
        return 1 + left_size + rank_keys(root["right"], key)
    else:
        return root["left"]["size"] if root["left"] else 0

def height(my_bst):
    """    Retorna la altura del arbol de busqueda
    Usa la función height_tree() para encontrar la altura del arbol
    Parameters:
        my_bst (binary_search_tree) – El arbol de búsqueda
    Returns:
        La altura del arbol
    Return type:
        int
    """
    return height_tree(my_bst["root"])

def height_tree(root):
    """    Retorna la altura del arbol de busqueda
    Es usada en la función height() Usa la función height_tree() para encontrar la altura del arbol
    Parameters:
        root (bst_node) – La raiz del arbol a examinar
    Returns:
        La altura del arbol
    Return type:
        int
    """
    if root is None:
        return 0
    return 1 + max(height_tree(root["left"]), height_tree(root["right"]))

def keys(my_bst,key_initial, key_final):
    """    Retorna todas las llaves del arbol que se encuentren entre [key_initial, key_final].
    Usa la función keys_range() para encontrar las llaves en el rango especificado
    Parameters:
            my_bst (binary_search_tree) – La tabla de simbolos
            key_initial (any) – limite inferior
            key_final (any) – limite superior
    Returns:
        Las llaves en el rago especificado
    Return type:
        single_linked_list
    """
    single_linked_list = sl.new_list()
    keys_range(my_bst["root"], key_initial, key_final, single_linked_list)
    return single_linked_list

def keys_range(root, key_initial, key_final, list_key):
    """    Retorna todas las llaves del arbol que se encuentren entre [key_initial, key_final].
    Es usada en la función keys() Usa la función keys_range() para encontrar las llaves en el rango especificado
    Parameters:
            root (bst_node) – La raiz del arbol a examinar
            key_initial (any) – limite inferior
            key_final (any) – limite superior
            list_key (single_linked_list) – La lista de respuesta
    Returns:
        Las llaves en el rago especificado
    Return type:
        single_linked_list
    """
    if root is None:
        return
    key = root["key"]
    if key > key_initial:
        keys_range(root["left"], key_initial, key_final, list_key)
    if key_initial <= key <= key_final:
        sl.add_last(list_key, root["value"])
    if key < key_final:
        keys_range(root["right"], key_initial, key_final, list_key)


def values(my_bst, key_initial, key_final):
    """    Retorna todas los valores del arbol que se encuentren entre [key_initial, key_final]
    Usa la función values_range() para encontrar los valores en el rango especificado
    Parameters:
            my_bst (binary_search_tree) – La tabla de simbolos
            key_initial (any) – limite inferior
            key_final (any) – limite superior
    Returns:
        Las llaves en el rago especificado
    Return type:
        single_linked_list
    """
    values_list = sl.new_list()
    keys_range(my_bst["root"], key_initial, key_final, values_list)
    return values_list

def default_compare(key, element):
    """Función de comparación por defecto. Compara una llave con la llave de un elemento llave-valor.
Parameters:
        key (any) – Llave a comparar
        element (bst_node) – entry a comparar
Returns:
    0 si son iguales, 1 si key > la llave del element, -1 si key < que la llave del element
Return type:
    int
    """
    if key == bts.get_key(element):
      return 0
    elif key > bts.get_key(element):
      return 1
    return -1