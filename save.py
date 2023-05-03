
from datetime import date
import re
def new_save(fname, workout, user):
    '''create new .txt save file'''
    with open(f"{fname}.txt", "w") as f:
        f.write(f"user info: {user.name}, {user.age}, {user.height}, {user.weight}, {user.gender}, {user.level}\n")
        names = [exercise['name'] for exercise in workout]
        f.write(f"Date:{date.today()} Exercises: {names}\n")

def add_save(fname, workout):
    '''add workout to existing save file'''
    with open(f"{fname}.txt", 'a') as f:
        names = [exercise['name'] for exercise in workout]
        f.write(f"{date.today()}: {names}\n")
        

def past_workouts(fname, spec_day = None):
    with open(fname, 'r') as f:
        for line in f:
            if spec_day:
                if re.search(fr"{spec_day}"):
                    print(line)
                else:
                    raise ValueError('No such date in save file')
            if line.startswith('Date:'):
                print(line)
            
                
                