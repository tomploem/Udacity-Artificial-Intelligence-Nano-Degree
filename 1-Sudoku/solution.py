from util import *

assignments = []


def assign_value(values, box, value):
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def naked_twins(values):

    for unit in unitlist:
        possibilities = {coordinate: values[coordinate] for coordinate in unit if len(str(values[coordinate])) != 1}
        rev_possibilities = {}

        for key, value in possibilities.items():
            rev_possibilities.setdefault(value, set()).add(key)

        twin_keys = [key for key, values in rev_possibilities.items() if (len(values) > 1) & (len(key) == 2)]
        for twin_key in twin_keys:
            for key, value in possibilities.items():
                if twin_key != value:
                    for number in list(twin_key):
                        if number in value:
                            new_number = values[key].replace(number, '')
                            values = assign_value(values, key, new_number)

    return values
    pass

def grid_values(grid):
    elimenation = '123456789'
    values = [a for a in grid]
    dict = {}
    for index in range(len(values)):
        dict[boxes[index]] = elimenation if values[index] == '.' else values[index]
    return dict
    pass


def display(values):
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    pass


def eliminate(values):
    for key, value in values.items():
        if (len(value) == 1) & (value != '.'):
            for peer in peers[key]:
                values = assign_value(values, peer, values[peer].replace(value, ''))
    return values
    pass


def only_choice(values):
    for unit in unitlist:
        box = {}
        # create a dictionary of all coordinates with value in a unit
        box = {coordinate: values[coordinate] for coordinate in unit}
        already_assigned = ''.join([value for key, value in box.items() if len(str(box[key])) == 1])

        # delete all values which already has the right number
        box = {key: value for key, value in box.items() if len(str(box[key])) != 1}
        # create a string of all numbers that have that can be entered in a box
        possible_entries = ''.join([value for key, value in box.items()])
        # filter all numbers that only occur once
        numbers_with_one_occurence = [i for i in range(1, 10) if
                                      (possible_entries.count(str(i)) == 1) & (str(i) not in already_assigned)]
        # get the coordinates of the numbers with one occurence in sudoku grid
        values_with_only_choice = {key: digit for key, value in box.items() for digit in numbers_with_one_occurence if
                                   str(digit) in value}
        for k, v in values_with_only_choice.items():
                values = assign_value(values, k, str(v))

    return values
    pass


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = (solved_values_before == solved_values_after)
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False

    return values
    pass


def search(values):
    values = reduce_puzzle(values)

    if all(len(values[s]) == 1 for s in boxes):
        return values
    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    for value in values[s]:

        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)

        if attempt:
            return attempt

    pass


def solve(grid):
    values = grid_values(grid)
    values = search(values)
    return values


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments

        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
