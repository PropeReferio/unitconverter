import json

with open('conversions.json', 'r') as f:
    datastore = json.load(f)  #something about closing files after you're 
    #done... does "with" autoclose?

print(datastore)

def convert(original: str, converted: str, n: int) -> int:
    '''Takes as arguments the unit to convert from (original), the amount of 
    that unit (n), and the unit to convert to (converted), and outputs the 
    amount of that final unit.'''
    # I think I need graph theory, to go from foot to centimeter, for example.
    # Multiply when going from index 0 to 1, Divide when going from 1 to 0.
    # Maybe I should convert this into 1 or more dictionaries? I.e.,
    'footinch': 12,
    'inchfoot': 0.0833333,
    #By using a dictionary, I don't have to loop over the list like a fool
    #every time I run the program, looping multiple times to get convert 
    #between units with no direct link in the json.
    #Doing it this way would require making every possible unit conversion,
    #however, i.e. 'footcentimeter', 'yearsecond'. This could take a lot of
    #time. But would I really have to do it that way? Or could I combine this
    #string concatenation with an adjacency list of some sort so that the
    #program understands automatically to convert first to inches, and then to
    #centimeters?
    #If I make a cache of every single possible unit conversion and save that
    #as a cache just one time, that dictionary would be available to all users
    #of the program forever. Will W20 accept this method?

    #To use this, you would concatenate original and converted, and then simply
    #use that as a key in said dictionary, get the value (an int/float), and
    #multiply it by n. That would be the output.

    #Step 1: Make the program work as you always have.
    #Step 2: Create a CLI which passes arguments to your function. Consider
    #Making a very simple CLI with simple function first to make learning
    #easy.

