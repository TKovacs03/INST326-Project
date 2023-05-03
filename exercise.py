'''Reads csv file info'''
exercise_list = []
def file_reader(file):
    '''
    TJ Kovacs
    Create a list of dictionaries of exercises from a csv file, format:
    name; maleweight; femaleweight; setsxreps; workout type; description
    
    for use in workout generation. 
    
    args: 
    file(str): name of csv file
    
    returns:
        exercise_list(list of dict): a list of dictionaries.
    
    '''
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            e_dict = {}
            l = line.split(';')
            e_dict['name'] = l[0]
            e_dict['m'] = l[1]
            e_dict['f'] = l[2]
            e_dict['rep'] = l[3]
            e_dict['group'] = l[4]    
            e_dict['desc'] = l[5]        
            exercise_list.append(e_dict)
    return exercise_list
            

            
            