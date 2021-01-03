input_list = []

with open('input_puzzle_2') as file:
    for line in file:
        input_list.append(line.strip().split())

prepared_list = []

for el in input_list:
    prepared_list.append({
        'min': int(el[0].split('-')[0]),
        'max': int(el[0].split('-')[1]),
        'letter': el[1][0],
        'password': el[2]
    })

def check_password(list):
    correct_passowrd = 0
    for dict in list:
        if dict['min'] <= dict['password'].count(dict['letter']) <= dict['max']:
            correct_passowrd += 1
    return correct_passowrd

print(check_password(prepared_list))


def check_password_2(list):
    correct_passowrd = 0
    for dict in list:
        if dict['password'][dict['min']-1] == dict['letter'] and dict['password'][dict['max']-1] != dict['letter']:
            correct_passowrd += 1
        elif dict['password'][dict['min']-1] != dict['letter'] and dict['password'][dict['max']-1] == dict['letter']:
            correct_passowrd +=1
    return correct_passowrd

print(check_password_2(prepared_list))