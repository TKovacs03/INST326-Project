import functions
import exercise
import user


def main(save = None):
    '''execute the workout tracker program.'''
    if save:
        pass
    else:
        name = input('What is your name?\n')
        age = input('What is your age\n')
        height = input('Your height?\n')
        weight = input('Weight?\n')
        gender = input('Gender?\n')
        level = input('Level of exercise experience (novice, intermediate, expert)\n')
        main_user = user.User(name, age, height, weight, gender, level)
        