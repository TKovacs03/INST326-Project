import functions
import exercise
from user import User
import save


def main(exercise_file, savefile = None):
    '''execute the workout tracker program.'''
    if savefile:
        pass
    else:
        name = input('What is your name?\n')
        age = input('What is your age\n')
        height = input('Your height?\n')
        weight = input('Weight?\n')
        gender = input('Gender?\n')
        level = input('Level of exercise experience (novice, intermediate, expert)\n')
        main_user = User(name, age, height, weight, gender, level)
    
    while True:
        choice = input('What would you like to do? (workout, view history, track calories, save, or end)')
        if choice == 'workout':
            workout_type = input('What kind of workout? (push, pull, or legs)')
            workout = functions.workout_generator(workout_type, exercise_file   )
            print(workout)
        elif choice == 'track calories':
            bmr = functions.BMR(gender, height, weight, age)
            calgoals = functions.total_cal_intake(bmr, level)
            foodcals = {}
            food = input("What food did you eat?")
            calories = input("How many calories was it?")
            doneornot = input("Are you done eating for the day(True/False)?")
            functions.calorie_tracker(food, calories, calgoals, doneornot)
        elif choice == 'bmr':
            bmr = functions.BMR(gender, height, weight, age)
            print(bmr)
        elif choice == 'view history':
            if savefile:
                hist_choice = input("type date in YYYY-MM-DD format for specifc day, or type 'all' for total history.")
                if hist_choice == 'all':
                    save.past_workouts(savefile)
                else:
                    save.past_workouts(savefile, spec_day = hist_choice)
        elif choice == 'save':
            if savefile:
                save.add_save(savefile, workout)
            else:
                fname = input('what would you like to name your file?\n')
                save.new_save(fname, workout, main_user)
        elif choice == 'end':
            print('Goodbye!')
            break
        else:
            raise ValueError('incorrect input')
        

if __name__ == "__main__":
    main()