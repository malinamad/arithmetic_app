import random


def modify_last_number(numbers_line, oper_index, operator):
    num = numbers_line.replace(' ' + operator + ' ', '')
    return num[oper_index:]


def modify_first_number(numbers_line, oper_index):
    num = numbers_line[:oper_index]
    return num


def get_numbers_between_operator(math_line, operator):
    num_index = math_line.index(' ' + operator + ' ')
    first_num = modify_first_number(math_line, num_index)
    last_num = modify_last_number(math_line, num_index, operator)
    return int(first_num), int(last_num)


def generate_easy_math_task():
    random_operator = random.choice(['*', '+', '-'])
    return f'{random.randint(2, 9)} {random_operator} {random.randint(2, 9)}'


def math_operations(math_task):
    if '*' in math_task:
        fst_num, sec_num = get_numbers_between_operator(math_task, '*')
        return fst_num * sec_num
    elif '+' in math_task:
        fst_num, sec_num = get_numbers_between_operator(math_task, '+')
        return fst_num + sec_num
    elif '-' in math_task:
        fst_num, sec_num = get_numbers_between_operator(math_task, '-')
        return fst_num - sec_num
