import random

def piedraPapelTijera():
    puntosJugador = 0
    puntosIA = 0
    maxPuntos = 3
    opciones = ['piedra', 'papel', 'tijera']
    while puntosJugador < maxPuntos and puntosIA < maxPuntos:
        opcionJugador = input('Escoge opcion (piedra, papel, tijera): ').lower()
        if opcionJugador not in opciones:
            print('Opcion no valida. Intentalo de nuevo.')
            continue
        opcionIA = opciones[random.randint(0, len(opciones) - 1)]

        print(f'Has escogido: {opcionJugador}')
        print(f'La IA ha escogido: {opcionIA}')

        if opcionJugador == opcionIA:
            print('Empate!')
        elif opcionJugador == 'piedra' and opcionIA == 'tijera':
            print('Has ganado esta ronda!')
            puntosJugador += 1
        elif opcionJugador == 'papel' and opcionIA == 'piedra':
            print('Has ganado esta ronda!')
            puntosJugador += 1
        elif opcionJugador == 'tijera' and opcionIA == 'papel':
            print('Has ganado esta ronda!')
            puntosJugador += 1
        else:
            print('La IA ha ganado esta ronda.')
            puntosIA += 1

        print(f'Marcador: Jugador {puntosJugador} - {puntosIA} IA')
        print('---------------------------------------------------')

    if puntosJugador == maxPuntos:
        print('Felicidades! Has ganado la partida.')
    else:
        print('La IA ha ganado la partida.')

    return True

def ahorcado():
    palabras = [
        "casa", "gato", "perro", "mesa", "luna",
        "sol", "flor", "arbol", "coche", "puerta",
        "libro", "plato", "ventana", "mar", "cielo",
        "pez", "montana", "rio", "nieve", "viento"
    ]

    palabra = palabras[random.randint(0, len(palabras) - 1)]
    palabraSecreta = ['_'] * len(palabra)
    intentos = len(palabra) * 2

    while intentos != 0 and '_' in palabraSecreta:
        print('')
        print(palabraSecreta)
        print(f'Intentos restantes: {intentos}')
        letra = input('Introduce la letra a descubrir: ').lower()

        if len(letra) != 1:
            print('Letra no valida')
            continue

        if letra in palabra:
            print('Has acertado!')
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabraSecreta[i] = letra
        else:
            print('La letra no esta en la palabra')
            intentos -= 1
    print('')

    if '_' not in palabraSecreta:
        print(f'Enhorabuena! Has descubierto la palabra {palabra}')
    else:
        print(f'Te has quedado sin intentos. La palabra era {palabra}')

    return True

def tresEnRaya():
    tablero = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    jugador = 'X'
    ia = 'O'
    turnos = 0
    ganador = None
    turnoActual = jugador
    lineas = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]

    print("\nBienvenido al Tres en Raya!")
    print("Introduce un numero del 1 al 9 para colocar tu ficha.")

    while turnos < 9 and ganador is None:
        if turnoActual == jugador:
            # Mostrar tablero
            print("\n")
            print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
            print("-----------")
            print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
            print("-----------")
            print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")
            print("\n")

            try:
                posicion = int(input('Escoge una posicion (1-9): ')) - 1
            except ValueError:
                print('Valor invalido. Introduce un numero entero.')
                continue

            if posicion < 0 or posicion > 8:
                print('Posicion fuera de rango. Debe ser entre 1 y 9.')
                continue

            if tablero[posicion] == 'X' or tablero[posicion] == 'O':
                print('Esa casilla ya esta ocupada. Prueba otra.')
                continue

            tablero[posicion] = jugador
        else:
            print('Turno de la IA')
            casillas_libres = []
            for i in range(9):
                if tablero[i] != 'X' and tablero[i] != 'O':
                    casillas_libres.append(i)
            tablero[random.choice(casillas_libres)] = ia

        turnos += 1

        # Comprobar ganador
        for l in lineas:
            if tablero[l[0]] == turnoActual and tablero[l[1]] == turnoActual and tablero[l[2]] == turnoActual:
                ganador = turnoActual
                break

        turnoActual = ia if turnoActual == jugador else jugador

    # Tablero final
    print("\n")
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("-----------")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("-----------")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")
    print("\n")

    if ganador == jugador:
        print('Felicidades! Has ganado la partida.')
    elif ganador == ia:
        print('La IA ha ganado la partida.')
    else:
        print('Empate! El tablero se ha llenado.')

    return True

def blackjack():
    cartas_disponibles = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(cartas_disponibles)

    mano_jugador = []
    mano_ia = []

    for i in range(2):
        mano_jugador.append(cartas_disponibles.pop())
        mano_ia.append(cartas_disponibles.pop())

    print("\n--- BIENVENIDO AL BLACKJACK ---")

    while True:
        # Calcular puntuacion del jugador (los ases valen 11 o 1)
        puntuacion_jugador = sum(mano_jugador)
        ases = mano_jugador.count(11)
        while puntuacion_jugador > 21 and ases > 0:
            puntuacion_jugador -= 10
            ases -= 1

        print(f"\nTus cartas: {mano_jugador} (Suma: {puntuacion_jugador})")
        print(f"Carta visible de la IA: {mano_ia[0]}")

        if puntuacion_jugador == 21:
            print("Blackjack! Tienes 21.")
            break
        elif puntuacion_jugador > 21:
            print("Te has pasado de 21. Has perdido!")
            break

        accion = input("Quieres otra carta? (pedir / plantarse): ").lower()

        if accion == 'pedir':
            mano_jugador.append(cartas_disponibles.pop())
        elif accion == 'plantarse':
            break
        else:
            print("Accion no valida. Escribe 'pedir' o 'plantarse'.")

    if puntuacion_jugador <= 21:
        # La IA pide carta hasta llegar a 17 o mas
        while True:
            puntuacion_ia = sum(mano_ia)
            ases = mano_ia.count(11)
            while puntuacion_ia > 21 and ases > 0:
                puntuacion_ia -= 10
                ases -= 1
            if puntuacion_ia >= 17:
                break
            mano_ia.append(cartas_disponibles.pop())

        print("\n--- RESULTADO FINAL ---")
        print(f"Tus cartas finales: {mano_jugador} (Suma: {puntuacion_jugador})")
        print(f"Cartas de la IA: {mano_ia} (Suma: {puntuacion_ia})")

        if puntuacion_ia > 21:
            print("La IA se ha pasado de 21. Has ganado!")
        elif puntuacion_ia > puntuacion_jugador:
            print("La IA tiene mas puntuacion. Has perdido.")
        elif puntuacion_ia < puntuacion_jugador:
            print("Felicidades! Tienes mas puntuacion que la IA. Has ganado.")
        else:
            print("Empate!")

    return True

try:
    while True:
        print('\n1 - Piedra, papel o tijera')
        print('2 - Ahorcado')
        print('3 - Tres en raya')
        print('4 - Blackjack')
        print('5 - Salir')

        try:
            opcion = int(input('> '))
        except ValueError:
            print('Error: Debes introducir un numero entero.')
            continue

        match opcion:
            case 1:
                print('Has escogido Piedra, papel o tijera')
                piedraPapelTijera()
            case 2:
                print('Has escogido Ahorcado')
                ahorcado()
            case 3:
                print('Has escogido Tres en raya')
                tresEnRaya()
            case 4:
                print('Has escogido Blackjack')
                blackjack()
            case 5:
                print('Saliendo...')
                break
            case _:
                print('Opcion no valida en el menu.')

except KeyboardInterrupt:
    print('\nPrograma interrumpido por el usuario.')