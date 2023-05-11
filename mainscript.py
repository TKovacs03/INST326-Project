import functions
from user import User , parse_args
import save
import json


foodcals = {}

def main(user):
    '''execute the workout tracker program.'''
    while True:
        choice = input('What would you like to do?(workout, workout check-in, view history, '
                       'track, calories, bmr, calorie intake, save, '
                       'add user, bmi plot or end)\n')
        
        if choice == 'workout':
            exercise_file = "sample_exercise_data.csv"   
            workout_type = input('What kind of workout? (push, pull, legs)\n')
            print("Your workout is as follows:\n")
            workout = functions.workout_generator(
                workout_type, functions.file_reader(exercise_file)
                )
            for w in workout:
                print(f"{w['name']}: {w[user.gender]}lbs {w['rep']}\n {w['desc']}")

        elif choice == 'workout check-in':
            post_workout = input("Post workout check-in.\n"
                                 "Enter in format: how intense was your workout (on a scale from 1-10), " 
                                 "difficulty [too easy, too hard, just right]\n")
            functions.Workout_checkin(post_workout)

        elif choice == 'track calories':
                bmr = functions.BMR(user.gender, user.height, user.weight, user.age)
                calgoals = functions.total_cal_intake(bmr, args.active_level)
                calgoals = round(calgoals, 0)
                food = input("What food did you eat?\n")
                calories = input("How many calories was it?\n")
                doneornot = input("Are you done eating for the day and will"
                                  "not hit your calorie goal(Yes/No)?\n")
                functions.Calorie_tracker(food, calories, calgoals, doneornot)
                
        elif choice == 'bmr':
            bmr = functions.BMR(user.gender, user.height, user.weight, user.age)
            print(f"Your bmr is {bmr}")
            
        elif choice == 'calorie intake':
            bmr = functions.BMR(user.gender, user.height, user.weight, user.age)
            cal_intake = round(functions.total_cal_intake(bmr, user.active_level), -1)
            print(f"You should intake {cal_intake} calories")
            
        elif choice == 'view history':
                date = input(
                    "if you'd like to view a specific date, type it in" 
                    " YYYY-MM-DD format. Otherwise type none\n"
                    )
                if date in ('none', 'None') :
                    save.past_workouts(user.name)
                else:     
                    save.past_workouts(user.name, spec_day = date)
            
        elif choice == 'save':
            try:
                save.add_save(user.name, workout)
                break
            except:
                save.new_save(user.name, workout)
                break
            
        elif choice == 'end':
            print("Goodbye!")
            break
            
        elif choice == "add user":
            with open("user_information.json", "r") as f:
                users_output = json.load(f)
                
            name = input("Enter your name:\n")
            age = input("Enter your age:\n")
            height = input("Enter your height in inches:\n")
            weight = input("Enter your weight in pounds:\n")
            gender = input("Enter your gender:\n")
            active_level = input("Enter your active_level, either Little/None,"
                                 "Light, Moderate, High, Extreme :\n")
        
            if name in users_output:
                print("We already have your information. Thank you!")
                
            else:
                user_dict = {
                        "name": name,
                        "age": age,
                        "height": height,
                        "weight": weight,
                        "gender": gender,
                        "active_level": active_level,
                        }
                    
                users_output[name] = user_dict
                
                with open("user_information.json", "w") as f:
                    json.dump(users_output, f, indent = 4)
                    
            print(f"Welcome, {name}! Your private data has been stored. The"
                  "details you offered are as follows.")
            print(f"You are {age} years old, {height} inches tall, and weigh {weight} pounds.")
            print(f"Your gender is {gender}.")
            print(f"You indicated that your weekly activity level is {active_level}.") 
            
        elif choice == "bmi plot":
            functions.showBMI_plot("user_information.json")   



if __name__ == "__main__":
    args = parse_args()
    user = User(args.name, args.age, args.height, args.weight, args.gender, args.active_level)
    main(user)
    
    