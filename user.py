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
        
     # Get user's personal information from command line arguments 
    def add_user(self):
        print("Please give your height in inches")
        user_profile = {}
        self.name = sys.argv[1]
        self.age = int(sys.argv[2])
        self.height = int(sys.argv[3])
        if isinstance(self.height,str):
            print("Please provide a number in inches for your height!") 
        self.weight = int(sys.argv[4])
        self.gender = sys.argv[5]
        
        # Save the user's personal information to the dictionary
        user_profile["Name"] = self.name
        user_profile["Age"] = self.age
        user_profile["Height"] = self.height
        user_profile["Weight"] = self.weight
        user_profile["Gender"] = self.gender
       
        # Print the user's personal information
        print(f"Welcome, {self.name} Your personal information has been saved.")
        print(f"You are {self.age} years old, {self.height} inches tall, and weigh {self.weight} pounds.")
        print(f"Your gender is {self.gender}.")
        