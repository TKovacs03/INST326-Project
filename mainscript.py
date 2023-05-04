import functions
from exercise import file_reader
from user import User , parse_args
import save

foodcals = {}
def main(user):
    '''execute the workout tracker program.'''
    while True:
        choice = input('What would you like to do? (workout, view history, track calories, bmr, calorie intake, save, or end)\n')
        if choice == 'workout':
            exercise_file = input('What is the name of your exercise file?\n')
            workout_type = input('What kind of workout? (push, pull, or legs)\n')
            print("Your workout is as follows:\n")
            workout = functions.workout_generator(workout_type, file_reader(exercise_file))
            for w in workout:
                print(f"{w['name']}: {w[user.gender]}lbs {w['rep']}\n {w['desc']}")

        elif choice == 'track calories':
            if len(foodcals) < 1:
                bmr = functions.BMR(user.gender, user.height, user.weight, user.age)
                calgoals = round(functions.total_cal_intake(bmr, args.active_level), 0)
                food = input("What food did you eat?\n")
                calories = input("How many calories was it?\n")
                doneornot = input("Are you done eating for the day(True/False)?\n")
                functions.calorie_tracker(food, calories, calgoals, doneornot)
        elif choice == 'bmr':
            bmr = functions.BMR(user.gender, user.height, user.weight, user.age)
            print(f"Your bmr is {bmr}")
        elif choice == 'calorie intake':
            bmr = functions.BMR(user.gender, user.height, user.weight, user.age)
            cal_intake = round(functions.total_cal_intake(bmr, user.active_level), 0)
            print(f"You should intake {cal_intake} calories")
        elif choice == 'view history':
            try:
                save.past_workouts(user.name)
            except:
                print('No preexisting save')
        elif choice == 'save':
            try:
                save.add_save(user.name, workout)
                break
            except:
                save.new_save(user.name, workout)
                break
        elif choice == 'end':
            print('Goodbye!')



if __name__ == "__main__":
    args = parse_args()
    user = User(args.name, args.age, args.height, args.weight, args.gender, args.active_level)
    main(user)