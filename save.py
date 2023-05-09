
from datetime import date
import re
def new_save(fname, workout):
    '''create new .txt save file and writes workout information
        
        Args:
        fname(str): name of user
        workout(list of str): names of exercises performed
        
        Side Effects:
        creates new .txt file named after user, writes to file
            '''
    with open(f"{fname}.txt", "w") as f:
        names = [exercise['name'] for exercise in workout]
        f.write(f"Date:{date.today()} Exercises: {names}\n")

def add_save(fname, workout):
    '''adds workout to existing save file.
    
        Args:
            fname(str): name of user
            workout(list of str): names of exercises performed
        
        Side Effects:
            writes exercises to file
    '''
    with open(f"{fname}.txt", 'a') as f:
        names = [exercise['name'] for exercise in workout]
        f.write(f"{date.today()}: {names}\n")
        

def past_workouts(fname, spec_day = None):
    '''retrieves workout information from text file.
    
        Args:
            fname(str): name of user
            spec_day(str): optional, date in YYYY-MM-DD format
    
        Side Effects:

    '''
    with open(f"{fname}.txt", 'r') as f:
        for line in f:
            if spec_day:
                if re.search(fr"{spec_day}", line):
                    print(line)
                else:
                    raise ValueError('No such date in save file')
            else:
                print(line)
            
                
                