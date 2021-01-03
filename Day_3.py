input_list = []

with open('input_puzzle_3') as file:
    for line in file:
        line = line.strip()
        input_list.append(line*73)

def journey(list,right,down):
    go_right = 1
    go_down = 1
    trees = 0
    while go_down != len(list):
        go_right += right
        go_down += down
        if list[go_down-1][go_right-1] == '#':
            trees += 1
    return trees

print(journey(input_list, 3,1)) #148
print(journey(input_list, 1,1)) #50
print(journey(input_list, 5,1)) #53
print(journey(input_list, 7,1)) #64
print(journey(input_list, 1,2)) #29