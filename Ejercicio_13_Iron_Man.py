from stack_ import Stack

class TrajeIronMan:
    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado


def mostrar_traje(traje):
    print("Modelo:", traje.modelo)
    print("Película:", traje.pelicula)
    print("Estado:", traje.estado)


def mostrar_pila(stack):
    aux = Stack()
    while not stack.is_empty():
        traje = stack.pop()
        mostrar_traje(traje)
        aux.push(traje)
    while not aux.is_empty():
        stack.push(aux.pop())


def cantidad_trajes_destruidos(pila):
    contador = 0
    aux = Stack()
    while not pila.is_empty():
        traje = pila.pop()
        if traje.estado == "Destruido":
            contador += 1
        aux.push(traje)
    while not aux.is_empty():
        pila.push(aux.pop())
    return contador


def modelos_impecables_avengers(pila):
    modelos = []  # No usamos set()
    aux = Stack()
    while not pila.is_empty():
        traje = pila.pop()
        if "Avengers" in traje.pelicula and traje.estado == "Impecable":
            if traje.modelo not in modelos:
                modelos.append(traje.modelo)
        aux.push(traje)
    while not aux.is_empty():
        pila.push(aux.pop())
    return modelos


def reemplazar_traje(pila, modelo_viejo, modelo_nuevo):
    aux = Stack()
    reemplazado = False
    while not pila.is_empty():
        traje = pila.pop()
        if traje.modelo == modelo_viejo and reemplazado == False:
            traje.modelo = modelo_nuevo
            reemplazado = True
        aux.push(traje)
    while not aux.is_empty():
        pila.push(aux.pop())
    return reemplazado


if __name__ == "__main__":
    pila = Stack()


    pila.push(TrajeIronMan("Mark III", "Iron Man", "Dañado"))
    pila.push(TrajeIronMan("Mark VI", "Avengers", "Impecable"))
    pila.push(TrajeIronMan("Mark XLII", "Iron Man 3", "Destruido"))
    pila.push(TrajeIronMan("Mark L", "Avengers: Infinity War", "Destruido"))
    pila.push(TrajeIronMan("Mark LXXXV", "Avengers: Endgame", "Dañado"))

    print("Todos los trajes:")
    mostrar_pila(pila)

    print("Cantidad de trajes destruidos:")
    print(cantidad_trajes_destruidos(pila))

    print("Modelos impecables en películas de Avengers:")
    modelos = modelos_impecables_avengers(pila)
    for i in range(len(modelos)):
        print(modelos[i])

    print("Reemplazar Mark III por Mark IV:")
    if reemplazar_traje(pila, "Mark III", "Mark IV"):
        print("Reemplazo exitoso.")
    else:
        print("No se encontró el modelo.")

    print("Pila final de trajes:")
    mostrar_pila(pila)

