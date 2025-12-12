# En el taller de Santa hay un elfo becario que está aprendiendo a envolver regalos 🎁.

# Le han pedido que envuelva cajas usando solo texto… y lo hace más o menos bien.

# Le pasan dos parámetros:

# size: el tamaño del regalo cuadrado
# symbol: el carácter que el elfo usa para hacer el borde (cuando no se equivoca 😅)
# El regalo debe cumplir:

# Debe ser un cuadrado de size x size.
# El interior siempre está vacío (lleno de espacios), porque el elfo "aún no sabe dibujar el relleno".
# Si size < 2, devuelve una cadena vacía: el elfo lo intentó, pero se le perdió el regalo.
# El resultado final debe ser un string con saltos de línea \n.
# Sí, es un reto fácil… pero no queremos que despidan al becario. ¿Verdad?
from time import time
def drawGift(size, symbol):
    start_time = time()
    gift = ''
    if size < 2:
        return gift
    for i in range(size):
        for j in range(size):
            if i == 0 or i == ( size - 1 ) or j == 0 or j == ( size - 1 ):
                gift += symbol
            else:
                gift += " "
        if i < (size - 1):
            gift += "\n"
    end_time = time() - start_time
    print(f"Execution time: {end_time} seconds")
    return gift

g1 = drawGift(4, '*')
print(g1)
"""
/*
 ****
 *  *
 *  *
 ****
 */
"""
g2 = drawGift(3, '#')
print(g2)
"""
/*
###
# #
###
*/
"""
g3 = drawGift(2, '-')
print(g3)
"""
/*
--
--
*/
"""
g4 = drawGift(1, '+')
print(g4)
"""
// ""  pobre becario…
"""
g5 = drawGift(50, '*')
print(g5)