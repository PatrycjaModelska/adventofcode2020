input_list = []

with open('input_puzzle_5') as file:
    for line in file:
        input_list.append(line.strip())


# F -  I połowa
# B - II połowa
# L -  I połowa
# R - II połowa

# Part I

def check_ID(input_list):
    max_ID = 0
    list_seat_ID = []
    for el in input_list:
        row = 0
        column = 0
        rows = list(range(0, 128))
        columns = list(range(0, 8))
        for letter in el[:7]:
            if letter == "F":
                rows = rows[:int(len(rows) / 2)]
            else:
                rows = rows[-int(len(rows) / 2):]

        row = rows[0]

        for letter in el[7:]:
            if letter == "L":
                columns = columns[:int(len(columns) / 2)]
            else:
                columns = columns[-int(len(columns) / 2):]

        column = columns[0]

        list_seat_ID.append(row * 8 + column)


        if max_ID < (row * 8 + column):
            max_ID = (row * 8 + column)

    list_seat_ID.sort()
    print(max_ID)
    return list_seat_ID

# correct answer 989


# Part II

def find_your_seat(input_list):
    list = check_ID(input_list)
    for index, value in enumerate(list):
        if index+89 != value:
            return value - 1

print(find_your_seat(input_list))

# correct answer 548