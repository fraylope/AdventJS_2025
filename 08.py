# Santa 🎅 quiere saber cuál es la primera letra no repetida en el nombre de un juguete 🎁.

# Escribe una función que reciba un string y devuelva la primera letra que no se repite, ignorando mayúsculas y minúsculas al contar, pero devolviendo la letra tal como aparece en el string.

# Si no hay ninguna, devuelve una cadena vacía ("").

def find_unique_toy(toy:str) -> str:
    toy_lower = toy.lower()
    for char in toy:
        if toy_lower.count(char.lower()) == 1:
            return char            
    return ''

# Ejemplos:

find_unique_toy('Gift') # 'G'
# ℹ️ La G es la primera letra que no se repite
# y la devolvemos tal y como aparece

find_unique_toy('sS') # ''
# ℹ️ Las letras se repiten, ya que no diferencia mayúsculas

find_unique_toy('reindeeR') # 'i'
# ℹ️ La r se repite (aunque sea en mayúscula)
# y la e también, así que la primera es la 'i'

# Más casos:
find_unique_toy('AaBbCc') # ''
find_unique_toy('abcDEF') # 'a'
find_unique_toy('aAaAaAF') # 'F'
find_unique_toy('sTreSS') # 'T'
find_unique_toy('z') # 'z'