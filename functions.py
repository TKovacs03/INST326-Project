import random


'''Miscellaneous functions not included in either user or exercise file.
Can also be used to write a preliminary main script for testing

Should contain:
    workout generator:
        ask user what kind of workout they'd like, and select workouts based on this input.
        should hit every muscle group in selected type of workout:
            push: chest, shoulders, triceps
            pull: Biceps, back, lats
            legs: quads, hamstrings, glutes
        display weight and repetition range, as well as exercise description if user asks for it.
            
    workout saver:
        should take user input for their performance on each exercise
        use this information to create new user_exercise objects and add them to user's container if it's the first time they've done it,
        or modify existing user_exercise objects
        i.e. if the user says their bench press set was very easy, add 5-10 pounds.
        
    calorie tracker:
        
'''

def workout_generator():
    """ A function that generates random workout base on user category.
    
    The function takes user name and workout category to generate random workout
    
    Side effects:
        It prints to stdout user name and randomly selected workouts
    
    """
    
    workout_dict = {
        "push": ['push-up', 'bench press', 'shoulder press', 'dips', 'tricep extensions'],
        "pull": ['pull-up', 'lat pulldown', 'row', 'bicep curl', 'face pull'],
        "legs": ['squat', 'deadlift', 'leg press', 'lunges', 'calf raise'] 
    }
    
    
    # Ask user for workout choice:
    name = input("Enter your name full name, (eg: John Miles): ")
    workout_type = input("What type of workout would you like? (push, pull, legs): ")

    
    if workout_type not in list(workout_dict):
        raise ValueError("Your selection is not in the list")
    
    if workout_type == "push":
        exercises = workout_dict["push"]
    
    elif workout_type == "pull":
        exercises = workout_dict["pull"]
    
    else:
        exercises = workout_dict["legs"]
        
    # Generate a workout consisting of a random number
    num_exercises = random.randint(2, 4)
    workout = list()
    
    for num in range(num_exercises):
        exercise = random.choice(exercises)
        num_sets = random.randint(4, 6)
        reps = random.randint(15, 30)
        weight = random.randint(35, 100)
        workout.append((exercise, num_sets, reps, weight))
    
    
    print(f"\nHi! {name} your workout for today:")
    for exercise, num_set, reps, weight in workout:
        print(f"{exercise} => {num_set} sets of {reps} reps at {weight} lbs")
        


# BMR Calculation function and Total Calorie Intake function

def BMR(gender, height, weight, age):
    
    bmr1 = ((12.7 * height) + (6.23 * weight) - (6.8 * age))
    
    bmr2 = ((4.7 * height) + (4.35 * weight) - (4.7 * age))

    bmr1 if gender == "Male" else bmr2

    
def total_cal_intake(bmr, active_level):
    if active_level == "Little to None":
        daily_cals = (bmr * 1.2)
        return daily_cals
    
    elif active_level == "Lightly Active":
        daily_cals = (bmr * 1.375)
        return daily_cals
    
    elif active_level == "Moderately Active":
        daily_cals = (bmr * 1.55)
        return daily_cals
    
    elif active_level == "Very Active":
        daily_cals = (bmr * 1.725)
        return daily_cals
    
    else:
        daily_cals = (bmr * 1.9)
        return daily_cals
#Alex Hildebrand Function   
foodcals = {}
def calorie_tracker(food, calories, done = False, goal = 2000):
    """Allows you to see the foods you've eaten and their calories and updates you on where you
    are at in reaching your calorie goal
    Args:
        food(str): What food you ate
        calories(int): the calorie count for the corresponding food
        goal(int, optional) = The amount of calories you want to have for the day, default is 2000
        done(boolean, optional): Whether you are done eating for the day, default is False meaning not 
        done
    Returns: String of the foods and calories in the dictionary and how many more calories you need
    to hit your goal
    Side Effects: Prints to the console and changes global variable"""
    foodcals[food] = calories
    total_calories = sum(foodcals.values())
    if total_calories < goal:
        for key in foodcals:
            print(f"{key}: {foodcals[key]} calories")
        print(f"You still need to eat {goal - total_calories} calories")
    if done == True:
        for key in foodcals:
            print(f"{key}: {foodcals[key]} calories")
        print(f"You were {goal - total_calories} calories short")
        for key in foodcals:
            foodcals.pop()
    if goal <= total_calories <= goal + 200:
        for key in foodcals:
            print(f"{key}: {foodcals[key]} calories")
        print(f"You roughly ate your specified calorie count goal!")
        foodcals.clear()
    if goal +200 < total_calories:
        for key in foodcals:
            print(f"{key}: {foodcals[key]} calories")
        print("You may have overeaten your calorie goal")
        foodcals.clear

        


    
    

