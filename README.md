# INST326-Project
Fitness Tracking app

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


    BMR function:




    total_cal_intake function:



    calorie_tracker function:



    get_BMI function:
        1. It takes hieght and weight as arguments:
            DataFrame series of height and weight are passed into its parameter and returns a series of BMI for each user

    
    showBMI_plot function:
        1. It takes a json file path as argument
        2. Opens the file and reads its content
        3. Creates a new dictionary (df_data) of user names, height and weight.
        4. It passes the dictionary (df_data) into a pandas DataFrame and generates a DataFrame.
        5. Calls the get_BMI funtion to create a new column (bmi) using pandas apply method.
        6. It first shows the created DataFrame
        7. Then uses seaborn to plot a bar graph using user names as 'x' and related bmi as 'y' to create a colorful plot.






+-------------------------------------------------------------------------------------------------------------------------------------------+
| **Method/function**               |    **Primary author**                 |  **Techniques demonstrated**                                  | 
+-------------------------------------------------------------------------------------------------------------------------------------------+
| workout_generator                 |    Gordon Brown                       | list comprehension with filtering                             |
+-------------------------------------------------------------------------------------------------------------------------------------------+
| showBMI_plot                      |    Gordon Brown                       | visualization data using seaborn bar plot                     |
+-------------------------------------------------------------------------------------------------------------------------------------------+
| file_reader                       |    Thomas Kovacs                      | with statement                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------+
| past_workouts                     |    Thomas Kovacs                      | keyword argument                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------+
|user_information                   |   Ewura Impraim                       | use of json.load and json.dump                                |                                                                   
+-------------------------------------------------------------------------------------------------------------------------------------------+
|repr method                        |   Ewura Impraim                       | magic method other than __init__                              |                                        
+-------------------------------------------------------------------------------------------------------------------------------------------+
| parse_args                        |   Ewura Impraim                       | ArgumentParser class from argparse method                    |                  
+-------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                       |                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                       |                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                       |                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                       |                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------+

