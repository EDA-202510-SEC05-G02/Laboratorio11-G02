from DataStructures.Tree import rbt_node as rbt
from DataStructures.List import single_linked_list as sl

def new_map():
    """
    Crea una tabla de simbolos ordenada basa en un árbol rojo-negro (RBT) vacia
    Se crea una tabla de simbolos ordenada con los siguientes atributos:
        root: Raíz del árbol. Inicializado en None
        type: Tipo de árbol. Inicializado en “RBT”
    Returns:
        La tabla de simbolos ordenada sin elementos
    Return type:
        red_black_tree
    """
    red_black_tree = {
        'root': None,
        'type': 'RBT'
    }
    return red_black_tree

def put(my_rbt, key, value):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe, 
    se reemplaza el valor. Usa la funcion insert_node()
    Parameters:
            my_rbt (red_black_tree) – El RBT
            key (any) – La llave asociada a la pareja
            value (any) – El valor asociado a la pareja
    Returns:
        El arbol con la nueva pareja
    Return type:
        red_black_tree
    """
    my_rbt["root"] = insert_node(my_rbt["root"], key, value)
    return my_rbt 


def insert_node(root, key, value):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe, 
    se reemplaza el valor. Es usada en la función insert()
    Parameters:
            root (rbt_node) – La raiz del arbol
            key (any) – La llave asociada a la pareja
            value (any) – El valor asociado a la pareja
    Returns:
        El arbol con la nueva pareja
    Return type:
        rbt_node
    """
    if root is None:
        return rbt.new_node(key, value)

    if key < rbt.get_key(root):
         root["left"] = insert_node(root["left"], key, value)
    elif key > rbt.get_key(root):
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value
        
    left_size = root["left"]["size"] if root["left"] is not None else 0
    right_size = root["right"]["size"] if root["right"] is not None else 0
    root["size"] = 1 + left_size + right_size
    
    return root

def get(my_rbt, key):
    """
    Retorna el valor con llave igual a key
    Usa la función get_node() para buscar la llave en el arbol
    Parameters:
            my_rbt (reb_black_tree) – El arbol de búsqueda
            key (any) – La llave asociada a la pareja
    Returns:
        La pareja el valor de la llave key. None en caso 
        de no ser encontrada
    Return type:
        any
    """
    return rbt.get_value(get_node(my_rbt["root"], key))

def get_node(root, key):
    """
    Retorna el valor de la llave igual a key
    Parameters:
            root (rbt_node) – La raiz del arbol
            key (any) – La llave asociada a la pareja a buscar
    Returns:
        El valor de la llave key. None en caso de no ser encontrada
    """
    if root is None:
        return None

    if key < rbt.get_key(root):
        return get_node(root["left"], key)
    elif key > rbt.get_key(root):
        return get_node(root["right"], key)
    else:
        return root

def remove(my_rbt, key):
    """
    Elimina la pareja llave-valor que coincida con``key``.
    Usa la función remove_node() para eliminar la pareja
    Parameters:
            my_rbt (reb_black_tree) – El arbol de búsqueda
            key (any) – La llave asociada a la pareja a eliminar
    Returns:
        El arbol sin la pareja key-value
    Return type:
        reb_black_tree
    """
    my_rbt["root"] = remove_node(my_rbt["root"], key)
    if my_rbt["root"]:
        my_rbt["root"]["color"] = "black"
    return my_rbt

def remove_node(root, key):
    """
    Elimina la pareja llave-valor que coincida con``key``.
    Es usada en la función remove() Usa la funcion remove_node()
    Parameters:
            root (rbt_node) – La raiz del arbol a examinar
            key (any) – La llave asociada a la pareja a eliminar
    Returns:
        El arbol sin la pareja key-value
    Return type:
        rbt_node
    """
    if root is None:
        return None

    if key < rbt.get_key(root):
        if not is_red(root["left"]):
            if not is_red(root["left"].get("left")):
                root = move_red_left(root)
        root["left"] = remove_node(root["left"], key)
    
    else:
        if is_red(root["left"]):
            root = rotate_right(root)
        if key == rbt.get_key(root) and root["right"] is None:
            return None
        if not is_red(root["right"]):
            if not is_red(root["right"].get("left")):
                root = move_red_right(root)
            root = move_red_right(root)
        if key == rbt.get_key(root):
            min_node = get_min_node(root["right"])
            root["key"] = min_node["key"]
            root["value"] = min_node["value"]
            root["right"] = delete_min_node(root["right"])
        else:
            root["right"] = remove_node(root["right"], key)

    left_size = root["left"]["size"] if root.get("left") else 0
    right_size = root["right"]["size"] if root.get("right") else 0
    root["size"] = 1 + left_size + right_size

    return balance(root)
    

