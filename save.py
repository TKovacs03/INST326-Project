
from datetime import date
import re
def new_save(fname, workout, user):
    '''create new .txt save file'''
    with open(f"{fname}.txt", "w") as f:
        f.write(f"user info: {user.name}, {user.age}, {user.height}, {user.weight}, {user.gender}, {user.level}\n")
        names = [exercise['name'] for exercise in workout]
        f.write(f"{date.today()}: {names}\n")

def add_save(fname, workout):
    '''add workout to existing save file'''
    with open(f"{fname}.txt", 'a') as f:
        names = [exercise['name'] for exercise in workout]
        f.write(f"{date.today()}: {names}\n")
        

def past_workouts(fname):
    with open(fname, 'r') as f:
        w_list = []
        for line in f:
            pass
        