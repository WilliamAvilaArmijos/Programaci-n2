# Simulación de un "buffer" que solo puede almacenar un número limitado de datos
buffer = []  # Aquí guardaremos los datos
tamaño_maximo = 3  # Definimos el tamaño del buffer

# Lista de datos que queremos guardar
datos = ["Hola", "Mundo", "Python", "Overflow"]

# Agregamos los datos al buffer
for dato in datos:
    if len(buffer) < tamaño_maximo:
        buffer.append(dato)
        print(f"Guardando: {dato}")
    else:
        print(f"¡El buffer está lleno! No se puede guardar '{dato}'.")

# Mostramos el contenido final del buffer
print("\nContenido del buffer:", buffer)