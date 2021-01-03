# Part I

# preparation puzzle input
def dict_of_rules():
    input_list = []
    with open('input_puzzle_7') as file:
        for line in file:
            for word in [' bags', ' bags,', ' bag', ' bag,', ' ,', ',', '.']:
                line = line.replace(word, '')
            input_list.append(line.strip().split(' contain '))
    rules = {}
    for el in input_list:
        rules[el[0]] = el[1]
    return rules


# recursion_helper generates list of unique bags contains your bag
def recursion_helper(bag_color, rules, result_list):
    for key in rules:
        if bag_color in rules[key]:
            if key not in result_list:
                result_list.append(key)
            recursion_helper(key, rules, result_list)
    return result_list


def where_is_my_bag(bag_color, rules):
    result_list = recursion_helper(bag_color, rules, [])
    return len(result_list)


solution = len(recursion_helper('shiny gold', dict_of_rules(), []))
print(f'Part I: answer is {solution}')


# Part I: answer is 101


# Part II

# preparation puzzle input

def dict_of_rules_2():
    input_list = []
    with open('input_puzzle_7') as file:
        for line in file:
            for word in [' bags', ' bags,', ' bag', ' bag,', ' ,', ',', '.']:
                line = line.replace(word, '')
            input_list.append(line.strip())
    rules = {}

    for line in input_list:
        temporary_list = []
        words = line.split()
        for i in range(0, len(words), 3):
            temporary_list.append(' '.join(words[i:i + 3]))
        rules[temporary_list[0].replace(' contain', '')] = temporary_list[1:]

    for key, items in rules.items():
        rules[key] = {}
        for bag in items:
            temp_bag_list = bag.split()
            rules[key][' '.join(temp_bag_list[1:])] = temp_bag_list[0]

    return rules


all_bags = ['shiny gold']
n = 0
rules = dict_of_rules_2()
list_controler = True

while list_controler == True:
    no_other_number = 0
    temporary_list = []
    for el in all_bags[n:]:
        for key in rules[el]:
            if key == 'other':
                no_other_number += 1
            else:
                for number in range(1, int(rules[el][key]) + 1):
                    temporary_list.append(key)

    if len(all_bags[n:]) == no_other_number:
        list_controler = False
    n = len(all_bags)

    all_bags.extend(temporary_list)

print(f'Part II: answer is {len(all_bags) - 1}')
# Part II: answer is 108636
