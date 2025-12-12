from typing import List, Dict

def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
    # Code here
    left_gloves = {}
    right_gloves = {}
    match = []
    for glove in gloves:
        color = glove['color']
        hand = glove['hand']

        if hand == 'L':
            # Si hay un guante derecho disponible, hacemos el par
            if right_gloves.get(color, 0) > 0:
                match.append(color)
                right_gloves[color] -= 1
            else:
                left_gloves[color] = left_gloves.get(color, 0) + 1
        elif hand == 'R':
            # Si hay un guante izquierdo disponible, hacemos el par
            if left_gloves.get(color, 0) > 0:
                match.append(color)
                left_gloves[color] -= 1
            else:
                right_gloves[color] = right_gloves.get(color, 0) + 1
    return match

gloves = [
  { "hand": 'L', "color": 'red' },
  { "hand": 'R', "color": 'red' },
  { "hand": 'R', "color": 'green' },
  { "hand": 'L', "color": 'blue' },
  { "hand": 'L', "color": 'green' }
]

match_gloves(gloves)
# // ["red", "green"]

gloves2 = [
  { "hand": 'L', "color": 'gold' },
  { "hand": 'R', "color": 'gold' },
  { "hand": 'L', "color": 'gold' },
  { "hand": 'L', "color": 'gold' },
  { "hand": 'R', "color": 'gold' }
]

match_gloves(gloves2)
# // ["gold", "gold"]

gloves3 = [
  { "hand": 'L', "color": 'red' },
  { "hand": 'R', "color": 'green' },
  { "hand": 'L', "color": 'blue' }
]

match_gloves(gloves3)
# // []

gloves4 = [
  { "hand": 'L', "color": 'green' },
  { "hand": 'L', "color": 'red' },
  { "hand": 'R', "color": 'red' },
  { "hand": 'R', "color": 'green' }
]

match_gloves(gloves4)
# // ['red', 'green']