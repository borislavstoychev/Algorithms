# Lab: Recursion
This document defines the in-class exercises (lab) for the "Algortihms" course @ Software University.
You can check your solutions [here:](https://judge.softuni.bg/Contests/687/Recursion-Lab)
## Part I - Recursion
##    1. Recursive Array Sum - [Solution](https://github.com/borislavstoychev/Algorithms/blob/main/Recursion/array_sum.py)
Write a program that finds the sum of all elements in an integer array. Use recursion.
Note: In practice recursion should not be used here (instead use an iterative solution), this is just an exercise.
### Examples
Input  | Output
-------| ------
1 2 3 4  | 10
-1 0 1  | 0
### Hints
Write a recursive method. It will take as arguments the input array and the current index.

    • The method should return the current element + the sum of all next elements (obtained by recursively calling it).
    • The recursion should stop when there are no more elements in the array.
##    2. Recursive Factorial - [solution](https://github.com/borislavstoychev/Algorithms/blob/main/Recursion/factorial.py)
Write a program that finds the factorial of a given number. Use recursion.
#### Note: In practice recursion should not be used here (instead use an iterative solution), this is just an exercise.
### Examples
Input | Output
------ | -----
5  | 120
10  | 3628800
### Hints
Write a recursive method. It will take as arguments an integer number.

    • The method should return the current element * the result of calculating factorial of current element - 1 (obtained by recursively calling it).
    • The recursion should stop when there are no more elements in the array.

##    3. Recursive Drawing - [Solution](https://github.com/borislavstoychev/Algorithms/blob/main/Recursion/recursive_drawing.py)
Write a program that draws the figure below depending on n. Use recursion.
### Examples
Input  | Output
------ | ------
2 | ```**```<br>```*```<br>#<br>##
5 | ```*****```<br>```****```<br>```***```<br>```**```<br>```*```<br>#<br>##<br>###<br>####<br>#####
#### Hints
Set the bottom of the recursion

Define pre- and post- recursive behavior

##    4. Generating 0/1 Vectors - [Solution](https://github.com/borislavstoychev/Algorithms/blob/main/Recursion/generating_vectors.py)
Generate all n-bit vectors of zeroes and ones in lexicographic order.
### Examples
Input  | Output
-------| ------
3 | 000<br>001<br>010<br>011<br>100<br>101<br>110<br>111
5  | 00000<br>00001<br>00010<br>…<br>11110<br>11111
###  Hints
The method should receive as parameters the array which will be our vector and a current index

Bottom of recursion should be when the index is outside of the vector

To generate all combinations, create a for loop with a recursive call

##    5. Generating Combinations - [Solution](https://github.com/borislavstoychev/Algorithms/blob/main/Recursion/generating_combinations.py)
Generate all n choose k combinations. Read the set of elements, then number of elements to choose.
### Examples
Input  | Output
-------| ------
1 2 3 4 <br>2  | 1 2<br>1 3<br>1 4<br>2 3<br>2 4<br>3 4
1 2 3 4 5 <br>3  | 1 2 3<br>1 2 4<br>1 2 5<br>…<br>3 4 5
### Hints
The method should receive the following parameters

Set the bottom of the recursion

Loop through all possible picks for a given index of the vector

## Part II - 8 Queens Puzzle [Solution](https://github.com/borislavstoychev/Algorithms/blob/main/Recursion/queens_puzzle.py)
In this lab we will implement a recursive algorithm to solve the "8 Queens" puzzle. Our goal is to write a program to find all possible placements of 8 chess queens on a chessboard, so that no two queens can attack each other (on a row, column or diagonal).
#### Input
(no input)
#### Output
```
* - - - - - - - 
- - - - * - - - 
- - - - - - - * 
- - - - - * - - 
- - * - - - - - 
- - - - - - * - 
- * - - - - - - 
- - - * - - - - 

* - - - - - - - 
- - - - - * - - 
- - - - - - - * 
- - * - - - - - 
- - - - - - * - 
- - - * - - - - 
- * - - - - - - 
- - - - * - - -

…

(90 solutions more)
```
####    1. Learn about the "8 Queens" Puzzle
Learn about the "8 Queens" puzzle, e.g. from Wikipedia: http://en.wikipedia.org/wiki/Eight_queens_puzzle.
####    2. Define a Data Structure to Hold the Chessboard
First, let’s define a data structure to hold the chessboard. It should consist of 8 x 8 cells, each either occupied by a queen or empty. Let’s also define the size of the chessboard as a constant:

####    3. Define a Data Structure to Hold the Attacked Positions
We need to hold the attacked positions in some data structure. At any moment during the execution of the program, we need to know whether a certain position {row, col} is under attack by a queen or not.
There are many ways to store the attacked positions:

    • By keeping all currently placed queens and checking whether the new position conflicts with some of them.
    • By keeping an int[,] matrix of all attacked positions and checking the new position directly in it. This will be complex to maintain because the matrix should change many positions after each queen placement/removal.
    • By keeping sets of all attacked rows, columns and diagonals. Let’s try this idea:

The above definitions have the following assumptions:

    • The Rows are 8, numbered from 0 to 7.
    • The Columns are 8, numbered from 0 to 7.
    • The left diagonals are 15, numbered from -7 to 7. We can use the following formula to calculate the left diagonal number by row and column: leftDiag = col - row.
    • The right diagonals are 15, numbered from 0 to 14 by the formula: rightDiag = col + row.
Let’s take as an example the following chessboard with 8 queens placed on it at the following positions:
    • {0, 0}; {1, 6}; {2, 4}; {3, 7}; {4, 1}; {5, 3}; {6, 5}; {7, 2}

Following the definitions above for our example the queen {4, 1} occupies the row 4, column 1, left diagonal -3 and right diagonal 5.
####    4. Write the Backtracking Algorithm
Now, it is time to write the recursive backtracking algorithm for placing the 8 queens.
The algorithm starts from row 0 and tries to place a queen at some column at row 0. On success, it tries to place the next queen at row 1, then the next queen at row 2, etc. until the last row is passed. The code for putting the next queen at a certain row might look like this:

Initially, we invoke this method from row 0:

####    5. Check if a Position is Free
Now, let’s write the code to check whether a certain position is free. A position is free when it is not under attack by any other queen. This means that if some of the rows, columns or diagonals is already occupied by another queen, the position is occupied. Otherwise it is free. A sample code might look like this:

Recall that col-row is the number of the left diagonal and row+col is the number of the right diagonal.
####    6. Mark / Unmark Attacked Positions
After a queen is placed, we need to mark as occupied all rows, columns and diagonals that it can attack:

On removal of a queen, we will need a method to mark as free all rows, columns and diagonals that were attacked by it. Write it yourself:

####    7. Print Solutions
When a solution is found, it should be printed at the console. First, introduce a solutions counter to simplify checking whether the found solutions are correct:

Next, pass through all rows and through all columns at each row and print the chessboard cells:

####    8. Testing the Code
The "8 queens" puzzle has 92 distinct solutions. Check whether your code generates and prints all of them correctly. The solutionsFound counter will help you check the number of solutions. Below are the 92 distinct solutions:

Submit your code in judge, printing all 92 solutions, separated by a single line.
####    9. Optimize the Solution
Now we can optimize our code:

    • Remove the attackedRows set. It is not needed because all queens are placed consecutively at rows 0…7.
    • Try to use bool[] array for attackedColumns, attackedLeftDiagonals and attackedRightDiagonals instead of sets. Note that arrays are indexed from 0 to their size and cannot hold negative indexes.
***Permutation Based Solution***

Try to implement the more-efficient permutation-based solution of the "8 Queens" puzzle. Look at this code to grasp the [idea:](http://introcs.cs.princeton.edu/java/23recursion/Queens.java.html).

## Part III - Find All Paths in a Labyrinth - [Solution](https://github.com/borislavstoychev/Algorithms/blob/main/Recursion/labyrinth.py)
You are given a labyrinth. Your goal is to find all paths from the start (cell 0, 0) to the exit, marked with 'e'. 
   
    • Empty cells are marked with a dash '-'. 
    • Walls are marked with a star '*';
On the first line, you will receive the dimensions of the labyrinth. Next you will receive the actual labyrinth.
The order of the paths does not matter.
### Examples
Input  | Output
-------| ------
3 <br>3<br>```---```<br>```-*-```<br>```--e``` | RRDD<br>DDRR
3 <br>5 <br> ```-**-e```<br>```-----```<br>```*****``` | DRRRRU<br>DRRRUR
Hints
Create methods for reading and finding all paths in the labyrinth.

Create a static list that will hold every direction (basically the path)

Finding all paths should be recursive

Implement all helper methods that are present in the code above.