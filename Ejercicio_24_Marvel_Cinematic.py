class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def tamano(self):
        return len(self.items)
    
    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None
    
    def __str__(self):
        return str(self.items)

class Personaje:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas
    
    def __str__(self):
        return f"{self.nombre} ({self.peliculas} películas)"

def crear_pila_mcu():
    pila = Pila()
    personajes = [
        ("Rocket Raccoon", 6),
        ("Groot", 5),
        ("Iron Man", 10),
        ("Captain America", 9),
        ("Black Widow", 8),
        ("Thor", 8),
        ("Hulk", 6),
        ("Doctor Strange", 5),
        ("Spider-Man", 5),
        ("Black Panther", 4),
        ("Star-Lord", 5),
        ("Gamora", 4),
        ("Drax", 4),
        ("Captain Marvel", 3),
        ("Scarlet Witch", 5),
        ("Vision", 4),
        ("Falcon", 5),
        ("Winter Soldier", 5),
        ("War Machine", 7),
        ("Loki", 6),
        ("Nick Fury", 9),
        ("Hawkeye", 5),
        ("Ant-Man", 4),
        ("Wasp", 3),
        ("Doctor Strange", 5),
        ("Star-Lord", 5),
        ("Gamora", 4),
        ("Drax", 4),
        ("Mantis", 3),
        ("Nebula", 4),
        ("Shang-Chi", 1),
        ("Eternals", 1),
        ("Wong", 5),
        ("Happy Hogan", 4),
        ("Pepper Potts", 4),
        ("Red Skull", 2),
        ("Thanos", 4),
        ("Ultron", 2),
        ("Hela", 1),
        ("Yondu", 2)
    ]
    
    for nombre, peliculas in personajes:
        pila.apilar(Personaje(nombre, peliculas))
    
    return pila

def posicion_rocket_groot(pila):
    pos_rocket = -1
    pos_groot = -1
    posicion = 1  
    
    pila_temp = Pila()
    
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        pila_temp.apilar(personaje)
        
        if personaje.nombre == "Rocket Raccoon":
            pos_rocket = posicion
        if personaje.nombre == "Groot":
            pos_groot = posicion
        
        posicion += 1
    
    
    while not pila_temp.esta_vacia():
        pila.apilar(pila_temp.desapilar())
    
    return (pos_rocket, pos_groot)

def personajes_mas_de_5_peliculas(pila):
    resultados = []
    pila_temp = Pila()
    
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        pila_temp.apilar(personaje)
        
        if personaje.peliculas > 5:
            resultados.append((personaje.nombre, personaje.peliculas))
    
    
    while not pila_temp.esta_vacia():
        pila.apilar(pila_temp.desapilar())
    
    return resultados

def peliculas_viuda_negra(pila):
    peliculas = 0
    pila_temp = Pila()
    
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        pila_temp.apilar(personaje)
        
        if personaje.nombre == "Black Widow":
            peliculas = personaje.peliculas
            break
    
    
    while not pila_temp.esta_vacia():
        pila.apilar(pila_temp.desapilar())
    
    return peliculas

def personajes_letras_cdg(pila):
    resultados = []
    pila_temp = Pila()
    
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        pila_temp.apilar(personaje)
        
        primera_letra = personaje.nombre[0].upper()
        if primera_letra in ['C', 'D', 'G']:
            resultados.append(personaje)
    
    
    while not pila_temp.esta_vacia():
        pila.apilar(pila_temp.desapilar())
    
    return resultados


if __name__ == "__main__":
    pila_mcu = crear_pila_mcu()
    
  
    pos_rocket, pos_groot = posicion_rocket_groot(pila_mcu)
    print("\na. Posiciones de Rocket Raccoon y Groot:")
    print(f"Rocket Raccoon está en la posición: {pos_rocket}")
    print(f"Groot está en la posición: {pos_groot}")
    
   
    mas_de_5 = personajes_mas_de_5_peliculas(pila_mcu)
    print("\nb. Personajes que participaron en más de 5 películas:")
    for nombre, peliculas in mas_de_5:
        print(f"{nombre}: {peliculas} películas")
    
    
    peliculas_bw = peliculas_viuda_negra(pila_mcu)
    print("\nc. Películas en las que participó Black Widow:")
    print(f"Black Widow participó en {peliculas_bw} películas")
    
    
    personajes_cdg = personajes_letras_cdg(pila_mcu)
    print("\nd. Personajes cuyos nombres empiezan con C, D y G:")
    for personaje in personajes_cdg:
        print(personaje)