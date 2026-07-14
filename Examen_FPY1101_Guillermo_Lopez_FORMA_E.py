
def menu():
    print('\n========== MENÚ PRINCIPAL ==========')
    print('1. Copias por género')
    print('2. Búsqueda de libros por rango de multa')
    print('3. Actualizar multa de libro')
    print('4. Agregar libro')
    print('5. Eliminar libro')
    print('6. Salir')
    print('=====================================')


def leer_opcion():
    while True:
        try:
            opcion = int(input('Ingrese una opcion: \n'))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print('Ingrese una opcion valida: \n')
        except ValueError:
            print('Ingrese una opcion valida: \n')

def copias_genero(genero, libros, prestamos):
    total_copias = 0
    genero_buscando = genero.strip().lower()

    for codigo in libros:
        genero_libro = libros[codigo][2].strip().lower()
        if genero_libro == genero_buscando:
            if codigo in prestamos:
                copias_disponibles = prestamos[codigo][1]
                total_copias = total_copias+copias_disponibles
    print(f'El total de copias disponibles es de : {total_copias}')

def busqueda_multa(multa_minima, multa_maxima, libros, prestamos):
    libros_encontrados = []
    for codigo in prestamos:
        precio_multa = prestamos[codigo][0]
        copias_disponibles = prestamos[codigo][1]
        if precio_multa >= multa_minima and precio_multa <= multa_maxima:
            if copias_disponibles != 0:
                if codigo in libros:
                    titulo = libros[codigo][0]
                    resultado = titulo +'--'+ codigo
                    libros_encontrados.append(resultado)
    libros_encontrados.sort()
    if len(libros_encontrados) > 0:
        print(f'Libros encontrados: {libros_encontrados}')
    else:
        print('No existen libros con ese rango de multa.')

def buscar_codigo(codigo, prestamos):
    buscar_codigo = codigo.strip().lower()
    for codigo_guardado in prestamos:
        if codigo_guardado.lower() == buscar_codigo:
            return True
    return False

def actualizar_multa(codigo, nueva_multa, prestamos):
    if buscar_codigo(codigo, prestamos):
        buscando_codigo = codigo.strip().lower()
        for codigo_guardado in prestamos:
            if codigo_guardado.lower()==buscando_codigo:
                prestamos[codigo_guardado][0]=nueva_multa
                return True
    return False

def Validar_codigo (codigo, libros, prestamos ):
    if codigo.strip() == '':
        return False
    
    buscando_codigo = codigo.strip().lower()
    for codigo_guardado in libros:
        if codigo_guardado.lower() == buscando_codigo:
            return False
    
    for codigo_guardado in prestamos:
        if codigo_guardado.lower() == buscando_codigo:
            return False
        
    return True

def validar_titulo(titulo):
    if titulo.strip() != '':
        return True
    else:
        return False
    
def validar_autor (autor):
    if autor.strip() != '':
        return True
    else:
        return False
    
def validar_genero(genero):
    if genero.strip() != '':
        return True
    else:
        return False
    
def validar_year (year):
    try:
        year = int(year)
        if year > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def validar_editorial(editorial):
    if editorial.strip() != '':
        return True
    else:
        return False
    
def validar_novedad(es_novedad):
    respuesta = es_novedad.strip().lower()
    if respuesta == 's' or respuesta == 'n':
        return True
    else:
        return False

def validar_precio_multa(precio_multa):
    try:
        precio_multa = int(precio_multa)

        if precio_multa > 0:
            return True
        else:
            return False
    except ValueError:
        return False
    
def Validar_copias_disponibles(copias_disponibles):
    try:
        copias_disponibles = int(copias_disponibles)
        if copias_disponibles >= 0:
            return True
        else:
            return False
    except ValueError:
        return False
    
def agregar_libro(codigo,titulo,autor,genero,year,editorial,es_novedad, precio_multa,copias_disponibles,libros,prestamos):
    Ncodigo = codigo.strip().upper()
    if Ncodigo in libros or Ncodigo in prestamos:
        return False
    libros[Ncodigo] = [
        titulo.strip(),
        autor.strip(),
        genero.strip(),
        year,
        editorial.strip(),
        es_novedad
    ]
    prestamos[Ncodigo] = [
        precio_multa,
        copias_disponibles
    ]
    return True

def eliminar_libro(codigo,libros,prestamos):
    if not buscar_codigo(codigo,prestamos):
        return False
    buscando_codigo = codigo.strip().lower()
    libros_codigo = ''
    prestamos_codigo = ''

    for codigo_guardado in libros:
        if codigo_guardado.lower() == buscando_codigo:
            libros_codigo = codigo_guardado

    for codigo_guardado in prestamos:
        if codigo_guardado.lower() == buscando_codigo:
            prestamos_codigo = codigo_guardado

    if libros_codigo != '':
        del libros[libros_codigo]

    if prestamos_codigo != '':
        del prestamos[prestamos_codigo]
    
    return True

