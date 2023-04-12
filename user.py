'''
Contains code for the User object. Should be able to:
    store basic user information(height, weight, etc.)
    workout information: 
        maybe a container for user_exercise objects to store user preferences. See docstring for exercise.py

'''
import sys


class User:
    #Initializing the users profile 
    
    
    
    def __init__(self,name,age,height,weight,gender):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        
args_dict = {}
for arg in sys.argv[1:]:
    value = arg.split(" ")
    args_dict["Name"] = sys.argv[1]
    args_dict["Age"] = sys.argv[2]
    args_dict["Height"] = sys.argv[3]
    args_dict["Weight"] = sys.argv[4]
    args_dict["Gender"] = sys.argv[5]

# Create User object with the provided information
user = User(args_dict["Name"], int(args_dict["Age"]), int(args_dict["Height"]), int(args_dict["Weight"]), args_dict["Gender"])

# Print the user's personal information
print(f"Welcome, {user.name}! Your personal information has been saved.")
print(f"You are {user.age} years old, {user.height} inches tall, and weigh {user.weight} pounds.")
print(f"Your gender is {user.gender}.")
        
    
