input_list = []

with open('input_puzzle_1') as file:
    for line in file:
        input_list.append(int(line.strip()))

def two_numbers():
    for x in input_list:
        for y in input_list:
            if x + y == 2020:
                return x, y, x * y

print(two_numbers())


def test():
    for x in input_list:
        y = 2020 - x
        if y in input_list:
            return x, y, x * y

print(test())


def tree_numbers():
    for x in input_list:
        for y in input_list:
            for z in input_list:
                if x + y + z == 2020:
                    return (x, y, z, x * y * z)


print(tree_numbers())