def main():
    libros = {
        'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
        'L002': ['Python en Ruta', 'M. Diaz', 'tecnologia', 2023, 'CodeBooks', True],
        'L003': ['Mar y Viento', 'C. Silva', 'poesia', 2017, 'Litoral', False],
        'L004': ['Historia Breve', 'J. Perez', 'historia', 2015, 'Cronos', False],
        'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficcion', 2021, 'Orion', True],
        'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False]
        }
    
    prestamos = {
        'L001': [500, 4],
        'L002': [700, 0],
        'L003': [300, 10],
        'L004': [400, 2],
        'L005': [600, 1],
        'L006': [350, 6]
        }
    menu_activo = True

    while menu_activo:
        menu()
        opcion = leer_opcion()

        if opcion == 1:
            genero = input('Ingrese genero a consultar: \n')
            copias_genero(genero, libros, prestamos)

        elif opcion == 2:
            datos_validos = False
            while datos_validos == False:
                try:
                    multa_minima = int (input('Ingrese multa minima: \n'))
                    multa_maxima = int (input('Ingrese multa maxima: \n'))
                    if multa_minima < 0 or multa_maxima < 0:
                        print('Las multas deben ser mayores o iguales a cero.')
                    elif multa_minima > multa_maxima:
                        print('Las multa minima no debe ser mayor que la multa maxima.')
                    else:
                        datos_validos = True
                except ValueError:
                    print('Debe ingresar valores enteros.')
            busqueda_multa(multa_minima, multa_maxima, libros, prestamos)

        elif opcion == 3:
            respuesta = 's'

            while respuesta == 's':
                codigo = input('Ingrese codigo del libro: \n')
                multa_valida = False
                while multa_valida == False:
                    try:
                        nueva_multa = int(input('Ingrese nueva multa'))
                        if nueva_multa > 0:
                            multa_valida = True
                        else:
                            print('La ulta debe ser un numero entero, mayor que cero ')
                    except ValueError:
                        print('La multa debe ser un numero entero mayor que cero.')
            resultado = actualizar_multa(codigo,nueva_multa,prestamos)
            if resultado == True:
                print('Multa actualizada')
            else:
                print('Codigo de multa no existe.')
            respuesta_valida = False
            while respuesta_valida == False:
                respuesta = input('Desea actualizar otra multa?: (s/n) ').strip().lower()
                if respuesta == 's' or respuesta == 'n':
                    respuesta = True
                else:
                    print('debe ingresar s o n: ')
                

        elif opcion == 4:
            codigo = input('Ingrese el codigo del libro: ')
            titulo = input('Ingrese el titulo del libro: ')
            autor = input('Ingrese el autor del libro: ')
            genero = input('Ingrese el genero del libro: ')
            year = input('Ingrese el ano del libro: ')
            editorial = input('Ingrese la editorial del libro: ')
            es_novedad = input('Ingrese si es de novedad del libro: ')
            precio_multa = input('Ingrese el precio de la multa del libro: ')
            copias_disponibles = input('Ingrese copias disponible del libro: ')

            datos_validos = True
            if not Validar_codigo(codigo,libros,prestamos):
                if codigo.strip() == '':
                    print('El codigo no puede estar vacio.')
                else:
                    print('el codigo ya existe.')
                datos_validos = False

            if not validar_titulo(titulo):
                print('El titulo no puede estar vacio.')
                datos_validos = False

            if not validar_autor(autor):
                print('El autor no puede estar vacio.')
                datos_validos = False

            if not validar_genero(genero):
                print('El genero no puede estar vacio.')
                datos_validos = False

            if not validar_year(year):
                print('El ano no puede estar vacio.')
                datos_validos = False

            if not validar_editorial(editorial):
                print('La editorial no puede estar vacio.')
                datos_validos = False

            if not validar_novedad(es_novedad):
                print('Novedad no puede estar vacio.')
                datos_validos = False

            if not validar_precio_multa(precio_multa):
                print('El precio de la multa no puede estar vacio.')
                datos_validos = False

            if not Validar_copias_disponibles(copias_disponibles):
                print('Las copias disponibles deben ser numero enteros')
                datos_validos = False

                if datos_validos == True:
                    year = int(year)
                    precio_multa = int(precio_multa)
                    copias_disponibles = int(copias_disponibles)

                    if es_novedad.strip().lower() == 's':
                        es_novedad_booleano = True
                    else:
                        es_novedad_booleano = False
                    resultado = agregar_libro(codigo,titulo,autor,genero,year,editorial,es_novedad_booleano,precio_multa,copias_disponibles)
                    if resultado == True:
                        print('Libro agregado.')
                    else:
                        print('El codigo ya existe.')
                
        elif opcion == 5:
            codigo = input('ingrese codigo del libro')
            resultado = eliminar_libro(codigo,libros,prestamos)
            if resultado == True:
                print ('Libro eliminado correctamente.')
            else:
                print ('LEl codigo no existe.')
        elif opcion == 6:
            menu_activo = False

            print('Programa finalizado')

main()