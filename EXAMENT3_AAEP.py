# Laberinto con valores: 1 = pasable, 3/4 = puntos, 0 = obstáculo
laberinto = [
    [1, 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 3, 1, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    [1, 1, 3, 1, 0, 1, 1, 1, 1],
]

N = len(laberinto)
M = len(laberinto[0])
inicio = (8, 0)
fin = (0, 0)

# Dirección: arriba, derecha, abajo, izquierda
direcciones = [(-1, 0), (0, 1), (1, 0), (0, -1)]

intento = 0
puntos_finales = 0
camino = [[0 for _ in range(M)] for _ in range(N)]
camino_exitoso = []  # Lista de pasos [(x, y)] del camino exitoso

def es_valido(x, y, visitado):
    return 0 <= x < N and 0 <= y < M and laberinto[x][y] != 0 and not visitado[x][y]

def imprimir_camino_actual(caminado, puntos):
    global intento
    intento += 1
    print(f"\n Intento {intento} - Puntos: {puntos}")
    for i in range(N):
        for j in range(M):
            if (i, j) == inicio:
                print(" I ", end="")
            elif (i, j) == fin:
                print(" F ", end="")
            elif caminado[i][j] == 1:
                print(f" {laberinto[i][j]} ", end="")
            else:
                print(" . ", end="")
        print()

def imprimir_pasos(camino_lista):
    print("\n Paso a paso del camino exitoso:")
    paso = 1
    for x, y in camino_lista:
        print(f"\nPaso {paso}: ({x},{y})")
        for i in range(N):
            for j in range(M):
                if (i, j) == (x, y):
                    print(" + ", end="")
                elif (i, j) == inicio:
                    print(" I ", end="")
                elif (i, j) == fin:
                    print(" F ", end="")
                elif (i, j) in camino_lista:
                    print(f" {laberinto[i][j]} ", end="")
                else:
                    print(" . ", end="")
            print()
        paso += 1

def copiar_camino(camino_actual):
    return [fila[:] for fila in camino_actual]

def backtrack(x, y, puntos, visitado, camino_actual, recorrido):
    global puntos_finales, camino, camino_exitoso

    camino_actual[x][y] = 1
    visitado[x][y] = True
    recorrido.append((x, y))

    valor = laberinto[x][y]
    puntos += valor if valor in [3, 4] else 0

    if (x, y) == fin:
        imprimir_camino_actual(camino_actual, puntos)
        if puntos >= 23:
            puntos_finales = puntos
            camino = copiar_camino(camino_actual)
            camino_exitoso = recorrido[:]
            return True

    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if es_valido(nx, ny, visitado):
            if backtrack(nx, ny, puntos, visitado, camino_actual, recorrido):
                return True

    camino_actual[x][y] = 0
    visitado[x][y] = False
    recorrido.pop()
    return False

def imprimir_laberinto_original():
    print("Laberinto original:")
    for fila in laberinto:
        for val in fila:
            print(f"{val:2}", end=" ")
        print()

def imprimir_laberinto_final():
    print("\n Camino final válido encontrado:")
    for i in range(N):
        for j in range(M):
            if (i, j) == inicio:
                print(" I ", end="")
            elif (i, j) == fin:
                print(" F ", end="")
            elif camino[i][j] == 1:
                print(f" {laberinto[i][j]} ", end="")
            else:
                print(" . ", end="")
        print()

def resolver_laberinto():
    visitado = [[False for _ in range(M)] for _ in range(N)]
    camino_actual = [[0 for _ in range(M)] for _ in range(N)]
    recorrido = []

    imprimir_laberinto_original()
    print("\n🔍 Iniciando búsqueda...\n")

    exito = backtrack(inicio[0], inicio[1], 0, visitado, camino_actual, recorrido)

    if exito:
        print(f"\n ¡Camino válido encontrado con {puntos_finales} puntos!")
        print("\n Laberinto original (para referencia):")
        imprimir_laberinto_original()
        imprimir_laberinto_final()
        imprimir_pasos(camino_exitoso)
    else:
        print("\n No se encontró un camino válido con al menos 23 puntos.")

resolver_laberinto()
