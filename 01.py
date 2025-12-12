# Santa ha recibido una lista de regalos, pero algunos están defectuosos. Un regalo es defectuoso si su nombre contiene el carácter #.

# Ayuda a Santa escribiendo una función que reciba una lista de nombres de regalos y devuelva una nueva lista que solo contenga
# los regalos sin defectos.

def filterGifts(gifts):
    return [gift for gift in gifts if '#' not in gift]

# Ejemplos
gifts1 = ['car', 'doll#arm', 'ball', '#train']
good1 = filterGifts(gifts1)
print(good1)
# // ['car', 'ball']

gifts2 = ['#broken', '#rusty']
good2 = filterGifts(gifts2)
print(good2)
# // []

gifts3 = []
good3 = filterGifts(gifts3)
print(good3)
# // []
