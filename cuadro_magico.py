# Función que inicializa un tablero vacío de NxN
def crear_cuadrado_magico(n):
    return [[0 for _ in range(n)] for _ in range(n)]


# Función que imprime el cuadrado mágico de manera legible
def imprimir_cuadrado(cuadrado):
    print('       1 2 3')
    print('     +-------+')

    for i, fila in enumerate(cuadrado):
        print(f'  {i + 1}  | ', end='')

        for col in fila:
            print(col, end=' ')

        print(f'| {i + 1}')

    print('     +-------+')
    print('       1 2 3')


# Función que verifica si una posición está vacía en el cuadrado
def posicion_valida(cuadrado, fila, columna):
    if cuadrado[fila][columna] is None:
        return True
    return False


# Función que coloca un número en el cuadrado
def colocar_numero(cuadrado, fila, columna, numero):
    if fila and columna

    cuadrado[fila][columna] = numero
    # --------------------------------------------------
    # --------------------------------------------------


# Función que comprueba si el cuadrado es mágico
def is_magico(cuadrado):
    # --------------------------------------------------
    # Validar si el cuadrado es mágico
    # --------------------------------------------------
    return False

# Función que permite al usuario jugar al cuadrado mágico
def jugar_cuadrado_magico(n):
    cuadrado = crear_cuadrado_magico(n)
    movimientos = 0
    max_movimientos = (
        n * n
    )  # El máximo número de movimientos es igual al número de casillas

    print('\n¡Bienvenido al juego del Cuadrado Mágico!\n')

    while movimientos < max_movimientos:
        imprimir_cuadrado(cuadrado)
        print(f'\nMovimientos restantes: {max_movimientos - movimientos}')

        # Solicitar al usuario la fila, columna y número que desea colocar
        try:
            fila = int(input(f'Ingrese la fila (1 a {n}): ')) - 1
            columna = int(input(f'Ingrese la columna (1 a {n}): ')) - 1
            numero = int(input('Ingrese el número a colocar: '))

            if 0 <= fila < n and 0 <= columna < n:
                if posicion_valida(cuadrado, fila, columna):
                    colocar_numero(cuadrado, fila, columna, numero)
                    movimientos += 1
                else:
                    print('¡La posición ya está ocupada! Inténtelo de nuevo.')
            else:
                print('¡Coordenadas fuera del rango! Inténtelo de nuevo.')
        except ValueError:
            print('Entrada inválida. Por favor, ingrese números válidos.')

        # Preguntar si el cuadrado es mágico después de cada movimiento
        if movimientos >= n:
            if is_magico(cuadrado):
                print('\n¡Felicidades, has completado un Cuadrado Mágico!\n')
                imprimir_cuadrado(cuadrado)
                return

    # Si se completan todos los movimientos y no es mágico
    if not is_magico(cuadrado):
        print('\nEl cuadrado no es mágico. Sigue intentando.\n')
        imprimir_cuadrado(cuadrado)


# Función que realiza una prueba y genera retroalimentación detallada
def resultado_prueba(prueba, resultado, descripcion):
    if resultado:
        print(f'True - {prueba} - {descripcion} superada')
    else:
        print(f'False - {prueba} - {descripcion} no superada')
    return resultado


# Función de prueba para verificar la ocupación de una posición
def prueba_posicion_ocupada():
    print('---- Prueba de Posición Ocupada ----')
    n = 3
    cuadrado = crear_cuadrado_magico(n)
    colocar_numero(cuadrado, 0, 0, 4)

    # Pruebas
    test1 = resultado_prueba(
        'prueba_posicion_ocupada_1',
        not posicion_valida(cuadrado, 0, 0),
        'No deberia ser valida',
    )
    test2 = resultado_prueba(
        'prueba_posicion_ocupada_2',
        posicion_valida(cuadrado, 0, 1),
        'Deberia ser valida',
    )
    colocar_numero(cuadrado, 0, 1, 5)
    test3 = resultado_prueba(
        'prueba_posicion_ocupada_3',
        not posicion_valida(cuadrado, 0, 1),
        'No deberia ser valida',
    )

    # Resultado final
    total_pruebas = test1 + test2 + test3
    print(f'\n{total_pruebas}/3 pruebas posicion ocupada\n')
    return total_pruebas


# Función de prueba para verificar si el cuadrado es mágico
def prueba_cuadrado_magico():
    print('---- Prueba de Cuadrado Mágico ----')
    # Cuadrado mágico de orden 3
    cuadrado_magico = [
        [8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
    ]
    # Cuadrado no mágico
    cuadrado_no_magico = [
        [8, 1, 6],
        [3, 5, 7],
        [4, 0, 2]
    ]

    # Pruebas
    test1 = resultado_prueba('prueba_cuadrado_magico_1', is_magico(cuadrado_magico), 'Es cuadrado mágico')
    test2 = resultado_prueba('prueba_cuadrado_magico_2', not is_magico(cuadrado_no_magico), 'No es cuadrado mágico')

    # Resultado final
    total_pruebas = test1 + test2
    print(f'\n{total_pruebas}/2 pruebas cuadrado magico\n')
    return total_pruebas


# Prueba de llenado completo de cuadrado
def prueba_lleno():
    print('---- Prueba de Cuadrado Lleno ----')
    n = 3
    cuadrado = crear_cuadrado_magico(n)
    colocar_numero(cuadrado, 0, 0, 1)
    colocar_numero(cuadrado, 0, 1, 2)
    colocar_numero(cuadrado, 0, 2, 3)
    colocar_numero(cuadrado, 1, 0, 4)
    colocar_numero(cuadrado, 1, 1, 5)
    colocar_numero(cuadrado, 1, 2, 6)
    colocar_numero(cuadrado, 2, 0, 7)
    colocar_numero(cuadrado, 2, 1, 8)
    colocar_numero(cuadrado, 2, 2, 9)

    # Verificar si está completamente lleno
    llenado_correcto = all(all(fila) for fila in cuadrado)
    resultado_prueba('prueba_lleno', llenado_correcto, 'prueba_lleno')


# Prueba para ver si el cuadrado está vacío inicialmente
def prueba_cuadrado_vacio():
    print('---- Prueba de Cuadrado Vacío ----')
    n = 3
    cuadrado = crear_cuadrado_magico(n)
    cuadrado_vacio = all(all(fila == 0 for fila in fila) for fila in cuadrado)
    resultado_prueba('prueba_cuadrado_vacio', cuadrado_vacio, 'prueba_cuadrado_vacio')


# Función que ejecuta todas las pruebas
def ejecutar_pruebas():
    total_pruebas = 0
    total_pruebas += prueba_posicion_ocupada()
    total_pruebas += prueba_cuadrado_magico()
    prueba_lleno()
    prueba_cuadrado_vacio()

    print(f'\nTotal de pruebas superadas: {total_pruebas}')


# Ejecución del juego y pruebas
if __name__ == '__main__':
    # Ejecutar el juego
    # jugar_cuadrado_magico(3)

    # Ejecutar todas las pruebas
    ejecutar_pruebas()
