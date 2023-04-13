'''
Contains exercise function, which reads information from a csv of the following format:
name, male beginner weight, female beginner weight, rep range, muscle group, description
and creates a list of dictionaries containing every exercise and their attributes. 
'''
exercise_list = []
def file_reader(file):
    with open(file, 'r', encoding="UTF8") as f:
        for line in f:
            e_dict = {}
            l = line.split(',')
            e_dict['name'] = l[0]
            e_dict['mweight'] = l[1]
            e_dict['fweight'] = l[2]
            e_dict['rep'] = l[3]
            e_dict['group'] = l[4]    
            e_dict['desc'] = l[5]        
            exercise_list.append(e_dict)
            
file_reader('sample_exercise_data.csv')
print(exercise_list)
            
            
            