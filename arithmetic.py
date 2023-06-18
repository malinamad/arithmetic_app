from simple_operations import generate_easy_math_task, math_operations
from user_input_actions import (validate_user_input,
                                difficulty_level_options, save_file_input_validation)
from mark_evaluation_actions import (user_mark_evaluation,
                                     check_whether_result_file_exist, create_result_file)
from integral_squares import random_integral_square_number, evaluate_integral_square


right_answer = 0
user_mark = 0
tasks_num = 0

difficulty_level = difficulty_level_options()

while True:
    if difficulty_level == 1:
        random_easy_math_task = generate_easy_math_task()
        print(random_easy_math_task)
        right_answer = math_operations(random_easy_math_task)
    elif difficulty_level == 2:
        intgrl_sqr_num = random_integral_square_number()
        print(intgrl_sqr_num)
        right_answer = evaluate_integral_square(intgrl_sqr_num)

    user_answer = validate_user_input()

    # mark operations
    if user_mark_evaluation(user_answer, right_answer):
        user_mark += 1

    tasks_num += 1
    if tasks_num == 5:
        if save_file_input_validation(user_mark):
            username = input('What is your name?\n')
            create_result_file(check_whether_result_file_exist(),
                               difficulty_level, username, user_mark)
        break
