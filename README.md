# Minesweeper
The objective was to implement an algorithm that verfies the solution to a puzzle that was NP-complete. 
I.e., create a puzzle that can be verified easily but is difficult to solve.    

## TO RUN GAME:

pip install random
pip install time


## GAMEPLAY:

Enter A Coordinate For The Row
Enter A Coordinate For The Column

## RULES:

- A player selects a square on an 8x8 grid with 10 mines randomly scattered throughout the grid.
- The squares have two states – uncovered or covered.
- The covered squares are blank and selectable.
- The uncovered squares are exposed and not selectable.
- If a player selects an covered square and it exposes itself as a mine,
  the game is over and the player loses.
- If a player selects an covered square and it is NOT a mine, the square will reveal a
  number between 0 and 4. The number indicates the number of mines adjacent to the selected square.
- A player wins the game when the only covered squares left are mines. (There are 10 mines
  total, so there will only be 10 covered squares left - or m mines if amount is changed.)
- The player earns one point for every turn without hitting a mine but the main objective is to
  solve the puzzle in the shortest amount of time possible.
