from DataStructures.List import array_list as slt

def new_stack():
    """
    Crea una nueva pila vacía.
    Returns: Una nueva pila vacía.
    Return type: stack
    """
    stk = slt.new_list()
    return stk


def push(my_stack, element):
    """
    Añade el elemento element al tope de la pila my_stack.
    Parameters:
        my_stack (stack) – La pila a la que se le añadirá el elemento.
        element (Any) – El elemento que se añadirá a la pila.
    Returns: La pila con el elemento añadido.
    Return type: stack
    """
    stack = slt.add_last(my_stack, element)
    return stack


def pop(my_stack):
    """
    Elimina y retorna el elemento en el tope de la pila my_stack no vacía.
    Si la pila está vacía, se lanza un error: EmptyStructureError: stack is empty.
    Parameters:
        my_stack (stack) – La pila de la que se eliminará el elemento.
    Returns: Elemento retirado de la pila.
    Return type: any
    """
    if is_empty(my_stack):
        return print("EmptyStructureError: stack is empty")
    else:
        return slt.remove_last(my_stack)


def top(my_stack):
    """
    Retorna sin eliminar el elemento en el tope de la pila my_stack.
    Si la pila está vacía, se lanza un error: EmptyStructureError: stack is empty.
    Parameters:
        my_stack (stack) – La pila de la que se retornará el elemento.
    Returns: Elemento en el tope de la pila.
    Return type: any
    """
    if is_empty(my_stack):
        return print("EmptyStructureError: stack is empty")
    return slt.last_element(my_stack)


def is_empty(my_stack):
    """
    Verifica si la pila my_stack está vacía.
    Parameters:
        my_stack (stack) – La pila a verificar.
    Returns: True si la pila está vacía, de lo contrario False.
    Return type: bool
    """
    return slt.is_empty(my_stack)


def size(my_stack):
    """
    Retorna el número de elementos en la pila my_stack.
    Parameters: 
        my_stack (stack) – La pila de la que se retornará el tamaño.
    Returns: Número de elementos en la pila.
    Return type: int
    """
    return slt.size(my_stack)
