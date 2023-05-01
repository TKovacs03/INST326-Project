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
    choice = input('What would you like to do? (workout, view history, track calories, or save)')
    if choice == 'workout':
        workout_type = input('What kind of workout? (push, pull, or legs)')
        functions.workout_generator(workout_type)
    elif choice == 'track calories':
        pass
    elif choice == 'view history':
        pass
    elif choice == 'save':
        pass