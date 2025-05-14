from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import single_linked_list as lt
from DataStructures.List import array_list as al
import random


def new_map(num_elements, load_factor, prime=109345121):
    """Crea una nueva tabla de simbolos (map) sin elementos.
La tabla de simbolos es creada con los siguientes atributos:
    . prime: Número primo usado para calcular el hash. Inicializado 
    con el valor de prime y en caso de no ser dado, con el valor por defecto de 109345121.
    . capacity: Tamaño de la tabla. Inicializado con el siguiente primo mayor 
    a num_elements/ load_factor.
    . scale: Número entero aleatorio entre 1 y prime- 1.
    . shift: Número entero aleatorio entre 0 y prime- 1.
    . table:  array_list de tamaño capacity inicializada con una single_linked_list en cada uno de elementos.
    . current_factor: Factor de carga actual de la tabla. Inicializado en 0.
    . limit_factor: Factor de carga límite de la tabla antes de hacer un rehash. 
    Inicializado con el valor de load_factor.
    . size: Número de elementos en la tabla. Inicializado en 0.
Args:
        num_elements (int) – Número de elementos que se desean almacenar en la tabla.
        load_factor (float) – Factor de carga límite de la tabla antes de hacer un rehash.
        prime (int) – Número primo utilizado para el cálculo del hash. Por defecto es 109345121.

Returns:
    Tabla recien creada.
Return type:

    map_separate_chaining
    """
    capacity = mf.next_prime(int(num_elements / load_factor))
    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)
    table = [lt.new_list() for _ in range(capacity)]  

    map_separate_chaining = {
        "prime": prime,
        "capacity": capacity,
        "scale": scale,
        "shift": shift,
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
    }
    
    return map_separate_chaining
    
    
def put(my_map, key, value):
    """Agrega una nueva entrada llave-valor a la tabla de hash. Si la llave 
ya existe en la tabla, se actualiza el value de la entrada.

Para agregar un nuevo elemento a la tabla, se realiza el siguiente procedimiento:

    . Calcular el hash de la llave, usando la función hash_value.

    . Se busca la lista en la posición del hash en la tabla.

    . Si la llave ya existe en la lista, se actualiza el valor de la entrada.

    . Si la llave no existe en la lista, se agrega una nueva entrada al final de la lista.

    . Se actualiza el current_factor de la tabla si se agrega una nueva entrada.

    . Si el current_factor supera el limit_factor, se realiza un rehash de la tabla.

    . Se retorna la tabla con la nueva entrada.

Parameters:
        my_map (map_separate_chaining) – Tabla de simbolos a la cual se desea agregar el elemento.
        key (any) – Llave del elemento a agregar.
        value (any) – Valor del elemento a agregar.
Returns:
    Tabla de simbolos con el nuevo elemento agregado.
Return type:
    (map_separate_chaining)


    """
    hash_llave = mf.hash_value(my_map, key)
    posicion = my_map["table"][hash_llave]  
    actualisa = posicion["first"]
    
    while actualisa:
        if me.get_key(actualisa["info"]) == key:
            me.set_value(actualisa["info"], value)  
            return my_map
        actualisa = actualisa["next"]

    lt.add_last(posicion, me.new_map_entry(key, value)) 
     
    my_map["size"] += 1
    my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    if my_map["current_factor"] > my_map["limit_factor"]:
        rehash(my_map)

    return my_map
    
    
def default_compare(key, entry):
    """Funcion de comparacion por defecto. Compara la llave key 
    con la llave de una entry dada.
Parameters:
        key (any) – Llave con la que se desea comparar.
        entry (map_entry) – Entrada de la tabla de simbolos con la que se desea comparar.
Returns:
    0 si son iguales, 1 si key > la llave del entry, -1 si key < que la llave del entry
Return type:
    int

    """
    if (key == me.get_key(entry)):
        return 0
    elif (key > me.get_key(entry)):
        return 1
    return -1


def contains(my_map, key):
    """Verifica si una llave se encuentra en la tabla de simbolos.
Parameters:
        my_map (map_separate_chaining) – Tabla de simbolos en la cual se desea verificar si la llave se encuentra.
        key (any) – Llave que se desea verificar si se encuentra en la tabla.
Returns:
    True si la llave se encuentra en la tabla, False en caso contrario.
Return type:
    bool

    """
    hash_key = mf.hash_value(my_map, key)
    posicion = my_map["table"][hash_key]  

    actualiza = posicion["first"]
    while actualiza:
        if me.get_key(actualiza["info"]) == key:
            return True 
        actualiza = actualiza["next"]

    return False  
    
    
