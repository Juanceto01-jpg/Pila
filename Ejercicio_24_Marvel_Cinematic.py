from stack_ import Stack

class Personaje:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas


def mostrar_personaje(p):
    print(p.nombre, "-", p.peliculas, "películas")


def crear_pila_mcu():
    pila = Stack()
    personajes = [
        ("Rocket Raccoon", 6), ("Groot", 5), ("Iron Man", 10), ("Captain America", 9),
        ("Black Widow", 8), ("Thor", 8), ("Hulk", 6), ("Doctor Strange", 5),
        ("Spider-Man", 5), ("Black Panther", 4), ("Star-Lord", 5), ("Gamora", 4),
        ("Drax", 4), ("Captain Marvel", 3), ("Scarlet Witch", 5), ("Vision", 4),
        ("Falcon", 5), ("Winter Soldier", 5), ("War Machine", 7), ("Loki", 6),
        ("Nick Fury", 9), ("Hawkeye", 5), ("Ant-Man", 4), ("Wasp", 3),
        ("Doctor Strange", 5), ("Star-Lord", 5), ("Gamora", 4), ("Drax", 4),
        ("Mantis", 3), ("Nebula", 4), ("Shang-Chi", 1), ("Eternals", 1), ("Wong", 5),
        ("Happy Hogan", 4), ("Pepper Potts", 4), ("Red Skull", 2), ("Thanos", 4),
        ("Ultron", 2), ("Hela", 1), ("Yondu", 2)
    ]
    for i in range(len(personajes)):
        nombre, cantidad = personajes[i]
        pila.push(Personaje(nombre, cantidad))
    return pila


def posicion_rocket_groot(pila):
    aux = Stack()
    pos_rocket = -1
    pos_groot = -1
    posicion = 1
    while not pila.is_empty():
        p = pila.pop()
        aux.push(p)
        if p.nombre == "Rocket Raccoon":
            pos_rocket = posicion
        if p.nombre == "Groot":
            pos_groot = posicion
        posicion += 1
    while not aux.is_empty():
        pila.push(aux.pop())
    return (pos_rocket, pos_groot)


def personajes_mas_de_5(pila):
    aux = Stack()
    resultados = []
    while not pila.is_empty():
        p = pila.pop()
        if p.peliculas > 5:
            resultados.append(p)
        aux.push(p)
    while not aux.is_empty():
        pila.push(aux.pop())
    return resultados


def peliculas_viuda_negra(pila):
    aux = Stack()
    resultado = 0
    encontrado = False
    while not pila.is_empty():
        p = pila.pop()
        if not encontrado and p.nombre == "Black Widow":
            resultado = p.peliculas
            encontrado = True
        aux.push(p)
    while not aux.is_empty():
        pila.push(aux.pop())
    return resultado


def personajes_letras_cdg(pila):
    aux = Stack()
    resultados = []
    while not pila.is_empty():
        p = pila.pop()
        letra = p.nombre[0].upper()
        if letra == "C" or letra == "D" or letra == "G":
            resultados.append(p)
        aux.push(p)
    while not aux.is_empty():
        pila.push(aux.pop())
    return resultados


if __name__ == "__main__":
    pila_mcu = crear_pila_mcu()

    print("a. Posiciones de Rocket Raccoon y Groot:")
    pos_r, pos_g = posicion_rocket_groot(pila_mcu)
    print("Rocket Raccoon está en la posición:", pos_r)
    print("Groot está en la posición:", pos_g)

    print("b. Personajes con más de 5 películas:")
    mas_de_5 = personajes_mas_de_5(pila_mcu)
    for i in range(len(mas_de_5)):
        mostrar_personaje(mas_de_5[i])

    print("c. Películas en las que participó Black Widow:")
    cantidad = peliculas_viuda_negra(pila_mcu)
    print("Black Widow participó en", cantidad, "películas")

    print("d. Personajes cuyos nombres empiezan con C, D o G:")
    seleccionados = personajes_letras_cdg(pila_mcu)
    for i in range(len(seleccionados)):
        mostrar_personaje(seleccionados[i])
