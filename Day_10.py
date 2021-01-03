with open("input_puzzle_10", "r") as file:
    input_puzzle = sorted([int(line.strip()) for line in file.readlines()])

# Part I

# Really tricky solution <3 from https://dev.to/thetalent/comment/192p8

# r = {1: 0, 2: 0, 3: 0}
# s = 0
# for i in data:
#     r[i - s] += 1
#     s = i
# print(r[1] * (r[3] + 1))

# My solution

chain = input_puzzle
chain.append(0)
chain.append(max(input_puzzle)+3)
chain.sort()

one_jolt = 0
tree_jolt = 0

for index, value in enumerate(chain[:-1]):
    if chain[index + 1] - value == 1:
        one_jolt += 1
    else:
        tree_jolt += 1

print(f'Part I: answer is {one_jolt * tree_jolt}')

# Part II

paths = {}

for el in sorted(input_puzzle):
    if el == sorted(input_puzzle)[0]:  # dla pierwszego el ustawiamy liczbę możliwych ścieżek równą 1
        paths[el] = 1
    else:
        paths[el] = 0  # pozostałe elementy na starcie otrzymają wartość 0

    # dowolny wierzchołek może mieć maksymalnie 3 rodziców
    # dlatego sprawdzamy tylko te trzy wartości: el - 1, el - 2 i el - 3

    if el - 1 in paths:
        paths[el] += paths[el - 1]
    if el - 2 in paths:
        paths[el] += paths[el - 2]
    if el - 3 in paths:
        paths[el] += paths[el - 3]

print(f'Part II: answer is {paths[max(input_puzzle)]}')