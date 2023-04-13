'''
Contains code for the User object. Should be able to:
    store basic user information(height, weight, etc.)
    workout information: 
        maybe a container for user_exercise objects to store user preferences. See docstring for exercise.py

'''
import sys


class User:
    #Initializing the users profile 

    def __init__(self,name,age,height,weight,gender,level = None):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.level = level
    
    def __repr__(self):
            """Return a formal representation of the user object."""
            return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Height: {self.height}\n"
            f"Weight: {self.weight}\n"
            f"Gender: {self.gender}\n"
            f"Level: {self.level}"
                )
   


list_dict = []        
args_dict = {}
for arg in sys.argv[1:]:
    value = arg.split(" ")
    args_dict["Name"] = sys.argv[1]
    args_dict["Age"] = sys.argv[2]
    args_dict["Height"] = sys.argv[3]
    args_dict["Weight"] = sys.argv[4]
    args_dict["Gender"] = sys.argv[5]
    args_dict["Level"] = sys.argv[6]


# Create User object with the provided information
user = User(args_dict["Name"], int(args_dict["Age"]), int(args_dict["Height"]), 
            int(args_dict["Weight"]), args_dict["Gender"], args_dict["Level"])
list_dict.append(user)



      
# Print the user's personal information
print(f"Welcome, {user.name}! Your private data has been stored. The details you offered are as follows.")
print(f"You are {user.age} years old, {user.height} inches tall, and weigh {user.weight} pounds.")
print(f"Your gender is {user.gender}.")
print(f"Your indicated that your workour level is {user.level}.")
print(list_dict)

    
