def validate_user_input():
    while True:
        try:
            user_answer = int(input())
            return user_answer
        except ValueError:
            print('Incorrect format.')


def difficulty_level_options():
    while True:
        try:
            selected_level = int(input('Which level do you want? Enter a number:\n'
                                       '1 - simple operations with numbers 2-9\n'
                                       '2 - integral squares of 11-29\n'))
            if selected_level != 1 and selected_level != 2:
                raise ValueError
            return selected_level
        except ValueError:
            print('Incorrect format.')


def save_file_input_validation(user_mark):
    true_values = 'y', 'yes'
    saving_result = input(f'Your mark is {user_mark}/5. '
                          f'Would you like to save the result? Enter yes or no.\n')
    if saving_result.lower() in true_values:
        return True
    return False
