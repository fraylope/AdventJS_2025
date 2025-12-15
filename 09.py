# Los elfos han construido un reno 🦌 robot aspirador (@) para limpiar un poco el taller de cara a las navidades.

# El reno se mueve sobre un tablero para recoger cosas del suelo (*) y debe evitar obstáculos (#).

# Recibirás dos parámetros:

# board: un string que representa el tablero.
# moves: un string con los movimientos: 'L' (izquierda), 'R' (derecha), 'U' (arriba), 'D' (abajo).
# Reglas del movimiento:

# Si el reno recoge algo del suelo (*) durante los movimientos → devuelve 'success'.
# Si el reno se sale del tablero o choca contra un obstáculo (#) → devuelve 'crash'.
# Si el reno no recoge nada ni se estrella → devuelve 'fail'.
# Ten en cuenta que si el reno recoge algo del suelo, ya es 'success', indepentientemente de si en movimientos posteriores se chocase con un obstáculo o saliese del tabler.

# Importante: Ten en cuenta que en el board la primera y última línea están en blanco y deben descartarse.

from typing import List, Literal


def move_reno(board: str, moves: str) -> str:
    rows = [line for line in board.split('\n') if line.strip() != '']
    if not rows:
        return 'fail'

    height = len(rows)
    width = len(rows[0])

    start_row, start_col = -1, -1
    for r in range(height):
        c = rows[r].find('@')
        if c != -1:
            start_row, start_col = r, c
            break

    if start_row == -1:
        # No hay reno en el tablero
        return 'fail'

    delta = {
        'U': (-1, 0),
        'D': ( 1, 0),
        'L': ( 0,-1),
        'R': ( 0, 1)
    }

    r, c = start_row, start_col

    def is_out(rr, cc):
        return rr < 0 or rr >= height or cc < 0 or cc >= width

    for step in moves:
        if step not in delta:
            continue

        dr, dc = delta[step]
        nr, nc = r + dr, c + dc

        if is_out(nr, nc):
            return 'crash'

        cell = rows[nr][nc]

        if cell == '#':
            return 'crash'

        r, c = nr, nc

        if cell == '*':
            return 'success'

    return 'fail'

# Ejemplos:


board = """
.....
.*#.*
.@...
.....
"""

move_reno(board, 'D')
# ➞ 'fail' -> se mueve pero no recoge nada

move_reno(board, 'U')
# ➞ 'success' -> recoge algo (*) justo encima

move_reno(board, 'RU')
# ➞ 'crash' -> choca contra un obstáculo (#)

move_reno(board, 'RRRUU')
# ➞ 'success' -> recoge algo (*)

move_reno(board, 'DD')
# ➞ 'crash' -> se choca con la parte de abajo del tablero

move_reno(board, 'UUU')
# ➞ 'success' -> recoge algo del suelo (*) y luego se choca por arriba

move_reno(board, 'RR')
# ➞ 'fail' -> se mueve pero no recoge nada