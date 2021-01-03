# preparation puzzle input
input_list = []

with open('input_puzzle_6') as file:
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
def count_yes_answer(list_of_answers):
    all_yes_answer = 0
    for gorup in list_of_answers:
        dict = {}
        for person in gorup:
            for letter in person:
                if dict.get(letter):
                    dict[letter] += 1
                else:
                    dict[letter] = 1
        all_yes_answer += len(dict)

    return all_yes_answer

# good answer: 6437

# Part II
def count_yes_answer_2(list_of_answers):
    all_yes_answer = 0
    for group in list_of_answers:
        dict = {}
        for person in group:
            for letter in person:
                if dict.get(letter):
                    dict[letter] += 1
                else:
                    dict[letter] = 1

        for key in dict.keys():
            if len(group) == dict[key]:
                all_yes_answer += 1

    return all_yes_answer

# good answer: 3229
