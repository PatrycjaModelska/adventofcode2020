with open("input_puzzle_12", "r") as file:
    input_puzzle = [line.strip() for line in file.readlines()]

# Part I

directions = ['E', 'S', 'W', 'N']
face = 'E'
coordinates = {'E': 0,
               'S': 0,
               'W': 0,
               'N': 0
               }

for el in input_puzzle:
    if el[0] in coordinates:
        coordinates[el[0]] += int(el[1:])
    if el[0] == 'F':
        coordinates[face] += int(el[1:])
    if el[0] == 'R':
        step = int(int(el[1:]) / 90)
        current_index = directions.index(face)
        face = directions[(4 + current_index + step) % 4]
    if el[0] == 'L':
        step = int(int(el[1:]) / 90)
        current_index = directions.index(face)
        face = directions[(4 + current_index - step) % 4]

solution = abs(coordinates['N'] - coordinates['S']) + abs(coordinates['E'] - coordinates['W'])

print(f'Part I: answer is {solution}')

# Part II

# ['E', 'S', 'W', 'N']
ship_coordinates = [0, 0, 0, 0]
waypoint_coordinates = [10, 0, 0, 1]

for el in input_puzzle:
    if el[0] == 'E':
        waypoint_coordinates[0] += int(el[1:])
    if el[0] == 'S':
        waypoint_coordinates[1] += int(el[1:])
    if el[0] == 'W':
        waypoint_coordinates[2] += int(el[1:])
    if el[0] == 'N':
        waypoint_coordinates[3] += int(el[1:])
    if el[0] == 'R':
        step = int(int(el[1:]) / 90)
        temp_coordinates = []
        for it in range(len(waypoint_coordinates)):
            temp_coordinates.append(waypoint_coordinates[(4 + it - step) % 4])
        waypoint_coordinates = temp_coordinates
    if el[0] == 'L':
        step = int(int(el[1:]) / 90)
        temp_coordinates = []
        for it in range(len(waypoint_coordinates)):
            temp_coordinates.append(waypoint_coordinates[(4 + it + step) % 4])
        waypoint_coordinates = temp_coordinates
    if el[0] == 'F':
        for index, value in enumerate(waypoint_coordinates):
            ship_coordinates[index] += int(el[1:]) * value

solution = abs(ship_coordinates[0] - ship_coordinates[2]) + abs(ship_coordinates[1] - ship_coordinates[3])

print(f'Part II: answer is {solution}')
