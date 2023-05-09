# INST326-Project
Fitness Tracking app
    
functions.py file:
    workout_generator function:
        1. It ask user to select an exercise category (ie: Push, Pull or legs)
        2. If the user choice is not in the scope of exercises we offer, it generates a ValueError with a message
        3. But if the selection either push, pull or leg. It accesses the sample_exercise_data.csv and reads content 
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
| file_reader                       | Thomas Kovacs                         | with statement                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------+
| past_workouts                     | Thomas Kovacs                         | keyword argument                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                       |                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                       |                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                       |                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                       |                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                       |                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                       |                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                       |                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------+





