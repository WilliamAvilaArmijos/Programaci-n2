class Buffer:
    def __init__(self, size, circular=False):
        self.size = size
        self.circular = circular
        self.data = []
        self.rejected_entries = []
        self.overwrite_index = 0  # solo para modo circular

    def write(self, value):
        if len(self.data) < self.size:
            self.data.append(value)
        elif self.circular:
            print(f" Sobrescribiendo dato '{self.data[self.overwrite_index]}' con '{value}'")
            self.data[self.overwrite_index] = value
            self.overwrite_index = (self.overwrite_index + 1) % self.size
        else:
            print(f" Dato rechazado: '{value}' (buffer lleno)")
            self.rejected_entries.append(value)

    def display(self):
        print("\n Contenido actual del buffer:")
        print(self.data)
        if self.rejected_entries:
            print("\n Datos rechazados:")
            print(self.rejected_entries)



print(" Modo: Buffer normal (sin sobrescribir)")
buffer1 = Buffer(size=5, circular=False)
for i in range(7):
    buffer1.write(f"Dato{i+1}")
buffer1.display()

print("\n\n Modo: Circular Buffer (sobrescribe)")
buffer2 = Buffer(size=5, circular=True)
for i in range(8):
    buffer2.write(f"Dato{i+1}")
buffer2.display()
