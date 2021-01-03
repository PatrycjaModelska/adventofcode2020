import math

timestamp = 1006697
buses = [13,41,641,19,17,29,661,37,23]

# Part I

difference = []

for bus in buses:
    if isinstance(bus, int):
        ceil = math.ceil(timestamp / bus)
        difference.append([(ceil * bus - timestamp), bus])

smallest = min(difference)

print(f'Part I: answer is {smallest[0] * smallest[1]}')

# Part II

input_puzzle = []
with open('input_puzzle_13') as file:
    for line in file:
        input_puzzle.append(line.strip().split(','))

temporary_list = []
buses = input_puzzle[1]

for index, value in enumerate(buses):
    if value != 'x':
        temporary_list.append([int(value), index])


step = temporary_list[0][0]
iter = 0
time = 0
check = False

while check == False:
    if (time + temporary_list[iter + 1][1]) % temporary_list[iter +1][0] == 0:
        step *= temporary_list[iter + 1][0]
        iter += 1
        if iter + 1 == len(temporary_list):
            check = True
    else:
        time += step

print(f'Part II: answer is {time}')


# różnica liczby złożonej z trzech ostatnich cyfr i liczby złożonej z pozostałych cyfr jest podzielna przez 13
