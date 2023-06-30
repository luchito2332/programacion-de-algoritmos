alumno = []
def guardar_datos_alumno():
    rut = input("Ingresar el Rut del alumno: ")
    nombre = input("Ingresar el nombre del alumno: ")
    apellido = input("Ingresar el apellido del alumno: ")
    fecha = input("Ingrese la fecha del alumno: ")
    carrera = input("ingresar carrera del alumno: ")
    asignaturas = input("ingresar nombre y pomedio del alumno:")

    alumno = {
        "Rut": rut,
        "Nombre": nombre,
        "Apellido": apellido,
        "Fecha": fecha,
        "carrera": carrera,
        "asignaturas": asignaturas
    }
    
    alumno.append(alumno)
    print("alumno guardado correctamente.")

def buscar_alumno():
    rut_buscar = input("Ingrese el Rut del alumno a buscar: ")
    
    for alumno in alumno:
        if alumno["Rut"] == rut_buscar:
            print("Información del alumno: ")
            print(f"Rut: {alumno['Rut']}")
            print(f"Nombre: {alumno['Nombre']}")
            print(f"Apellido: {alumno['Apellido']}")
            print(f"Fecha: {alumno['Fecha']}")
            print(f"carrera: {alumno['carrera']}")
            print(f"asignaturas: {alumno['asignaturas']}")
            return
    
    print("alumno no ubicado.")

def imprimir_certificado():
    rut_certificado = input("Ingrese el Rut del alumno para imprimir el certificado: ")
    
    for alumno in alumno:
        if alumno["Rut"] == rut_certificado:
            print("Certificado de atención:")
            print(f"Fecha: {alumno['Fecha']}")
            print(f"Nombre: {alumno['Nombre']} {alumno['Apellido']}")
            return
    
    print("alumno no ubicado.")

while True:
    print("---- Certificado alumno regular ----")
    print("1. Registrar alumno")
    print("2. Buscar alumno")
    print("3. Imprimir certificado de alumno")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        guardar_datos_alumno()
    elif opcion == "2":
        buscar_alumno()
    elif opcion == "3":
        imprimir_certificado()
    elif opcion == "4":
        print("Gracias por utilizar el programa.¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")