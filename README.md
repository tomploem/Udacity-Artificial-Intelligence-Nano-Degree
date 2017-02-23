# Projects of the Artificial Intellingence ND

# Sudoku

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: The naked twins problem is where 2 boxes in a associated unit have the same possible values. For example if A1 and A3 have can hold the values 2 & 3: we now can ensure that every other box in the associated unit where 2 or 3 is possible can be deleted. 2 boxes with only 2 possible values ensures that there will be no other possible place for 2 and 3.



# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: In every strategy (search, eliminate, only choice) to solve a sudoku, i use unitlists. For example: the row unit for A1 is ['A1','A2','A3','A4','A5','A6','A7','A8','A9']. We can also create a unit for column and a box. In a Diagonal sudoku, there is also a diagonal unit. This ensures the diagonal from left to right has also a combination of 1 through 9. By simply adding the diagonal unit to the lists of units we check for diagonal formats.



