import os

# Función para convertir el mapa de laberinto en una matriz de caracteres
def parse_labyrinth(labyrinth_str):
    labyrinth_lines = labyrinth_str.strip().split('\n')
    labyrinth_matrix = [list(line) for line in labyrinth_lines]
    return labyrinth_matrix

# Función para limpiar la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar la matriz del laberinto en la pantalla
def print_labyrinth(labyrinth_matrix):
    for row in labyrinth_matrix:
        print(''.join(row))

# Función que ejecuta el juego
def main_loop(labyrinth, start, end):
    px, py = start

    while (px, py) != end:
        labyrinth[py][px] = 'P'
        clear_screen()
        print_labyrinth(labyrinth)
        labyrinth[py][px] = '.'

        move = input("Mueve al jugador con las teclas de flecha (↑, ↓, ←, →): ").lower()

        if move == "↑" or move == "w":
            new_px, new_py = px, py - 1
        elif move == "↓" or move == "s":
            new_px, new_py = px, py + 1
        elif move == "←" or move == "a":
            new_px, new_py = px - 1, py
        elif move == "→" or move == "d":
            new_px, new_py = px + 1, py
        else:
            print("Movimiento no válido. Usa las teclas de flecha.")
            continue

        if 0 <= new_px < len(labyrinth[0]) and 0 <= new_py < len(labyrinth):
            if labyrinth[new_py][new_px] != '#':
                px, py = new_px, new_py

    print("¡Has llegado al final del laberinto!")

# Define el laberinto y las posiciones iniciales y finales
laberinto =
"""
..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

mapa = parse_labyrinth(laberinto)
posicion_inicial = (0, 0)
posicion_final = (len(mapa[0]) - 1, len(mapa) - 1)

# Inicia el bucle principal del juego
main_loop(mapa, posicion_inicial, posicion_final)