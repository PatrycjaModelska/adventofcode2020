import re

# preparation puzzle input
input_list = []
with open('input_puzzle_4') as file:
    for line in file:
        input_list.append(line.strip())

correct_list = []
temporary_list = []

for el in input_list:
    if el != '':
        temporary_list.extend(el.split(' '))
    else:
        correct_list.append(temporary_list)
        temporary_list = []

# Part I
def check_passport(list):
    first_validation_list = []
    dict = {}
    correct_passport = 0
    for line in list:
        set = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
        for el in line:
            set.remove(el.split(':')[0])
        if len(set) == 0 or (len(set) == 1 and set == {'cid'}):
            correct_passport += 1
            for el in line:
                dict[el.split(":")[0]] = el.split(":")[1]
            first_validation_list.append(dict)
            dict = {}
    return first_validation_list


print(len(check_passport(correct_list)))
# 247

# Part II
def check_passport_2(list):
    first_validation_list = check_passport(list)
    correct_passport = 0
    for dict in first_validation_list:
        correct_key = 0
        for k, v in dict.items():
            if k == 'hgt':
                if "cm" in v:
                    if 150 <= int(v.replace("cm", '')) <= 193:
                        correct_key += 1
                if "in" in v:
                    if 59 <= int(v.replace("in", '')) <= 76:
                        correct_key += 1

            if k == 'byr' and 1920 <= int(v) <= 2002:
                correct_key += 1

            if k == 'iyr' and 2010 <= int(v) <= 2020:
                correct_key += 1

            if k == 'eyr' and 2020 <= int(v) <= 2030:
                correct_key += 1

            if k == 'hcl' and re.findall(r'^#[a-z0-9]{6}', v) != []:
                correct_key += 1

            if k == 'ecl' and v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                correct_key += 1

            if k == 'pid' and len(v) == 9 and v.isdigit():
                correct_key += 1
        if correct_key == 7:
            correct_passport += 1
    return correct_passport


print(check_passport_2(correct_list))
# 145
