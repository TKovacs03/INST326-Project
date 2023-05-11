# INST326-Project
Fitness Tracking app

Instructions on how to use our app:
    1. In the commandline, run mainscript.py with the following values:
       name age height(in inches) weight(lbs) gender('m' or 'f') activity (Little/None, 
       Light, Moderate, High, Extreme)

    2. Follow instructions printed to terminal. Be sure to type options exactly
       as they appear in terminal
       Note: (end) option will completely terminate the program.
             Parse user info. to start app again
             

mainscript.py file:
    mainscript.py is the heart of our app. It intergrates with all the various
    scripts (class, methods and functions) in our program.

    main function:
        1. When the program starts, parse_args function gets invoked

        2. It takes user input (name, age, height, weight, gender: "m" or "f" & active level)
           as commandline argument 

        3. The input is used to generate user object

        4. The user object is passed as positional argument to main function

        5. main function ask for user choice which is used to compute different modules
           within our program:
                (workout, track calories, bmr, calorie intake, view history, save file,
                 end program, add user to records if user doesn't exist & BMI visualization)
        




user.py file:
    1. The User class initializes the following attributes:
        name of user(str)
        age of user(int)
        height of user in inches(int)
        weight of user in pounds(int)
        gender of user (str)
        active level of user is either "Little/None",
        "Light","Moderate","High","Extreme"(str)

    2. Repr method is used to return the formal string representation of 
    the attributes.

    3. The user_information method opens a JSON file and loads the information 
    provided by the user. It prints out the welcome message and repeats the 
    users information for final verification. The information is saved in a 
    dictionary in a JSON file and uses the users name as a key. 

    4. The parse_args method is used to parse the command line arguments 
    provided by the user and returns it to its appropriate attributes.


functions.py file:
    workout_generator function:
        1. It ask user to select an exercise category (ie: Push, Pull or legs)

        2. If the user choice is not in the scope of exercises we offer, it generates a ValueError with a message

        3. But if the selection is either push, pull or leg. It accesses the sample_exercise_data.csv and reads content 
           to workout_generator function.

        4. The function uses list comprehension with filtering and random choice to select specific exercises for the user
           based on user choice and gender.

        5. It also gives a description of the various workout that the user might perform.



    workout_checkin function:
        1. The user will be asked to state the intensity and difficulty at which they felt their workout was performed for
           which the user will answer with their intensity score as a number from 1-10, followed by a comma, and then their difficulty [too easy, too hard, just right].

        2. The function will use sequence unpacking to store the user's answers into the variables "intensity" and "difficulty".

        3. Based on the user's answers, it will perform various if statements to determine what the user should proceed doing for
           future workouts based on the intensity and difficulty.

        4. The function will print out a description based on the intensity and difficulty specified by the user.


    BMR function:
        1. It will utilize input data (gender, height, weight, age) from a JSON file containing user information.

        2. The user's information will be utilized within a formula used to calculate the user's Basal Metabolic Rate (BMR).

        3. There are two formula options, one for male (bmr1) and another for female (bmr2), and the function will utilize a
           conditional expression to determine which formula to use.

        4. The user information pertaining to each parameter in the formula will be plugged into the formula and the function will
           then calculate and return user's BMR as the variable, "yourbmr".


    total_cal_intake function:
        1. The function will use two arguments, the user's calculated bmr (bmr) and activity level (level).

        2. The function takes the activity level stated by the user and checks to see if it matches the level for one of the
           if statements.

        3. Once determined, the bmr will be multiplied by a set number in order to calculate the number of
           calories they need to intake; the calculation will be set to the variable "daily_cals"

        4. The function will then return daily_cals back to the user as an integer 


    calorie_tracker class:
        1. Takes the calorie goal from the get_BMI and calorie_intake function and plugs it in
    
        2. Asks the user what food they ate, how many calories that food has, and ig they are done eating and have not reached their calorie goal
    
        3. Adds the food and calories to a dictionary as a key/value pair
    
        4. Returns a string of each food and calories associated with that food with the amount of calories left to eat in the day, if finished shows the string and a messge to the user that they met or went over their calorie goal
    
        5. If you are done eating and have not met the goal prints how many calories short you were

    most_cals method:
        1. Takes the dictionary of food/calories in the calorie_tracker class

        2. Replaces dictionary within class so the highest caloric foods are first for the string given bacck to the user

    get_BMI function:
        1. It takes height and weight as arguments:
            DataFrame rows of height and weight are passed as arguments & returns a BMI series 

    
    showBMI_plot function:
        1. It takes a json file path as argument

        2. Opens the file and reads its content

        3. Creates a new dictionary (df_data) of user names, height and weight.

        4. It then passes the dictionary (df_data) into a pandas DataFrame and generates a DataFrame.

        5. It calls the get_BMI funtion to create a new column (bmi) using pandas apply method.

        6. It first prints the users body mass index records

        7. Then it uses seaborn to plot a colorful bar graph:  names on x-axis & bmi on y-axis.


save.py file:
    new_save function:
        1. takes the name of the user, the workouts they've completed today,

        2. creates a .txt file named after the user with the workout and date.


    add_save function:
        1. same as new save, but writes to existing file if present


    past_workouts function:
        1. takes user name and optional date
        2. returns full file if no optional date
        3. searches for specific date and returns it if date


sample_exercise_data.csv file:
    provides exercises for the program to choose from, and all information.
    could theoretically be substituted with any file of correct format.





+-------------------------------------------------------------------------------------------------------------------------------------+
| **Method/function**               |    **Primary author**                 |  **Techniques demonstrated**                            | 
+-------------------------------------------------------------------------------------------------------------------------------------+
| workout_generator                 |    Gordon Brown                       | list comprehension with filtering                       |
+-------------------------------------------------------------------------------------------------------------------------------------+
| showBMI_plot                      |    Gordon Brown                       | visualization data using seaborn bar plot               |
+-------------------------------------------------------------------------------------------------------------------------------------+
| file_reader                       |    Thomas Kovacs                      | with statement                                          |
+-------------------------------------------------------------------------------------------------------------------------------------+
| past_workouts                     |    Thomas Kovacs                      | keyword argument                                        |
+-------------------------------------------------------------------------------------------------------------------------------------+
| user_information                  |    Ewura Impraim                      | use of json.load and json dump                          |
+-------------------------------------------------------------------------------------------------------------------------------------+
| repr method                       |    Ewura Impraim                      | formal string representation of User class attributes   |
+-------------------------------------------------------------------------------------------------------------------------------------+
| parse_args                        |    Ewura Impraim                      | ArgumentParser class from argparse                      |
+-------------------------------------------------------------------------------------------------------------------------------------+
| calorie_tracker                   |    Alex Hildebrand                    | f-string w/expression                                   |
+-------------------------------------------------------------------------------------------------------------------------------------+
| most_cals                         |    Alex Hildebrand                    | key function w/sorted                                   |
+-------------------------------------------------------------------------------------------------------------------------------------+
| workout_checkin                   |    Simon Huynh                        | sequence unpacking                                      |
+-------------------------------------------------------------------------------------------------------------------------------------+
| BMR                               |    Simon Huynh                        | conditional expression                                  |
+-------------------------------------------------------------------------------------------------------------------------------------+

