# INST326-Project
Fitness Tracking app

Framework:

main script:
1. ask if user would like to load save
    yes: load save (set up user object from dict of attributes, use same excercise dictionary as last time)
    no: ask user for attributes, and for exercise csv file

2. ask user what they'd like to do:

    workout: use workout generator to make workout, either push, pull or legs from user input.
            display instructions if need be, then ask if the workout was too easy, too hard, or just right.
            edit csv by adding/removing weights for next time. 
            store workout in a dictionary for saving

    view past workouts: if save file present, allow user to see completed workouts and cardio from past usage.
            
    
    track calories: use user attributes to calculate calorie goal
                    ask user for calories consumed, display amount still needed
                    track cardio exercise

    save: print user info to file.
          print accomplished workout to pastworkouts dict
          print cardio/calorie data to pastworkouts dict
