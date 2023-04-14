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
        
    
        


    
    

