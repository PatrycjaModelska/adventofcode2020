# preparation

def get_rules():
    input_list = []
    with open('input_puzzle_8') as file:
        for line in file:
            input_list.append(line.strip().split(' '))
    rules = []
    for el in input_list:
        rules.append([el[0], el[1][0], int(el[1][1:])])
    return rules


# main function

def accumulator_value():
    rules = get_rules()
    used_index = []
    acc_value = 0
    n = 0
    while n not in used_index:
        used_index.append(n)
        if rules[n][0] == 'acc' and rules[n][1] == '-':
            acc_value -= rules[n][2]
            n += 1
        elif rules[n][0] == 'acc' and rules[n][1] == '+':
            acc_value += rules[n][2]
            n += 1
        elif rules[n][0] == 'jmp' and rules[n][1] == '+':
            n += rules[n][2]
        elif rules[n][0] == 'jmp' and rules[n][1] == '-':
            n -= rules[n][2]
        else:
            n += 1

    return acc_value


print(accumulator_value())


# good answer: 1200

# part II

# checker() return index where you should put "nop" instead jmp

def checker():
    for index, el in enumerate(get_rules()):
        if el[0] == 'jmp':
            rules = get_rules()
            used_index = []
            acc_value = 0
            n = 0
            while n not in used_index and n < len(rules):
                used_index.append(n)
                if rules[n][0] == 'acc' and rules[n][1] == '-':
                    acc_value -= rules[n][2]
                    n += 1
                elif rules[n][0] == 'acc' and rules[n][1] == '+':
                    acc_value += rules[n][2]
                    n += 1
                elif rules[n][0] == 'jmp' and rules[n][1] == '+':
                    if n != index:
                        n += rules[n][2]
                    else:
                        n += 1
                elif rules[n][0] == 'jmp' and rules[n][1] == '-':
                    if n != index:
                        n -= rules[n][2]
                    else:
                        n += 1
                else:
                    n += 1

                if (len(rules) - 1) in used_index:
                    return index, acc_value

    return "We don't find anything interesting!"


print(checker())
