class departamento:
    def __init__(self):
        self.departamentos = [[0] * 4 for _ in range(10)]
        self.precios = {
            'Tipo A': 3800,
            'Tipo B': 3000,
            'Tipo C': 2800,
            'Tipo D': 3500
        }

    def mostrar_estado(self):
        print("Estado actual de los departamentos:")
        for i in range(len(self.departamentos)):
            for j in range(len(self.departamentos[i])):
                if self.departamentos[i][j] == 0:
                    print(i * 4 + j + 1, end="\t")  # departamento disponible
                else:
                    print("X", end="\t")  # departamento ocupado
            print()  # Salto de línea

    def comprar_departamento(self):
        self.mostrar_estado()
        departamento = int(input("Ingrese el número del departamento que desea comprar: "))
        fila = (departamento - 1) // 4
        columna = (departamento - 1) % 4

        if self.departamentos[fila][columna] != 0:
            print("El departamento no está disponible.")
            return

        for tipo, rango in self.precios.items():
            if 1 <= departamento <= rango:
                precio = self.precios[tipo]
                break

        run = input("Ingrese el RUN del comprador (sin guion ni dígito verificador): ")
        self.departamentos[fila][columna] = {
            'run': run,
            'precio': precio
        }
        print("Operación realizada correctamente.")

    def mostrar_disponibles(self):
        self.mostrar_estado()

    def mostrar_compradores(self):
        compradores = []
        for i in range(len(self.departamentos)):
            for j in range(len(self.departamentos[i])):
                if self.departamentos[i][j] != 0:
                    compradores.append(self.departamentos[i][j]['run'])
        compradores.sort()
        print("Listado de compradores:")
        for compradores in compradores:
            print(compradores)

    def calcular_ganancias(self):
        total = sum(departamentos['precio'] for fila in self.departamentos for departamentos in fila if departamentos != 0)
        print("Ganancias totales:", total)


# Menú principal
departamento = departamento()

while True:
    print("\n=== MENÚ ===")
    print("1. comprar departamento")
    print("2. departamentos disponibles")
    print("3. Listado de compradores")
    print("4. Ganancias totales")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        departamento.comprar_departamento()
    elif opcion == "2":
        departamento.mostrar_disponibles()
    elif opcion == "3":
        departamento.mostrar_compradores()
    elif opcion == "4":
        departamento.calcular_ganancias()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Intente nuevamente.")

print("Gracias por utilizar el programa.")