from argparse import ArgumentParser
import json 


class User:
    """
    Attributes: 
    Represents a user's information. 
    
    """
    
    def __init__(self, name, age, height, weight, gender, active_level=None):
        """ Sets and initailizes attributes.
        
        Args:
        name(str) : name of user
        age(int): age of user
        height(int): height of user in inches
        weight(int): weight of user in pounds
        gender(str): gender of user 
        active(str): active level of user
        """
        
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.active_level = active_level
    
    def __repr__(self):
        """
        Produce a formal string representation of a user.
        
        Returns:
        str: the string representation.
        """
        
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Height: {self.height}\n"
            f"Weight: {self.weight}\n"
            f"Gender: {self.gender}\n"
            f"Level: {self.active_level}"
        )


    def user_information(self):
        """
        This method saves the information provided by user in a JSON file. 
        
        Side effects:
        The attributes provided by the user are stored in a dictionary.
        Displays a welcome message and the provided information of user.
        The user information is loaded from and dumped into 
        the user_infromation JSON file.
    
        """
        
        with open("user_information.json", "r") as f:
            users_output = json.load(f)
        
        print(f"Welcome, {self.name}! Your private data has been stored. The details you offered are as follows.")
        print(f"You are {self.age} years old, {self.height} inches tall, and weigh {self.weight} pounds.")
        print(f"Your gender is {self.gender}.")
        print(f"You indicated that your weekly activity level is {self.active_level}.")
        if self.name in users_output:
            print(self)

        else:
            user_dict = {
                "name": self.name,
                "age": self.age,
                "height": self.height,
                "weight": self.weight,
                "gender": self.gender,
                "active_level": self.active_level,
                }
        
            users_output = {"Users"}
            with open("user_information.json", "r") as f:
                users_output = json.load(f)
            
            users_output[self.name] = user_dict
        
            with open("user_information.json", "w") as f:
                json.dump(users_output, f, indent = 4)
            print (self)
        

        
def parse_args():
    """ Parse command-line arguments.
    
    Expects six mandatory arguments:
        name: the name of the user (str)
        age: the age of the user (int)
        height: the height of user in inches (int)
        weight: the weight of user in pounds (int)
        gender: the gender of user (str)
        active_level: the workout level of the user (str)
    
    Returns:
        namespace: an object with attributes for each argument.
    """
    
    parser = ArgumentParser()
    parser.add_argument("name", type=str, help="name of user")
    parser.add_argument("age", type=int, help="age of the user")
    parser.add_argument("height", type=int, help="height of the user in inches")
    parser.add_argument("weight", type=int, help="weight of the user in pounds")
    parser.add_argument("gender", type=str, help="gender of the user")
    parser.add_argument("active_level", type=str, help="workout level of the user")
    
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    user = User(args.name, args.age, args.height, args.weight, args.gender, args.active_level)
    user.user_information()