def contains(my_rbt, key):
    """
    Informa si la llave key se encuentra en la tabla de hash.
    Usa la función get() para buscar la llave en el arbol
    Parameters:
            my_rbt (reb_black_tree) – El arbol de búsqueda
            key (any) – La llave a buscar
    Returns:
        True si la llave está presente, False en caso contrario
    Return type:
        bool
    """
    return get(my_rbt, key) is not None

def size(my_rbt):
    """
    Retorna el número de entradas en la tabla de simbolos
    Usa la función size_tree() para contar el número de elementos
    Parameters:
        my_rbt (reb_black_tree) – El arbol de búsqueda
    Returns:
        El número de elementos en la tabla
    Return type:
        int
    """
    return size_tree(my_rbt["root"])

def is_empty(my_rbt):
    """
    Informa si la tabla de simbolos se encuentra vacia.
    Parameters:
        my_rbt (reb_black_tree) – El arbol de búsqueda
    Returns:
        True si la tabla es vacía, False en caso contrario
    Return type:
        bool
    """
    return my_rbt["root"] is None

def key_set(my_rbt):
    """
    Retorna una lista con todas las llaves de la tabla.
    Usa la función key_set_tree() para construir la lista de llaves
    Parameters:
        my_rbt (reb_black_tree) – El arbol de búsqueda
    Returns:
        Una lista con todas las llaves de la tabla
    Return type:
        single_linked_list
    """
    key_list = sl.new_list()
    key_set_tree(my_rbt["root"], key_list)
    return key_list

def key_set_tree(root, key_list):
    """
    Construye una lista con las llaves de la tabla. Se recorre
    el arbol en inorder Es usada en la función key_set()
    Si root no es None, se recorre el arbol en inorder, primero 
    el hijo izquierdo, luego la raiz y finalmente el hijo derecho
    Parameters:
            root (rbt_node) – La raiz del arbol a examinar
            key_list (single_linked_list) – La lista de respuesta
    Returns:
        Una lista con todos las llaves
    Return type:
        single_linked_list
    """
    if root is None:
        return
    key_set_tree(root["left"], key_list)
    sl.add_last(key_list, rbt.get_key(root))
    key_set_tree(root["right"], key_list)

def value_set(my_rbt):
    """
    Retorna una lista con los valores de la tabla.
    Usa la función value_set_tree() para construir la lista de valores
    Parameters:
        my_rbt (reb_black_tree) – El arbol de búsqueda
    Returns:
        Una lista con todos los valores de la tabla
    Return type:
        single_linked_list
    """
    key_list = sl.new_list()
    value_set_tree(my_rbt["root"], key_list)
    return key_list

def value_set_tree(root, key_list):
    """
    Construye una lista con los valorers de la tabla. 
    Se recorre el arbol en inorder Es usada en la función value_set()
    Si root no es None, se recorre el arbol en inorder, primero el 
    hijo izquierdo, luego la raiz y finalmente el hijo derecho
    Parameters:
            root (rbt_node) – La raiz del arbol a examinar
            value_list (single_linked_list) – La lista de respuesta
    Returns:
        Una lista con todos los valores
    Return type:
        single_linked_list
    """
    if root is None:
        return
    value_set_tree(root["left"], key_list)
    sl.add_last(key_list, rbt.get_value(root))
    value_set_tree(root["right"], key_list)


