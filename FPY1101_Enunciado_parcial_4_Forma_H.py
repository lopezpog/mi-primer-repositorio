autos = []

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Debe ingresar una opcion entre 1 y 6.")
        except ValueError:
            print("Debe ingresar un numero valido.")

def validar_modelo(modelo):
    if modelo.strip() != "":
        return True
    else:
        return False

def validar_anio(anio):
    try:
        anio = int(anio)
        if anio > 1900:
            return True
        else:
            return False
    except ValueError:
        return False

def validar_precio(precio):
    try:
        precio = float(precio)
        if precio > 0:
            return True
        else:
            return False
    except ValueError:
        return False
    
def agregar_auto(lista):
    modelo = input("Ingrese el modelo del auto: ")
    anio = input("Ingrese el año del auto: ")
    precio = input("Ingrese el precio del auto: ")

    if not validar_modelo(modelo):
        print("El modelo no puede estar vacio.")
        return
    if not validar_anio(anio):
        print("El año debe ser un numero entero mayor que 1900.")
        return
    if not validar_precio(precio):
        print("El precio debe ser un numero mayor que cero.")
        return
    auto = {
        "modelo" : modelo.strip(),
        "anio" : int(anio),
        "precio" : float(precio),
        "disponible" : False
    }
    lista.append(auto)
    print("Vehiculo agregado correctamente.")

def buscar_auto(lista, modelo):
    for i in range (len(lista)):
        if lista[i]["modelo"] == modelo:
            return i
    return -1

def eliminar_auto(lista):
    modelo = input("ingrese el modelo del vehiculo a eliminar: ")
    posicion = buscar_auto(lista, modelo)
    if posicion != -1:
        lista.pop(posicion)
        print("Vehiculo eliminado correctamente.")
    else:
        print(f"El vehiculo {modelo} no se encuentra registrado.")

def actualizar_disponibilidad(lista):
    for auto in lista:
        if auto["anio"] >= 2020:
            auto["disponible"] = True
        else:
            auto["disponible"] = False
    print("Disponibilidad actualizada correctamente.")

def mostrar_auto(lista):
    actualizar_disponibilidad(lista)

    if len(lista) == 0:
        print("no hay vehiculos registrados.")
        return
    print ("== LISTA DE VEHICULOS ==")

    for auto in lista:
        print("Modelo:", auto["modelo"])
        print("Año:", auto["anio"])
        print("Precio:", auto["precio"])

        if auto["disponible"]:
            print ("Estado: DISPONIBLE")
        else:
            print ("Estado: NO DISPONIBLE")

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_auto(autos)
    elif opcion == 2:
        modelo = input("Ingrese el modelo a buscar: ")
        posicion = buscar_auto(autos, modelo)

        if posicion != -1:
            print("Auto encontrado en la posicion: ", posicion)
            print("Modelo:", autos[posicion]["modelo"])
            print("Año:", autos[posicion]["anio"])
            print("Precio:", autos[posicion]["precio"])
            print("Disponible:", autos[posicion]["disponible"])
        else:
            print("Auto no encontrado.")
    elif opcion == 3:
        eliminar_auto(autos)
    elif opcion == 4:
        actualizar_disponibilidad(autos)
    elif opcion == 5:
        mostrar_auto(autos)
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break