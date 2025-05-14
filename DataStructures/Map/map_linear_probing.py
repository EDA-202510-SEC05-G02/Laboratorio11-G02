from DataStructures.List import array_list as al
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
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
    . table: Lista de tamaño capacity con las entradas de la tabla de tipo 
    array_list. Inicializado con una lista donde cada elemento es una map_entry 
    con llave y valor None.
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

    map_linear_probing

    
    """
    capacity = mf.next_prime(int(num_elements / load_factor))
    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)
    table = [me.new_map_entry(None, None) for _ in range(capacity)]
    
    map_linear = {
        "prime": prime,             
        "capacity": capacity,      
        "scale": scale,             
        "shift": shift,             
        "table": table,            
        "current_factor": 0,        
        "limit_factor": load_factor,  
        "size": 0                   
    }
    
    return map_linear


def put(my_map, key, value):
    """Agrega una nueva entrada llave-valor a la tabla de hash. Si la llave 
ya existe en la tabla, se actualiza el value de la entrada.

Para agregar un nuevo elemento a la tabla, se realiza el siguiente procedimiento:

    . Se calcula el hash de la llave, usando la función hash_value.

    . Se busca la posición en la tabla con la función find_slot. Si la posición está ocupada, se busca la siguiente posición disponible.

    . Se inserta la entrada en la tabla.

    . Se actualiza el current_factor de la tabla si se agrega un nuevo elemento.

    . Si el current_factor supera el limit_factor, se realiza un rehash de la tabla.

    . Se retorna la tabla con el nuevo elemento agregado.

Parameters:
        my_map (map_linear_probing) – Tabla de simbolos a la cual se desea agregar el elemento.
        key (any) – Llave del elemento a agregar.
        value (any) – Valor del elemento a agregar.
Returns:
    Tabla de simbolos con el nuevo elemento agregado.
Return type:
    map_linear_probing


    """
    hash_llave = mf.hash_value(my_map, key)
    ocupied, posicion = find_slot(my_map, key, hash_llave)
    
    if not ocupied:  
        my_map["table"][posicion] = me.new_map_entry(key, value)
        my_map["size"] += 1  
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]  
    else:  
        my_map["table"][posicion]["value"] = value  
    if my_map["current_factor"] > my_map["limit_factor"]:
        rehash(my_map)

    return my_map


def find_slot(my_map, key, hash_value):
    """Busca la posición en la tabla donde se debe insertar/encontrar una 
    entrada con una llave dada. Utiliza la función de hash_value para calcular 
    la posición inicial y busca la siguiente posición disponible  si la posición 
    inicial está ocupada. Utiliza las funciónes de validación is_available y 
    comparación default_compare.
Parameters:
        my_map (map_linear_probing) – Tabla de simbolos en la que se desea buscar la posición.
        key (any) – Llave de la entrada que se desea buscar.
        hash_value (int) – Valor del hash de la llave.
Returns:
    Retorna una tupla con dos valores. El primero indica si la posición está ocupada, True si se encuentra
    la key de lo contrario False. El segundo la posición en la tabla de hash donde se encuentra o posición 
    libre para agregarla
Return type:

    bool, int

    """
    

    first_avail = None
    found = False
    ocupied = False

    while not found:
        if is_available(my_map["table"], hash_value):
            if first_avail is None:
                first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
                found = True
        elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True

        hash_value = (hash_value + 1) % my_map["capacity"]

    return ocupied, first_avail


def is_available(table, pos):
    """Verifica si la posición pos en la tabla de simbolos está disponible.
Se entiende que una posición está disponible si su contenido es igual a None 
(no se ha usado esa posición) o a __EMPTY__ (la posición fue liberada).
Parameters:
        table (array_list) – Tabla de simbolos en la que se desea verificar la disponibilidad de la posición.
        pos (int) – Posición en la tabla de simbolos que se desea verificar.
Returns:
    True si la posición está disponible, False en caso contrario
Return type:
    bool

    """
    entry = al.get_element(table, pos)
    if entry is None or me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
        return True
    return False
 
 
def default_compare(key, entry):
    """Funcion de comparacion por defecto. Compara la llave key con la llave de una entry dada.
Parameters:
        key (any) – Llave con la que se desea comparar.
        entry (map_entry) – Entrada de la tabla de simbolos con la que se desea comparar.
Returns:
    0 si son iguales, 1 si key > la llave del entry, -1 si key < que la llave del entry
Return type:
    int
    
    """
    if key == me.get_key(entry):    
        return 0
    elif key > me.get_key(entry):
        return 1
    return -1


def contains(my_map, key):
    """Valida si una llave dada se encuentra en la tabla de simbolos.

Parameters:
        my_map (map_linear_probing) – Tabla de simbolos en la que se desea buscar la llave.
        key (any) – Llave que se desea buscar en la tabla.