def get_min(my_rbt):
    """
    Retorna la llave mas a la izquierda de la tabla de simbolos
    Important
    Dependiendo de la definición de la función de comparación, 
    la llave más a la izquierda puede ser la menor o la mayor.
    Usa la función left_key_node() para encontrar la llave más a la izquierda
    Parameters:
        my_rbt (reb_black_tree) – El arbol de búsqueda
    Returns:
        La llave más a la izquierda
    Return type:
        any
    """
    node = get_min_node(my_rbt["root"])
    return node["key"] if node else None

def get_min_node(root):
    """
    Retorna la llave mas a la izquierda de la tabla de simbolos
    Important
    Dependiendo de la definición de la función de comparación, 
    la llave más a la izquierda puede ser la menor o la mayor.
    Es usada en la función get_min() Usa la función left_key_tree() 
    para encontrar la llave más a la izquierda
    Parameters:
        root (rbt_node) – La raiz del arbol a examinar
    Returns:
        La llave más a la izquierda
    Return type:
        any
    """
    if root is None or root["left"] is None:
        return root
    return get_min_node(root["left"])

def get_max(my_rbt):
    """
    Retorna la llave mas a la derecha de la tabla de simbolos
    Important
    Dependiendo de la definición de la función de comparación, 
    la llave más a la derecha puede ser la menor o la mayor.
    Usa la función right_key_node() para encontrar la llave más
    a la derecha del arbol
    Parameters:
        my_rbt (reb_black_tree) – El arbol de búsqueda
    Returns:
        La llave más a la derecha
    Return type:
        any
    """
    node = get_max_node(my_rbt["root"])
    return node["key"] if node else None

def get_max_node(root):
    """
    Retorna la llave mas a la derecha de la tabla de simbolos
    Important
    Dependiendo de la definición de la función de comparación, 
    la llave más a la derecha puede ser la menor o la mayor.
    Es usada en la función get_max() Usa la función get_max_node() 
    para encontrar la llave más a la derecha
    Parameters:
        root (rbt_node) – La raiz del arbol a examinar
    Returns:
        La llave más a la derecha
    Return type:
        any
    """
    if root is None or root["right"] is None:
        return root
    return get_max_node(root["right"])

def delete_min(my_rbt):
    """
    Encuentra y remueve la llave mas a la izauierda de la tabla 
    de simbolos y su valor asociado.
    Important
    Dependiendo de la definición de la función de comparación, la 
    llave más a la izquierda puede ser la menor o la mayor.
    Usa la función delete_min_node() para eliminar la llave más a la izquierda
    Parameters:
        my_rbt (reb_black_tree) – El arbol de búsqueda
    Returns:
        El arbol de búsqueda sin la llave más a la izquierda
    Return type:
        reb_black_tree
    """
    if not is_red(my_rbt["root"]["left"]):
        if not is_red(my_rbt["root"]["right"]):
            my_rbt["root"]["color"] = "red"
    my_rbt["root"] = delete_min_node(my_rbt["root"])
    
    if my_rbt["root"]:
        my_rbt["root"]["color"] = "black"
    return my_rbt

def delete_min_node(root):
    """Encuentra y remueve la llave mas a la izquierda de la tabla de simbolos 
    y su valor asociado.
    Important
    Dependiendo de la definición de la función de comparación, la llave más a 
    la izquierda puede ser la menor o la mayor.
    Es usada en la función delete_max() Usa la función delete_max_node() 
    para eliminar la llave más a la izquierda
    Parameters:
        root (rbt_node) – La raiz del arbol a examinar
    Returns:
        Retorna la raiz del arbol sin la llave más a la izquierda
    Return type:
        rbt_node
    """
    if root["left"] is None:
        return root["right"]

    if not is_red(root["left"]):
        if not is_red(root["left"]["left"]):
            root = move_red_left(root)

    root["left"] = delete_min_node(root["left"])
    
    left_size = root["left"]["size"] if root["left"] else 0
    right_size = root["right"]["size"] if root["right"] else 0
    root["size"] = 1 + left_size + right_size

    return balance(root)

