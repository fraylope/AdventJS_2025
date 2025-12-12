def draw_tree(height, ornament, frequency):
    width = 2 * height - 1
    pos = 1
    levels = []
    for i in range(1, height + 1):
        level_width = 2 * i -1
        chars = []
        for _ in range(level_width):
            if pos % frequency == 0:
                chars.append(ornament)
            else:
                chars.append('*')
            pos += 1
        level = ' ' * ((width - level_width) // 2) + ''.join(chars)
        levels.append(level)

    trunk = ' ' * (width // 2) + '#'
    levels.append(trunk)

    return '\n'.join(levels)

draw_tree(5, 'o', 2)
print(draw_tree(5, 'o', 2))
# //     *
# //    o*o
# //   *o*o*
# //  o*o*o*o
# // *o*o*o*o*
# //     #

draw_tree(3, '@', 3)
print(draw_tree(3, '@', 3))
# //   *
# //  *@*
# // *@**@
# //   #

draw_tree(4, '+', 1)
print(draw_tree(4, '+', 1))
# //    +
# //   +++
# //  +++++
# // +++++++
# //    #