Returns:
    True si la llave se encuentra en la tabla, False en caso contrario.
Return type:
    bool
    
    """
    hash_key = mf.hash_value(my_map, key)  
    ocupied, _ = find_slot(my_map, key, hash_key) 

    if ocupied:  
        return True
    return False 


def remove(my_map, key):
    
    """Elimina una entrada de la tabla de simbolos asociada a una llave dada.
Parameters:
        my_map (map_linear_probing) – Tabla de simbolos de la cual se desea eliminar la entrada.
        key (any) – Llave de la entrada que se desea eliminar.
Returns:
    Tabla de simbolos sin la entrada asociada a la llave dada.
Return type:

    map_linear_probing
    """
    hash_key = mf.hash_value(my_map, key)  
    ocupied, posicion = find_slot(my_map, key, hash_key) 

    if ocupied:  
        entry = al.get_element(my_map["table"], posicion)
        me.set_key(entry, "__EMPTY__") 
        me.set_value(entry, None) 
        my_map["size"] -= 1  
        my_map["current_factor"] = my_map["size"] / my_map["capacity"] 
    return my_map


def get(my_map, key):
    """Obtiene el valor asociado a una llave dada en la tabla de simbolos.
Parameters:
        my_map (map_linear_probing) – Tabla de simbolos en la que se desea buscar el valor.
        key (any) – Llave de la cual se desea obtener el valor.
Returns:
    Valor asociado a la llave dada. Si la llave no se encuentra en la tabla, se retorna None.
Return type:
    any

    """
    hash_key = mf.hash_value(my_map, key)  
    ocupied, posicion = find_slot(my_map, key, hash_key)  

    if ocupied:  
        return me.get_value(al.get_element(my_map["table"], posicion)) 
    return None 
    
    
def size(my_map):
    """Obtiene la cantidad de elementos en la tabla de simbolos.
Parameters:
    my_map (map_linear_probing) – Tabla de simbolos de la cual se desea obtener la cantidad de elementos.
Returns:
    Cantidad de elementos en la tabla de simbolos.
Return type:
    int

    """
    return my_map["size"]


def is_empty(my_map):
    """Valida si la tabla de simbolos está vacía.
Parameters:
    my_map (map_linear_probing) – Tabla de simbolos de la cual se desea verificar si está vacía.
Returns:
    True si la tabla está vacía, False en caso contrario.
Return type:
    bool

    """
    return size(my_map) == 0 


def key_set(my_map):
    """Obtiene la lista de llaves de la tabla de simbolos.
Parameters:
    my_map (map_linear_probing) – Tabla de simbolos de la cual se desea obtener el conjunto de llaves.
Returns:
    Lista de llaves de la tabla de simbolos.
Return type:
    array_list

    """
    llaves = al.new_list()  
    
    for i in my_map["table"]:
        if i["key"] is not None and i["key"] != "__EMPTY__":  
            al.add_last(llaves, i["key"]) 
    return llaves 

 
def value_set(my_map):
    """Obtiene la lista de valores de la tabla de simbolos.
Parameters:
    my_map (map_linear_probing) – Tabla de simbolos de la cual se desea obtener el conjunto de valores.
Returns:
    Lista de valores de la tabla de simbolos.
Return type:
    array_list

    """
    valores = al.new_list()  

    for i in my_map["table"]:
        if i["key"] is not None and i["key"] != "__EMPTY__":  
            al.add_last(valores, i["value"])  

    return valores


def rehash(my_map):
    """Realiza un rehash de la tabla de simbolos.

Para realizar un rehash se debe seguir los siguientes pasos:
    . Crear una nueva tabla map_linear_probing con capacity que sea el siguiente primo al doble del capacity actual.
    . Insertar los elementos de la tabla actual en la nueva tabla uno por uno.
    . Asignar la nueva tabla a la tabla actual.
    . Retornar la tabla nueva.
Parameters:
    my_map (map_linear_probing) – Tabla de simbolos de la cual se desea realizar el rehash.
Returns:
    Tabla de simbolos con el rehash realizado.
Return type:
    map_linear_probing

    """
    viojo = my_map["table"]  
    new_capacity = mf.next_prime(2 * my_map["capacity"])  
    nuevo = new_map(new_capacity, my_map["limit_factor"])
    
    for entry in viojo:
        if isinstance(entry, dict) and entry["key"] is not None and entry["key"] != "__EMPTY__":
            put(nuevo, entry["key"], entry["value"])  
            
    my_map["table"] = nuevo["table"]
    my_map["capacity"] = nuevo["capacity"]
    my_map["scale"] = nuevo["scale"]
    my_map["shift"] = nuevo["shift"]
    my_map["prime"] = nuevo["prime"]
    my_map["current_factor"] = nuevo["current_factor"]
    my_map["size"] = nuevo["size"]

    return my_map