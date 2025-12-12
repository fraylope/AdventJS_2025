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

def move_reno(board: str, moves: str) -> Literal['fail', 'crash', 'success']:
    board = board.split("\n")
    board = board[1:-1]

    for move in moves:
        match move:
            case 'U':
                for row in board:
                    if '@' in row:
                        col = row.index('@')
                        new_row = board.index(row) - 1
                        if new_row < 0:
                            return 'crash'
                        if board[new_row][col] == '#':
                            return 'crash'
                        elif board[new_row][col] == '*':
                            return 'success'
                        else:
                            board[board.index(row)] = row[:col] + '.' + row[col+1:]
                            board[new_row] = board[new_row][:col] + '@' + board[new_row][col+1:]
                        break
            case 'D':
                for row in board:
                    if '@' in row:
                        col = row.index('@')
                        new_row = board.index(row) + 1
                        if new_row > board.index(board[-1]):
                            return 'crash'
                        if board[new_row][col] == '#':
                            return 'crash'
                        elif board[new_row][col] == '*':
                            return 'success'
                        else:
                            board[board.index(row)] = row[:col] + '.' + row[col+1:]
                            board[new_row] = board[new_row][:col] + '@' + board[new_row][col+1:]
                        break
            case 'R':
                for row in board:
                    if '@' in row:
                        col = row.index('@')
                        new_col = row.index('@') + 1
                        if new_col > row.index(row[-1]):
                            return 'crash'
                        if board[new_row][col] == '#':
                            return 'crash'
                        elif board[new_row][col] == '*':
                            return 'success'
                        else:
                            board[board.index(row)] = row[:col] + '.' + row[col+1:]
                            board[new_row] = board[new_row][:col] + '@' + board[new_row][col+1:]
                        break
            case 'L':
                for row in board:
                    if '@' in row:
                        col = row.index('@')
                        new_col = row.index('@') - 1
                        if new_col < 0:
                            return 'crash'
                        if board[new_row][col] == '#':
                            return 'crash'
                        elif board[new_row][col] == '*':
                            return 'success'
                        else:
                            board[board.index(row)] = row[:col] + '.' + row[col+1:]
                            board[new_row] = board[new_row][:col] + '@' + board[new_row][col+1:]
                        break
    print(board)
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