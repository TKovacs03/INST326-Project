import functions
from exercise import file_reader
import user
import save


def main(user):
    '''execute the workout tracker program.'''
    while True:
        choice = input('What would you like to do? (workout, view history, track calories, save, or end)\n')
        if choice == 'workout':
            exercise_file = input('What is the name of your exercise file?\n')
            workout_type = input('What kind of workout? (push, pull, or legs)\n')
            print("Your workout is as follows:\n")
            workout = functions.workout_generator(workout_type, file_reader(exercise_file))
            for w in workout:
                print(f"{w['name']}: {w[user.gender]}lbs {w['rep']}\n {w['desc']}")

        elif choice == 'track calories':
            bmr = functions.BMR(user.gender, user.height, user.weight, user.age)
            alevel = input("How often do you exercise on a weekly basis(Little to None, Lightly Active,\n Moderately Active, Very Active, Extremely Active)?\n")
            calgoals = functions.total_cal_intake(bmr, alevel)
            foodcals = {}
            food = input("What food did you eat?\n")
            calories = input("How many calories was it?\n")
            doneornot = input("Are you done eating for the day(True/False)?\n")
            functions.calorie_tracker(food, calories, calgoals, doneornot)
        elif choice == 'bmr':
            bmr = functions.BMR(user.gender, user.height, user.weight, user.age)
            print(bmr)
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
    args = user.parse_args()
    main(user.user_information(args.name, args.age, args.height, args.weight, args.gender, args.active_level))