def delete_max(my_rbt):
    """
    Encuentra y remueve la llave mas a la derecha de la tabla 
    de simbolos y su valor asociado.
    Important
    Dependiendo de la definición de la función de comparación, la 
    llave más a la derecha puede ser la menor o la mayor.
    Usa la función delete_max_node() para eliminar la llave más a 
    la derecha
    Parameters:
        my_rbt (reb_black_tree) – El arbol de búsqueda
    Returns:
        El arbol de búsqueda sin la llave más a la derecha
    Return type:
        reb_black_tree
    """
    if my_rbt["root"] is None:
        return my_rbt
    
    if not is_red(my_rbt["root"]["right"]):
        if not is_red(my_rbt["root"]["left"]):
            my_rbt["root"]["color"] = "red"
    my_rbt["root"] = delete_max_node(my_rbt["root"])
    
    if my_rbt["root"]:
        my_rbt["root"]["color"] = "black"
    return my_rbt

def delete_max_node(root):
    """
    Encuentra y remueve la llave mas a la derecha de la tabla de 
    simbolos y su valor asociado.
    Important
    Dependiendo de la definición de la función de comparación, la 
    llave más a la derecha puede ser la menor o la mayor.
    Es usada en la función delete_max() Usa la función delete_max_node() 
    para eliminar la llave más a la derecha
    Parameters:
        root (rbt_node) – La raiz del arbol a examinar
    Returns:
        Retorna la raiz del arbol sin la llave más a la derecha
    Return type:
        rbt_node
    """ 
    if root["right"] is None:
        return root["left"]

    if not is_red(root["right"]):
        if not is_red(root["right"]["right"]):
            root = move_red_right(root)

    root["right"] = delete_max_node(root["right"])
    
    left_size = root["left"]["size"] if root["left"] else 0
    right_size = root["right"]["size"] if root["right"] else 0
    root["size"] = 1 + left_size + right_size

    return balance(root)

def floor(my_rbt, key):
    """
    Retorna la llave que precede a la llave key en la tabla de simbolos.
    Si la llave existe, retorna la misma llave. Si no existe, retorna la 
    llave predecedente más cercana como si la llave key existiera en la tabla. 
    Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la 
    llave 6, la función retornará 5.
    Usa la función floor_key() para encontrar la llave predecesora a key
    Parameters:
            my_rbt (reb_black_tree) – El arbol de búsqueda
            key (any) – La llave de búsqueda
    Returns:
        La llave predecesora a key
    Return type:
        any
    """
    return rbt.get_key(floor_key(my_rbt["root"], key))

def floor_key(root, key):
    """
    Retorna la llave que precede a la llave key en la tabla de simbolos.
    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave 
    predecedente más cercana como si la llave key existiera en la tabla.
    Es usada en la función floor() Usa la función floor_key() para encontrar la 
    llave predecesora a key
    Parameters:
            root (rbt_node) – La raiz del arbol a examinar
            key (any) – La llave de búsqueda
    Returns:
        La llave predecesora a key
    Return type:
        any
    """
    if root is None:
        return None
    if key == rbt.get_key(root):
        return root
    elif key < rbt.get_key(root):
        return floor_key(root["left"], key)
    else:
        resultado = floor_key(root["right"], key)
        if resultado is not None:
            return resultado
        else:
            return root
    
def ceiling(my_rbt, key):
    """
    Retorna la llave que sucede a la llave key en la tabla de simbolos.
    Si la llave existe, retorna la misma llave. Si no existe, retorna 
    la llave sucesora más cercana como si la llave key existiera en la 
    tabla. Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] 
    y se busca la llave 6, la función retornará 7.
    Usa la función ceiling_key() para encontrar la llave sucesora a key
    Parameters:
            my_rbt (reb_black_tree) – El arbol de búsqueda
            key (any) – La llave de búsqueda
    Returns:
        La llave sucesora a key
    Return type:
        any
    """
    return rbt.get_key(ceiling_key(my_rbt["root"], key))

