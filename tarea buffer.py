buffer = []  # Aquí guardaremos los datos
tamaño_maximo = 3  # Definimos el tamaño del buffer
indice_actual = 0  # Rastrea la próxima posición de escritura

# Lista de datos que queremos guardar
datos = ["Hola", "Mundo", "Python", "Overflow", "Circular", "Buffer"]
print("--- Llenando el Buffer ---")
# Agregamos los datos al buffer
for dato in datos:
    if len(buffer) < tamaño_maximo:
        buffer.append(dato)
        print(f"Guardando: {dato}")
    else:
        # El buffer está lleno, sobrescribimos el dato más antiguo
        buffer[indice_actual] = dato
        print(f"Buffer lleno. Sobrescribiendo el dato en la posición {indice_actual} con: {dato}")
    
    # Actualizamos el índice para la próxima escritura
    indice_actual = (indice_actual + 1) % tamaño_maximo

# Mostramos el contenido final del buffer
print("\n--- Contenido Final del Buffer ---")
print("Contenido del buffer:", buffer)