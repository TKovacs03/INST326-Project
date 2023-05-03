import functions
from exercise import file_reader
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
        choice = input('What would you like to do? (workout, view history, track calories, save, or end)\n')
        if choice == 'workout':
            workout_type = input('What kind of workout? (push, pull, or legs)\n')
            print("Your workout is as follows:\n")
            workout = functions.workout_generator(workout_type, file_reader(exercise_file))
            for w in workout:
                print(f"{w['name']}: {w[main_user.gender]}lbs {w['rep']}\n {w['desc']}")
           
            
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
            else:
                print('No preexisting save')
        elif choice == 'save':
            if savefile:
                save.add_save(savefile, workout)
                break
            else:
                fname = main_user.name
                save.new_save(fname, workout, main_user)
                break
        elif choice == 'end':
            print('Goodbye!')
            break
        else:
            raise ValueError('incorrect input')
        

if __name__ == "__main__":
    main('sample_exercise_data.csv')