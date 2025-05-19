class TrajeIronMan:
    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado  
    
    def __str__(self):
        return f"Modelo: {self.modelo}, Película: {self.pelicula}, Estado: {self.estado}"

class PilaTrajes:
    def __init__(self):
        self.trajes = []
    
    def apilar(self, traje):
        self.trajes.append(traje)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.trajes.pop()
        return None
    
    def esta_vacia(self):
        return len(self.trajes) == 0
    
    def tamanio(self):
        return len(self.trajes)
    
    def cima(self):
        if not self.esta_vacia():
            return self.trajes[-1]
        return None
    
    def mostrar_trajes(self):
        for traje in reversed(self.trajes):
            print(traje)


def cantidad_trajes_destruidos(pila):
    contador = 0
    pila_aux = PilaTrajes()
    
    while not pila.esta_vacia():
        traje = pila.desapilar()
        pila_aux.apilar(traje)
        if traje.estado == "Destruido":
            contador += 1
    
    
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    
    return contador

def modelos_impecables_avengers(pila):
    modelos = set()
    pila_aux = PilaTrajes()
    
    while not pila.esta_vacia():
        traje = pila.desapilar()
        pila_aux.apilar(traje)
        if "Avengers" in traje.pelicula and traje.estado == "Impecable":
            modelos.add(traje.modelo)
    
   
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    
    return modelos

def reemplazar_traje(pila, modelo_viejo, modelo_nuevo):
    pila_aux = PilaTrajes()
    encontrado = False
    
    while not pila.esta_vacia():
        traje = pila.desapilar()
        if traje.modelo == modelo_viejo and not encontrado:
            traje.modelo = modelo_nuevo
            encontrado = True
        pila_aux.apilar(traje)
    
    # Restaurar la pila original
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    
    return encontrado


if __name__ == "__main__":
    pila_trajes = PilaTrajes()
    
    
    pila_trajes.apilar(TrajeIronMan("Mark III", "Iron Man", "Dañado"))
    pila_trajes.apilar(TrajeIronMan("Mark VI", "Avengers", "Impecable"))
    pila_trajes.apilar(TrajeIronMan("Mark XLII", "Iron Man 3", "Destruido"))
    pila_trajes.apilar(TrajeIronMan("Mark L", "Avengers: Infinity War", "Destruido"))
    pila_trajes.apilar(TrajeIronMan("Mark LXXXV", "Avengers: Endgame", "Dañado"))
    
    print("Todos los trajes:")
    pila_trajes.mostrar_trajes()
    
    print("\nCantidad de trajes destruidos:", cantidad_trajes_destruidos(pila_trajes))
    
    print("\nModelos impecables en películas de Avengers:")
    print(modelos_impecables_avengers(pila_trajes))
    
    print("\nReemplazar Mark III por Mark IV:")
    if reemplazar_traje(pila_trajes, "Mark III", "Mark IV"):
        print("Traje reemplazado con éxito")
    else:
        print("Traje no encontrado")
    
    print("\nPila después de las operaciones:")
    pila_trajes.mostrar_trajes()