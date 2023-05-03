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

def workout_generator(workout_type):
    """ A function that generates random workout base on user category.
    
    The function takes user workout category to generate random workout
    
    Returns:
        sets (int): The number of exercise set the user performs
        reps (int): The number of repetitions a user performs within a set
        weight (int): The weight needed to perform the exercise
        description (str): Step-by-step instructions of the exercise
    
    """
    
    workout_dict = {
        "push": ['push-up', 'bench press', 'shoulder press', 'dips'],
        "pull": ['pull-up', 'lat pulldown', 'row', 'bicep curl'],
        "legs": ['squat', 'deadlift', 'leg press', 'lunges'] 
    }
    
    desc = {
        "push-up": """
      1. Start in a plank position with hands wider & feet together
      2. Lower body to the ground with elbow bent and body in straight position
      3. Chest touch the ground, arm 90-degrees angle.
      4. Push back up to a start position. Repeat for desired number of rep
       """,
      "bench press": """
      1. Lie down on a flat bench, feet flat on the ground & eye under the bar
      2. Grab bar & lift bar off the rack with arm fully extended
      3. Lower bar to chest & keep elbow tucked in close to your side
      4. Once bar tounches chest, push bar back up to starting position
      5 Press feet into the ground & extend your arm. Repeat for desired rep
      """,
      "shoulder press":"""
      1. Hold dumbell in each hand at shoulder height with elbow bent.
      2. feet must be shoulder-width apart, keeping your back straight.
      3. Push dumbbells up overhead, fully extending your arms, while exhaling
      4. Pause at the top of the movement, squeezing your shoulder muscles.
      5. Lower the dumbbells down to the starting position, inhaling as you go.
      6. Repeat for the desired number of reps.
      """,
      "dips":"""
      1. Use a parallel bar. Place hands on the bars, palms facing down
      2. Lift yourself up so that your arms are straight & feet off the ground.
      3. Lower body by bending your arms & leaning forward slightly
      4. Keeping your elbows pointed behind you
      5. Push yourself up by straightening your arms, return to start position.
      6. Repeat for the desired number of reps. 
      """,
      "pull-up":"""
      1. Hanging from a pull-up bar with your palms facing away from you 
         and your hands shoulder-width apart.
      2. Engage your shoulder blades and keep your elbows close to your body.
      3. Pull yourself up towards the bar.
      4. Continue to pull slowly lower yourself back down to the start position.
      5. Repeat for the desired number of repetitions.
      """,
      "lat pulldown":"""
      1. Sit down on the lat pulldown machine and adjust the thigh pad so that 
         it fits snugly against your thighs.
      2. Grasp the bar with an overhand grip that is slightly wider than 
         shoulder-width apart. Your palms should be facing away from you.
      3. Sit with your back straight and your chest up. 
         Your feet should be flat on the ground
      4. Start the movement by pulling the bar down towards your chest.
      5. Pause when bar is close to chest and release it back up to straight 
         position
      6. Repeat the movement for the desired number of reps.
      """,
      "row":"""
      1. Begin by standing with your feet hip-width apart & knees bent.
      2. Hold a dumbbell in each hand with your palms facing towards your body.
      3. Hinge forward, keeping your back straight & your core engaged. 
      4. Your arms should be hanging straight down towards the floor.
      5. Pull dumbbells up towards your chest, & keeping them close to body.  
         Squeeze shoulder blades together as you lift the weights.
      6. Pause briefly at the top of the movement, slowly lower the dumbbells 
         back down to the starting position.
      7. Repeat the movement for the desired number of reps.
      """,
      "bicep curl":"""
      1. Stand up straight with feet shoulder-width apart, and hold dumbbell in 
         each hand with an underhand grip (palms facing upwards).
      2. Keep elbows close to your sides & upper arms stationary throwout.
      3. Slowly lift the dumbbells towards shoulders while contracting biceps 
         muscles, making sure wrists straight.
      4. Pause a sec. at the top of the movement. Then slowly lower dumbbells
      5. Repeat the movement for the desired number of reps.
      """,
      "squat":"""
      1. Stand with feet shoulder-width apart & toes pointing slightly outwards.
      2. Tighten your core muscles and keep your chest lifted.
      3. Lower hips & bend your knees, as if you're sitting back into a chair.
      4. Keep your knees in line with your toes and your weight in your heels.
      5. Lower down until your thighs are parallel to the ground, or as low as 
         you can comfortably go.
      6. Pause a moment, push through heels to return to the starting position.
      7. Repeat the movement for the desired number of reps.
      """,
      "deadlift":"""
      1. Standing with your feet shoulder-width apart, toes pointing forward &
         your shins almost touching the barbell.
      2. Bend down & grab the bar with an overhand grip, making sure that your
         hands are shoulder-width apart
      3. Keep arms straight & back flat as you lift the bar up off the ground, 
         using your legs & hips to drive the movement.
      4. Once the bar passes your knees, squeeze your glutes & drive your hips 
         forward to complete the lift.
      5. Slowly lower bar back down to the ground, making sure to keep your back
         flat & your core engaged throughout the movement.
      6. Repeat the movement for the desired number of reps.
      """,
      "leg press":"""
      1. Sit on the leg press machine with back flat against the pad & your feet
         shoulder-width apart on the foot plate. knees bent at a 90-degree angle
         & hands should be gripping the handles on either side of the seat.
      2. Press foot plate away from you by extending your legs. Be sure to keep 
         your feet flat on the plate & your back pressed firmly against the pad.
      3. Lower the weight back down by bending your knees & allowing the foot 
         plate to come towards you. Keep movements slow & controlled, avoiding 
         any sudden jerks or movements.
      4 Repeat the movement for the desired number of reps.
      """,
      "lunges":"""
      1. Stand up straight with your feet hip-width apart & hands on your hips.
      2. Take a step forward with right foot & lower your body down by bending 
         both knees. Keep your back straight & core engaged.
      3. Continue lowering body until your right thigh is parallel to the ground
         & left knee is hovering just above the floor.
      4. Push back up through right heel to return to the starting position.
      5. Repeat the same movement with your left foot forward.
      """
        
    }
    

    
    if workout_type not in list(workout_dict):
        raise ValueError("Your selection is not in the list")
    
    if workout_type == "push":
        exercises = workout_dict["push"]
    
    elif workout_type == "pull":
        exercises = workout_dict["pull"]
    
    elif workout_type == "legs":
        exercises = workout_dict["legs"]
        
    # Generate a workout consisting of a random number
    num_exercises = random.randint(3, 5)
    workout = list()
    
    for num in range(num_exercises):
        exercise = random.choice(exercises)
        num_sets = random.randint(4, 6)
        reps = random.randint(15, 30)
        weight = random.randint(35, 100)
        workout.append((exercise, num_sets, reps, weight))
    
    
    for exercise, num_set, reps, weight in workout:
        return (f"Your workout today: "\
            f"{exercise} => {num_set} sets of {reps} reps at {weight} lbs"\
                f"{desc[exercise]}")
        


# BMR Calculation function and Total Calorie Intake function

def BMR(gender, height, weight, age):
    
    bmr1 = ((12.7 * height) + (6.23 * weight) - (6.8 * age))
    
    bmr2 = ((4.7 * height) + (4.35 * weight) - (4.7 * age))

    yourbmr = bmr1 if gender == "Male" else bmr2
    return yourbmr

def total_cal_intake(bmr, active_level):
    if active_level == "Little to None":
        daily_cals = (bmr * 1.2)
        return daily_cals
    
    elif level == "Lightly Active":
        daily_cals = (bmr * 1.375)
        return daily_cals
    
    elif level == "Moderately Active":
        daily_cals = (bmr * 1.55)
        return daily_cals
    
    elif level == "Very Active":
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

        
        
        
        


    
    

