# La fábrica de Santa ha empezado a recibir la lista de producción de juguetes.
# Cada línea indica qué juguete hay que fabricar y cuántas unidades.

# Los elfos, como siempre, han metido la pata: han apuntado algunos juguetes con cantidades que no tienen sentido.

# Tienes una lista de objetos con esta forma:

# toy: el nombre del juguete (string)
# quantity: cuántas unidades hay que fabricar (number)
# Tu tarea es escribir una función que reciba esta lista y devuelva un array de strings con:

# Cada juguete repetido tantas veces como indique quantity
# En el mismo orden en el que aparecen en la lista original
# Ignorando los juguetes con cantidades no válidas (menores o iguales a 0, o que no sean número)

def manufactureGifts(giftsToProduce):
    production = []
    for gift in giftsToProduce:
        for i in range(gift["quantity"]):
            production.append(gift["toy"])
    return production
    # return production + [gift["toy"] for gift in giftsToProduce for _ in range(gift["quantity"]) if isinstance(gift["quantity"], int) and gift["quantity"] > 0]

production1 = [
    { "toy": "car", "quantity": 3 },
    { "toy": "doll", "quantity": 1 },
    { "toy": "ball", "quantity": 2 },
]

result1 = manufactureGifts(production1)
print(result1)
# ['car', 'car', 'car', 'doll', 'ball', 'ball']

production2 = [
  { "toy": 'train', "quantity": 0 }, # no se fabrica
  { "toy": 'bear', "quantity": -2 }, # tampoco
  { "toy": 'puzzle', "quantity": 1 }
]

result2 = manufactureGifts(production2)
print(result2)
# ['puzzle']

production3 = []
result3 = manufactureGifts(production3)
print(result3)
# []