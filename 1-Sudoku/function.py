from utils import *

def eliminate(values):
    for key, value in values.items():
        if len(value) == 1:
            for peer in peers[key]:
                values[peer] = values[peer].replace(value, '')

    return values
    pass


def only_choice(values):
    for unit in unitlist:
        box = {}
        # create a dictionary of all coordinates with value in a unit
        box = { coordinate: values[coordinate] for coordinate in unit }
        already_assigned = ''.join([value for key, value in box.items() if len(str(box[key])) == 1])

        # delete all values which already has the right number
        box = {key: value for key, value in box.items() if len(str(box[key])) != 1}
        # create a string of all numbers that have that can be entered in a box
        possible_entries = ''.join([value for key, value in box.items()])
        # filter all numbers that only occur once
        numbers_with_one_occurence = [i for i in range(1, 10) if (possible_entries.count(str(i)) == 1) & (str(i) not in already_assigned)]
        # get the coordinates of the numbers with one occurence in sudoku grid
        values_with_only_choice = {key: digit for key, value in box.items() for digit in numbers_with_one_occurence if
                                    str(digit) in value}
        for k, v in values_with_only_choice.items():
            values[k] = str(v)

    return values
    pass

el = eliminate(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..') )
print(' ')
display(el)
grid = only_choice(el)

display(grid)
