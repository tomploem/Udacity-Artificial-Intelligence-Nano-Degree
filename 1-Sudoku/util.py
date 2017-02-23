rows = 'ABCDEFGHI'
cols = '123456789'

def is_diagonal_sudoku(values):

    lr = ''.join([values[key] for key in ['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9']])
    rl = ''.join([values[key] for key in ['A9', 'B8', 'C7', 'D6', 'E5', 'F4', 'G3', 'H2', 'I1']])

    if (len(lr) != 9) & (len(rl) != 9):
        return True

    count = {}
    for s in lr:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    for key in count:
        if count[key] > 2:
            return False

    count = {}
    for s in rl:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    for key in count:
        if count[key] > 1:
            return False



    return True
    pass


def cross(A, B):
    return [s + t for s in A for t in B]
    pass


boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
diagonal_units = [['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9'], ['A9', 'B8', 'C7', 'D6', 'E5', 'F4', 'G3', 'H2', 'I1']]

unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)