def ceiling_key(root, key):
    """
    Retorna la llave que sucede a la llave key en la tabla de simbolos.
    Si la llave existe, retorna la misma llave. Si no existe, retorna la 
    llave sucesora más cercana como si la llave key existiera en la tabla. 
    Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca 
    la llave 6, la función retornará 7.
    Es usada en la función ceiling() Usa la función ceiling_key() para encontrar 
    la llave sucesora a key
    Parameters:
            root (rbt_node) – La raiz del arbol a examinar
            key (any) – La llave de búsqueda
    Returns:
        La llave sucesora a key
    Return type:
        any
    """
    if root is None:
        return None
    if key == rbt.get_key(root):
        return root
    elif key > rbt.get_key(root):
        return ceiling_key(root["right"], key)
    else:
        resultado = ceiling_key(root["left"], key)
        if resultado is not None:
            return resultado
        else:
            return root

def select(my_rbt, pos):
    """
    Retorna la siguiente llave a la k-esima llave de izquierda a 
    derecha de la tabla de simbolos.
    Usa la función select_key() para encontrar la llave en la 
    posición pos
    Parameters:
            my_rbt (reb_black_tree) – El arbol de búsqueda
            pos (int) – la pos-esima llave de izquierda a derecha
    Returns:
        La llave en la posición pos
    Return type:
        any
    """
    return rbt.get_key(select_key(my_rbt["root"], pos)) 

