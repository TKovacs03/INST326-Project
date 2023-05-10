import random
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



""" Miscellaneous functions used in mainscript.py """



def file_reader(file):
    '''
    TJ Kovacs
    Create a list of dictionaries of exercises from a csv file, format:
    name; maleweight; femaleweight; setsxreps; workout type; description
    for use in workout generation. 
    
    Args: 
    file(str): name of csv file
    
    Returns:
        exercise_list(list of dict): a list of dictionaries.
    
    '''
    exercise_list = []
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            e_dict = {}
            l = line.split(';')
            e_dict['name'] = l[0]
            e_dict['m'] = l[1]
            e_dict['f'] = l[2]
            e_dict['rep'] = l[3]
            e_dict['group'] = l[4]    
            e_dict['desc'] = l[5]        
            exercise_list.append(e_dict)
    return exercise_list



def workout_generator(workout_type, workout_list):
    """ A function that generates random workout base on user categorical choice.
    This function takes user workout choice (push, pull or legs)  and a list of exercises to generate random workout.
    
    
    Args:
        workout_type (str): it takes a workout selection of pull, push or legs
        work_list (list): a list of exerices types 

    Returns:
        sets (int): The number of exercise set the user performs
        reps (int): The number of repetitions a user performs within a set
        weight (int): The weight needed to perform the exercise
        description (str): Step-by-step instructions of the exercise
    
    """
    
    workout_types = ['push', 'pull', 'legs']
    
    if workout_type not in workout_types:
        raise ValueError("incorrect input")
    
    exercise_options =  [w for w in workout_list if w['group'] == workout_type]
    
        
    workout = []
    while len(workout) < 3:
        exercise = random.choice(exercise_options)
        if exercise not in workout:
            workout.append(exercise)
    
    return workout
        


# BMR Calculation function and Total Calorie Intake function

def BMR(gender, height, weight, age):
    """Allows for a user to have their Basal Metabolic Rate (BMR) calculated utilizing user information from User class.
    Args:
        gender: the user's specified gender
        height: the user's specified height
        weight: the user's specified weight
        age: the user's specified age
        
    Returns:
        BMR based off of user's gender, weight, height, and age
    """
    bmr1 = ((12.70 * height) + (6.23 * weight) - (6.80 * age) + 66)
    
    bmr2 = ((4.70 * height) + (4.35 * weight) - (4.70 * age) + 655)

    yourbmr = bmr1 if gender == "Male" else bmr2 #utilizes conditional expression skill
    return yourbmr

def total_cal_intake(bmr, level):
    """Calculates the recommended daily caloric intake amount necessary for a user utilizing their BMR and their activity level.
    Args:
        bmr: Basal Metabolic Rate (BMR) of the user
        level: the average level of activity user partakes in on a weekly basis
    Returns:
        the recommended daily calories necessary for user based on their activity level
    """
    if level == "Little/None":
        daily_cals = (bmr * 1.200)
        return daily_cals
    
    if level == "Light":
        daily_cals = (bmr * 1.375)
        return daily_cals
    
    if level == "Moderate":
        daily_cals = (bmr * 1.550)
        return daily_cals
    
    if level == "High":
        daily_cals = (bmr * 1.725)
        return daily_cals
    
    if level == "Extreme":
        daily_cals = (bmr * 1.900)
        return daily_cals

#Alex Hildebrand Function
foodcalu = {}   
foodcals = {}
class Calorie_tracker:
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
    def __init__(self,food, calories, goal, done = "No"):
        calories = int(calories)
        foodcalu[food] = calories
        foodcals = dict(self.most_cals(foodcalu))
        total_calories = sum(foodcals.values())
        if total_calories < goal:
            for key in foodcals:
                print(f"{key}: {foodcals[key]} calories")
            print(f"You still need to eat {goal - total_calories} calories")
        if done == "Yes":
            for key in foodcals:
                print(f"{key}: {foodcals[key]} calories")
            print(f"You were {goal - total_calories} calories short")
            foodcals.clear()
        if goal <= total_calories <= goal + 200:
            for key in foodcals:
                print(f"{key}: {foodcals[key]} calories")
            print(f"You roughly ate your specified calorie count goal!")
            foodcals.clear()
        if goal +200 < total_calories:
            for key in foodcals:
                print(f"{key}: {foodcals[key]} calories")
            print("You may have overeaten your calorie goal")
            foodcals.clear()
    def most_cals(self, di):
        """Sorts the dictionary displaying in order the most to least calories for each food to give the user
     a better perspective of where most of their calories are coming from
     Args:
        di(dictionary): a dictionary in the proper format
    Returns: The input dictionary sorted by foods with the most calories first
     """
        foodcals = sorted(di.items(), key=lambda x: x[1], reverse=True)
        return foodcals

def get_BMI(height, weight):
    """" A function that determines if a person is underweight to obese.
    
    Args:
        height (int): it take a person height in inches
        weight (int): it takes a person weight in pounds
        
    Returns:
        bmi (float): it returns a float of a person health bmi
            Underweight: BMI < 18.5
            Normal weight: 18.5 < BMI < 24.9
            Overweight: 25 < BMI < 29.9
            Obese: BMI => 30
    
    """
    
    height_meters = height * 0.025
    weight_kg = weight * 0.45
    bmi = weight_kg / (height_meters ** 2)
    return bmi


def showBMI_plot(jsonpath):
    """A function that shows users BMI visualization, using users weight and height in json file.
    
    Args:
        jsonpath (str): It takes a json file path 
        
    Side effects:
        It shows a bar graph and a DataFrame records of users BMI to stdout 
    
    """
    
    with open(jsonpath, 'r') as fhand:
        user_info = json.load(fhand)

    list_of_dict = []
    df_data ={'name':[],
            'height':[],
            'weight':[]}
    list_of_dict = [user_info[keys] for keys in user_info] # conditional expression
  
    for user in list_of_dict:
        
        df_data['name'].append(user['name'])
        df_data['height'].append(user['height'])
        df_data['weight'].append(user['weight'])

    df = pd.DataFrame(df_data)
    df['bmi'] = df.apply(lambda x: get_BMI(x['height'], x['weight']),\
        axis=1).round(1)
    
    sns.barplot(data=df, x='name', y='bmi')
    print(f"\n{df}")
    plt.show()
  
    
    