# Ather-FrontEnd-Developer-task

The 2048 game is developed using the Python3 programming language. The game starts with an empty grid having 2 values(2 or 4) in two different random
locations. The moves in the game Left(1), Right(2), Up(3) and Down(4) is taken as the user input and functions are made for the different kinds of 
moves possible. The game is successfully completed when the number 2048 appears in any cell after succesful merging of cells with same value along a line.
A new number(2 or 4) appears in a vacant cell after each move is performed. The user loses the game when there is no vacant spaces left in the grid.

The code has five functions:

ran_generator : It produces a random number(2 or 4) and assigns it in a random position which is not occupied by any other value.

key_1() : This function is used for performing the Left and Up(after transposing the grid) moves. The function adds same values along a line and shifts the
          values accordingly.
          
key_2() : This function is used for performing the Right and Down(after transposing the grid) moves. The function adds same values along a line and shifts 
          the values accordingly.
          
transposmat() : It finds the transpose of the grid, used for Up and Down moves.

printm() : It prints the elements in the grid in order. It also checks for the winning(2048 in a cell) and losing conditions(all cells occupied) and prints
           the appropriate message and ends the program.
          
The program can be easily transformed into an 8X8 grid game by simply changing the number of rows in the matrix, changing the limits of for loops, chaging
the random number generator function for more values and changing the the value of winning(eg : 2048 in 4X4), if required.

The winning value 2048 can be changed to 4096 by simply changing the value of variable w in the printm() function from 2048 to 4096.
