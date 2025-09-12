""" Display catch phrases from the Simpsons TV show"""


# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    '''
    Display the values from the dictionary parameter

    Parameters:
    dictionary (dict) : consists of character names and their catchphrases
    keys (list) : consists of character names

    Returns: no return value, only displays data
    '''
    for key in keys:
        # Changed k to key to correctly reference the key property from 
        # the for loop
        print(dictionary[key]) 


# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         # Added the escape character (\)
                         "homer": 'd\'oh!', 
                         "maggie": "(Pacifier Suck)"
                         }
# Converted second argument to a list to allow multiple string values 
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])  


'''
Expected console output:

BAAAAAART!
Eat My Shorts!
d'oh!
'''
