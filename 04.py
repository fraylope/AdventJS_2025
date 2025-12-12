# Los elfos han encontrado el código cifrado que protege la puerta del taller de Santa 🔐. El PIN tiene 4 dígitos,
# y está escondido dentro de bloques como estos:

# [1++][2-][3+][<]
# Escribe una función que descifre el PIN a partir del código.

# El código está formado por bloques entre corchetes [...] y cada bloque genera un dígito del PIN.

# Un bloque normal tiene la forma [nOP...], donde n es un número (0-9) y después puede haber una lista de operaciones (opcionales).

# Las operaciones se aplican en orden al número y son:

# + suma 1
# - resta 1
# El resultado siempre es un dígito (aritmética mod 10), por ejemplo 9 + 1 → 0 y 0 - 1 → 9.

# También existe el bloque especial [<], que repite el dígito del bloque anterior.

# Si al final hay menos de 4 dígitos, se debe devolver null.

def decodeSantaPin(code: str) -> str:
    code_blocks = code.strip().split('][')
    code_blocks[0] = code_blocks[0][1:]  # Remove leading '['
    code_blocks[-1] = code_blocks[-1][:-1]  # Remove trailing ']'
    pin = []
    for block in code_blocks:
        if block == '<':
            if pin:
                pin.append(pin[-1])
        else:
            digit = int(block[0])
            for op in block[1:]:
                if op == '+':
                    digit = (digit + 1) % 10
                elif op == '-':
                    digit = (digit - 1) % 10
            pin.append(digit)
    if len(pin) < 4:
        return None
    return ''.join(str(d) for d in pin[:4])

# Ejemplos:
print(decodeSantaPin('[1++][2-][3+][<]'))
# "3144"

print(decodeSantaPin('[9+][0-][4][<]'))
# "0944"

print(decodeSantaPin('[1+][2-]'))
# null (solo 2 dígitos)