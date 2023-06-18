from os import getcwd, path


def user_mark_evaluation(user_answer, right_answer):
    if user_answer == right_answer:
        print('Right!')
        return True
    else:
        print('Wrong!')


def check_whether_result_file_exist():
    file_path = getcwd() + '/results.txt'
    return path.isfile(file_path)


def create_a_new_result_file(username, user_score, difficulty_lvl):
    if difficulty_lvl == 1:
        with open('results.txt', 'w') as f:
            f.write(f'{username}: {user_score}/5 in level 1 '
                    f'(simple operations with numbers 2-9)')
    elif difficulty_lvl == 2:
        with open('results.txt', 'w') as f:
            f.write(f'{username}: {user_score}/5 in level 2 '
                    f'(integral squares 11-29)')


def add_new_score_to_the_file(username, user_score, difficulty_lvl):
    if difficulty_lvl == 1:
        with open('results.txt', 'a') as f:
            f.write(f'\n{username}: {user_score}/5 in level 1 '
                    f'(simple operations with numbers 2-9)')
    elif difficulty_lvl == 2:
        with open('results.txt', 'a') as f:
            f.write(f'\n{username}: {user_score}/5 in level 2 '
                    f'(integral squares 11-29)')


def create_result_file(is_file_exists, difficulty_lvl,
                       username, user_score):
    if is_file_exists:
        add_new_score_to_the_file(username, user_score, difficulty_lvl)
    else:
        create_a_new_result_file(username, user_score, difficulty_lvl)
    print('The results are saved in "results.txt".')