def remove(my_map, key):
    """Elimina una entrada de la tabla de simbolos asociada a una llave dada.
Parameters:
        my_map (map_separate_chaining) – Tabla de simbolos de la cual se desea eliminar una entrada.
        key (any) – Llave de la entrada que se desea eliminar.
Returns:
    Tabla de simbolos con la entrada eliminada.
Return type:
    map_separate_chaining

    """
    hash_key = mf.hash_value(my_map, key)
    posicion = my_map["table"][hash_key] 

    if lt.is_empty(posicion):  
        return my_map  

    anterior = None
    posicion1 = posicion["first"]

    while posicion1:
        if me.get_key(posicion1["info"]) == key:
            if anterior is None:
                posicion["first"] = posicion1["next"]
            else:
                anterior["next"] = posicion1["next"]
            if posicion1 == posicion["last"]:
                posicion["last"] = anterior
            my_map["size"] -= 1 
            return my_map  

        anterior, posicion1 = posicion1, posicion1["next"]
        
        
    return my_map  


def get(my_map, key):
    """Obtiene el valor asociado a una llave en la tabla de simbolos.
Parameters:
        my_map (map_separate_chaining) – Tabla de simbolos de la cual se desea obtener el valor asociado a una llave.
        key (any) – Llave de la cual se desea obtener el valor asociado.
Returns:
    Valor asociado a la llave en la tabla de simbolos.
Return type:
    any

    """

    if lt.is_empty(my_map["table"][mf.hash_value(my_map, key)]):
        return None

    nodo = my_map["table"][mf.hash_value(my_map, key)]["first"]
    while nodo:
        if me.get_key(nodo["info"]) == key:
            return me.get_value(nodo["info"]) 
        nodo = nodo["next"] 

    return None  


def size(my_map):
    """Obtiene la cantidad de elementos en la tabla de simbolos.
Parameters:
    my_map (map_separate_chaining) – Tabla de simbolos de la cual se desea obtener la cantidad de elementos.
Returns:
    Cantidad de elementos en la tabla de simbolos.
Return type:
    int

    """
    return my_map["size"]


def is_empty(my_map):
    """Verifica si la tabla de simbolos se encuentra vacia.
Parameters:
    my_map (map_separate_chaining) – Tabla de simbolos de la cual se desea verificar si se encuentra vacia.
Returns:
    True si la tabla se encuentra vacia, False en caso contrario.
Return type:
    bool

    """
    return size(my_map) == 0


def key_set(my_map):
    """Obtiene la lista de llaves de la tabla de simbolos.
Parameters:
    my_map (map_separate_chaining) – Tabla de simbolos de la cual se desea obtener el conjunto de llaves.
Returns:
    Lista de llaves de la tabla de simbolos.
Return type:
    array_list

    """
    llaves = al.new_list()  
    
    for i in my_map["table"]:  
        if not lt.is_empty(i): 
            nodo = i["first"]  
            while nodo is not None:  
                al.add_last(llaves, me.get_key(nodo["info"]))  
                nodo = nodo["next"] 

    
    return llaves


def value_set(my_map):
    """Obtiene la lista de valores de la tabla de simbolos.
Parameters:
    my_map (map_separate_chaining) – Tabla de simbolos de la cual se desea obtener el conjunto de valores.
Returns:
    Lista de valores de la tabla de simbolos.
Return type:
    array_list

    """
    valores = al.new_list()  

    for i in my_map["table"]:  
        if not lt.is_empty(i): 
            nodo = i["first"]  
            while nodo is not None: 
                al.add_last(valores, me.get_value(nodo["info"]))  
                nodo = nodo["next"]  

    return valores


def rehash(my_map):
    """    Realiza un rehashing de la tabla de simbolos.

    Para realizar un rehash se debe seguir los siguientes pasos:

            . Crear una nueva tabla map_separate_chaining con capacity que sea el siguiente primo al doble del capacity actual.

            . Recorrer la tabla actual y reinsertar cada elemento en la nueva tabla.

            . Asignar la nueva tabla como la tabla actual.

            . Retornar la tabla nueva.
    Parameters:
        my_map (map_separate_chaining) – Tabla de simbolos a la cual se le desea realizar un rehashing.
    Returns:
        Tabla de simbolos con un nuevo tamaño.
    Return type:
        map_separate_chaining

    """
    viojojo = my_map["table"]
    new_capacity = mf.next_prime(2 * my_map["capacity"])
    nuevo = new_map(new_capacity, my_map["limit_factor"])

    for bucket in viojojo:
        current = bucket["first"]
        while current:
            entry = current["info"]
            put(nuevo, entry["key"], entry["value"])  
            current = current["next"]

    my_map["table"] = nuevo["table"]
    my_map["capacity"] = nuevo["capacity"]
    my_map["size"] = nuevo["size"]
    my_map["scale"] = nuevo["scale"]
    my_map["shift"] = nuevo["shift"]
    my_map["prime"] = nuevo["prime"]
    my_map["current_factor"] = nuevo["current_factor"]

    return my_map