def select_key(root, key):
    """
    Retorna la siguiente llave a la k-esima llave de izquierda a derecha 
    de la tabla de simbolos.
    Es usada en la función select() Usa la función select_key() para encontrar 
    la llave en la posición pos
    Parameters:
            root (rbt_node) – La raiz del arbol a examinar
            key (int) – la llave de búsqueda
    Returns:
        La llave en la posición pos
    Return type:
        rbt_node
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

def rank(my_rbt, key):
    """
    Retorna el número de llaves en la tabla que son estrictamente 
    predecesoras a key Por ejemplo, si la tabla contiene las llaves 
    [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 3.
    Usa la función rank_keys() para encontrar el número de llaves 
    predecesoras a key
    Parameters:
            my_rbt (reb_black_tree) – El arbol de búsqueda
            key (any) – la llave de busqueda
    Returns:
        El número de llaves
    Return type:
        int
    """
    return rank_keys(my_rbt["root"], key)

def rank_keys(root, key):
    """
    Retorna el número de llaves en la tabla que son estrictamente 
    predecesoras a key Por ejemplo, si la tabla contiene las llaves 
    [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 3.
    Es usada en la función rank() Usa la función rank_keys() para encontrar 
    el número de llaves predecesoras a key
    Parameters:
            root (rbt_node) – La raiz del arbol a examinar
            key (any) – la llave de busqueda
    Returns:
        El número de llaves
    Return type:
        int
    """
    if root is None:
        return 0
    if key < rbt.get_key(root):
        return rank_keys(root["left"], key)
    elif key > rbt.get_key(root):
        left_size = root["left"]["size"] if root["left"] else 0
        return 1 + left_size + rank_keys(root["right"], key)
    else:
        return root["left"]["size"] if root["left"] else 0

def height(my_rbt):
    """
    Retorna la altura del arbol de busqueda
    Usa la función height_tree() para encontrar la altura del arbol
    Parameters:
        my_rbt (reb_black_tree) – El arbol de búsqueda
    Returns:
        La altura del arbol
    Return type:
        int
    """
    return height_tree(my_rbt["root"])

def height_tree(root):
    """
    Retorna la altura del arbol de busqueda
    Es usada en la función height() Usa la función height_tree() 
    para encontrar la altura del arbol
    Parameters:
        root (rbt_node) – La raiz del arbol a examinar
    Returns:
        La altura del arbol
    Return type:
        int
    """
    if root is None:
        return 0
    return 1 + max(height_tree(root["left"]), height_tree(root["right"]))

def keys(my_rbt, key_initial, key_final):
    """
    Retorna todas las llaves del arbol que se encuentren entre 
    [key_initial, key_final].
    Important
    Dependiendo de la definición de la función de comparación 
    y del orden de las llaves,  el rango puede ser [key_final, key_initial].
    Si la función de comparación es la función por defecto, el rango es 
    [key_initial, key_final]. Si la función de comparación es la función inversa,
    el rango es [key_final, key_initial].
    Usa la función keys_range() para encontrar las llaves en el rango especificado
    Parameters:
            my_rbt (reb_black_tree) – La tabla de simbolos
            key_initial (any) – limite inferior
            key_final (any) – limite superior
    Returns:
        Las llaves en el rago especificado
    Return type:
        single_linked_list
    """
    single_linked_list = sl.new_list()
    keys_range(my_rbt["root"], key_initial, key_final, single_linked_list)
    return single_linked_list


def keys_range(root, key_initial, key_final, list_key):
    """
    Retorna todas las llaves del arbol que se encuentren entre 
    [key_initial, key_final].
    Important
    Dependiendo de la definición de la función de comparación y del 
    orden de las llaves, el rango puede ser [key_final, key_initial].
    Si la función de comparación es la función por defecto, el rango 
    es [key_initial, key_final]. Si la función de comparación es la 
    función inversa, el rango es [key_final, key_initial].
    Es usada en la función keys() Usa la función keys_range() para 
    encontrar las llaves en el rango especificado
    Parameters:
            root (rbt_node) – La raiz del arbol a examinar
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
        sl.add_last(list_key,  root["key"])
    if key < key_final:
        keys_range(root["right"], key_initial, key_final, list_key)
        
def values(my_rbt, key_initial, key_final):
    """
    Retorna todas los valores del arbol que se encuentren entre 
    [key_initial, key_final]
    Important
    Dependiendo de la definición de la función de comparación y del 
    orden de las llaves, el rango puede ser [key_final, key_initial].
    Si la función de comparación es la función por defecto, el rango es 
    [key_initial, key_final]. Si la función de comparación es la función 
    inversa, el rango es [key_final, key_initial].
    Usa la función values_range() para encontrar los valores en el rango 
    especificado
    Parameters:
            my_rbt (reb_black_tree) – La tabla de simbolos
            key_initial (any) – limite inferior
            key_final (any) – limite superior
    Returns:
        Las llaves en el rago especificado
    Return type:
        single_linked_list
    """
    values_list = sl.new_list()
    values_range(my_rbt["root"], key_initial, key_final, values_list)
    return values_list

def values_range(root, key_initial, key_final, value_list):
    """
    Retorna todas los valores del arbol que se encuentren entre [key_initial, key_final]
    Important
    Dependiendo de la definición de la función de comparación y del orden de las llaves, 
    el rango puede ser [key_final, key_initial].
    Si la función de comparación es la función por defecto, el rango es 
    [key_initial, key_final]. Si la función de comparación es la función 
    inversa, el rango es [key_final, key_initial].
    Es usada en la función values() Usa la función values_range() para 
    encontrar los valores en el rango especificado
    Parameters:
            root (rbt_node) – La raiz del arbol a examinar
            key_lo (any) – limite inferior
            key_hi (any) – limite superior
            list_values (single_linked_list) – La lista de respuesta
    Returns:
        Las llaves en el rago especificado
    Return type:
        single_linked_list
    """
    if root is None:
        return
    key = root["key"]
    if key > key_initial:
        values_range(root["left"], key_initial, key_final, value_list)
    if key_initial <= key <= key_final:
        sl.add_last(value_list, root["value"])
    if key < key_final:
        values_range(root["right"], key_initial, key_final, value_list)

#Segun pipus
def rotate_left(node_rbt):
    """
    Rotación izquierda para compensar dos enlaces rojos consecutivos
    Parameters:
        node_rbt – Nodo raiz del arbol a rotar
    Returns:
        El arbol rotado
    Return type:
        rbt_node
    """
    try:
        temp = node_rbt["right"] 
        node_rbt["right"] = temp["left"]  
        temp["left"] = node_rbt  
        temp["color"] = node_rbt["color"]
        node_rbt["color"] = "red"
        temp["size"] = node_rbt["size"]
        left_size = node_rbt["left"]["size"] if node_rbt["left"] else 0
        right_size = node_rbt["right"]["size"] if node_rbt["right"] else 0
        node_rbt["size"] = 1 + left_size + right_size

        return temp

    except Exception as e:
        print("Error en rotate_left:", e)
        return node_rbt

def rotate_right(node_rbt):
    """
    Rotación a la derecha para compensar un hijo rojo a la derecha
    Parameters:
        node_rbt – Nodo raiz del arbol a rotar
    Returns:
        El arbol rotado
    Return type:
        rbt_node
    """
    try:
        temp = node_rbt["left"]
        node_rbt["left"] = temp["right"]
        temp["right"] = node_rbt
        temp["color"] = node_rbt["color"]
        node_rbt["color"] = "red"
        temp["size"] = node_rbt["size"]

        left_size = node_rbt["left"]["size"] if node_rbt["left"] else 0
        right_size = node_rbt["right"]["size"] if node_rbt["right"] else 0
        node_rbt["size"] = 1 + left_size + right_size

        return temp

    except Exception as e:
        print("Error en rotate_right:", e)
        return node_rbt

def flip_node_color(node_rbt):
    """
    Cambia el color de un nodo
    Parameters:
        node_rbt (rbt_node) – El nodo a cambiar
    Returns:
        El nodo con el color opuesto
    Return type:
        rbt_node
    """
    if node_rbt is not None:
        if node_rbt["color"] == "red":
            node_rbt["color"] = "black"
        else:
            node_rbt["color"] = "red"
    return node_rbt

def flip_colors(node_rbt):
    """
    Cambia el color de un nodo y de sus dos hijos
    Parameters:
        node_rbt (rbt_node) – El nodo a cambiar
    Returns:
        El nodo con el color opuesto
    Return type:
        rbt_node
    """
    flip_node_color(node_rbt)
    flip_node_color(node_rbt["left"])
    flip_node_color(node_rbt["right"])
    return node_rbt

def is_red(node_rbt):
    """
    Indica si un nodo del arbol es rojo
    Parameters:
        node_rbt (rbt_node) – El nodo a examinar
    Returns:
        True si el nodo es rojo, False de lo contrario
    Return type:
        bool
    """
    if node_rbt is None:
        return False
    return node_rbt["color"] == "red"

def size_tree(root):
    """
    Retornar el número de entradas en la a partir del nodo root
    Es usada en la función size()
    Parameters:
        root (rbt_node) – La raiz del arbol a examinar
    Returns:
        El número de elementos en la tabla
    Return type:
        int
    """
    if root is None:
        return 0
    return root["size"]

def move_red_right(root):
    """
    Cambio de color durante el proceso de eliminacion
    Parameters:
        root (rbt_node) – Raiz del arbol
    Returns:
        El arbol con un hijo derecho de root en negro
    """
    flip_colors(root)
    
    if is_red(root["left"]) and is_red(root["left"]["left"]):
        root = rotate_right(root)
        flip_colors(root)
        
    return root

def move_red_left(root):
    """
    Cambio de color durante el proceso de eliminacion
    Parameters:
        root (rbt_node) – Raiz del arbol
    Returns:
        El arbol con el hijo izquierdo de root en negro
    Return type:
        rbt_node
    """
    flip_colors(root)
    
    if is_red(root["right"]) and is_red(root["right"]["left"]):
        root["right"] = rotate_right(root["right"])
        root = rotate_left(root)
        flip_colors(root)
        
    return root

def balance(root):
    """
    Balancea el arbol
    Parameters:
        root (rbt_node) – raiz del arbol
    Returns:
        Raiz con el arbol balanceado
    Return type:
        rbt_node
    """
    if is_red(root["right"]):
        root = rotate_left(root)
        
    if is_red(root["left"]) and is_red(root["left"]["left"]):
        root = rotate_right(root)
        
    if is_red(root["left"]) and is_red(root["right"]):
        flip_colors(root)
    
    left_size = root["left"]["size"] if root["left"] else 0
    right_size = root["right"]["size"] if root["right"] else 0
    root["size"] = 1 + left_size + right_size
    
    return root

def default_compare(key, element):
    """
    Función de comparación por defecto. Compara una llave con 
    la llave de un elemento llave-valor.
    Parameters:
            key (any) – Llave a comparar
            element (rbt_node) – entry a comparar
    Returns:
        0 si son iguales, 1 si key > la llave del element, -1 
        si key < que la llave del element
    Return type:
        int
    """
    if key == rbt.get_key(element):
      return 0
    elif key > rbt.get_key(element):
      return 1
    return -1
