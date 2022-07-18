# Exercise: Recursion and Combinatorial Problems

**This document defines the lab for[ "Algorithms with Python" course @Software University](https://softuni.bg/opencourses/algorithms-with-python)<span style="text-decoration:underline;">"</span>.**

**Please submit your solutions (source code) of all below-described problems in[ Judge](https://judge.softuni.org/Contests/3460).**

## Reverse Array

**Write a program that reverses and prints an array. Use recursion.**

### Examples

<table>
  <tr>
   <td><strong>			Input</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Output</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
  <tr>
   <td><strong>			1 2 3 4 5 6</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			6 5 4 3 2 1</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
</table>

## Nested Loops To Recursion

**Write a program that simulates the execution of n nested loops from 1 to n which prints the values of all its iteration variables at any given time on a single line. Use recursion.**

### Examples

<table>
  <tr>
   <td><strong>			Input</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Output</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
  <tr>
   <td><strong>			2</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			1 1</strong>
<p>
<strong>			</strong>
<p>
<strong>			1 2</strong>
<p>
<strong>			</strong>
<p>
<strong>			2 1</strong>
<p>
<strong>			</strong>
<p>
<strong>2 			2</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
  <tr>
   <td><strong>			3</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			1 1 1</strong>
<p>
<strong>1 1 2</strong>
<p>
<strong>			</strong>
<p>
<strong>			1 1 3</strong>
<p>
<strong>			</strong>
<p>
<strong>			1 2 1</strong>
<p>
<strong>			</strong>
<p>
<strong>			1 2 2</strong>
<p>
<strong>			</strong>
<p>
<strong>			…</strong>
<p>
<strong>			</strong>
<p>
<strong>			3 2 3</strong>
<p>
<strong>			</strong>
<p>
<strong>			3 3 1</strong>
<p>
<strong>			</strong>
<p>
<strong>			3 3 2</strong>
<p>
<strong>			</strong>
<p>
<strong>3 			3 3</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
</table>

## Move Down / Right

**Marinette has the ability to transform into Ladybug. She is stuck on a grid. Her initial location is at the top-left corner and tries to move to the bottom-right corner. However, she can only move either down or right at any point in time.**

**Write a program that prints the number of all possible unique paths that Marinette can take to reach the bottom-right corner.**

### Input

- **On the first line you will receive an integer – m – number of rows. \
  **
- **On the second line you will receive an integer – n – number of cols. \
  **

### Output

- **Print the number of all possible unique paths to the bottom-right corner. \
  **

### Constraints

- **m and n will always be in the range [0… 1000]. \
  **

### Examples

<table>
  <tr>
   <td><strong>			Input</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Output</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Comments</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
  <tr>
   <td><strong>			3</strong>
<p>
<strong>			</strong>
<p>
<strong>2</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			3</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			All possible 			unique paths:</strong>
<p>
<strong>			</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
  <tr>
   <td><strong>			3</strong>
<p>
<strong>			</strong>
<p>
<strong>5</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			15</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			</strong>
<p>
<strong>			</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
</table>

## Connected Areas in a Matrix

**Let’s define a connected area in a matrix as an area of cells in which there is a path between every two cells.**

**Write a program to find all connected areas in a matrix.**

### Input

- ** On the first line, you will get the number of rows. \
  **
- ** On the second line, you will get the number of columns. \
  **
- ** The rest of the input will be the actual matrix. \
  **

### Output

- ** Print on the console the total number of areas found. \
  **
- ** On a separate line for each area print its starting coordinates and size. \
  **
- ** Order the areas by size (in descending order) so that the largest area is printed first. \
  **
  - ** If several areas have the same size, order them by their position, first by the row, then by the column of the top-left corner. \
    **
  - ** If there are two connected areas of the same size, the one which is above and/or to the left of the other will be printed first. \
    **

### Examples

<table>
  <tr>
   <td><strong>			Example Layout</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Output</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
  <tr>
   <td><strong>			4</strong>
<p>
<strong>			</strong>
<p>
<strong>9</strong>
<p>
<strong>			</strong>
<p>
<strong>---*---*-</strong>
<p>
<strong>			</strong>
<p>
<strong>---*---*-</strong>
<p>
<strong>			</strong>
<p>
<strong>---*---*-</strong>
<p>
<strong>			</strong>
<p>
<strong>----*-*--</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Total areas found: 3</strong>
<p>
<strong>			</strong>
<p>
<strong>			Area #1 at (0, 0), size: 13</strong>
<p>
<strong>			</strong>
<p>
<strong>			Area #2 at (0, 4), size: 10</strong>
<p>
<strong>			</strong>
<p>
<strong>Area 			#3 at (0, 8), size: 5</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
  <tr>
   <td><strong>			5</strong>
<p>
<strong>			</strong>
<p>
<strong>10</strong>
<p>
<strong>			</strong>
<p>
<strong>*--*---*--</strong>
<p>
<strong>			</strong>
<p>
<strong>*--*---*--</strong>
<p>
<strong>			</strong>
<p>
<strong>*--*****--</strong>
<p>
<strong>			</strong>
<p>
<strong>*--*---*--</strong>
<p>
<strong>			</strong>
<p>
<strong>*--*---*--</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Total areas found: 4</strong>
<p>
<strong>			</strong>
<p>
<strong>			Area #1 at (0, 1), size: 10</strong>
<p>
<strong>			</strong>
<p>
<strong>			Area #2 at (0, 8), size: 10</strong>
<p>
<strong>			</strong>
<p>
<strong>			Area #3 at (0, 4), size: 6</strong>
<p>
<strong>			</strong>
<p>
<strong>Area 			#4 at (3, 4), size: 6</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
</table>

### Hints

- **Create a method to find the first traversable cell which hasn’t been visited. This would be the top-left corner of a connected area. If there is no such cell, this means all areas have been found. \
  **
- \*\*You can create a class to hold info about a connected area (its position and size). Additionally, you can implement Comparable and store all areas found in a TreeSet. \

## Word Cruncher

**Write a program that receives some strings and forms another string that is required. On the first line, you will be given all of the strings separated by comma and space. On the next line, you will be given the string that needs to be formed from the given strings. For more clarification see the examples below.**

### Input

- **On the first line, you will receive the strings (separated by comma and space ", ") \
  **
- **On the next line, you will receive the target string \
  **

### Output

- **Print each of them found ways to form the required string as shown in the examples \
  **

### Constrains

- **There might be repeating elements in the input \
  **

### Examples

<table>
  <tr>
   <td><strong>			Input</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Output</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
  <tr>
   <td><strong>			text, 			me, 			so, 			do, 			m, 			ran</strong>
<p>
<strong>			</strong>
<p>
<strong>somerandomtext</strong>
<p>
<strong>			</strong>
<p>
<strong>			</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			so 			me 			ran 			do 			m 			text</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
  <tr>
   <td><strong>			Word, cruncher, 			cr, h, unch, c, r, un, ch, er</strong>
<p>
<strong>			</strong>
<p>
<strong>Wordcruncher</strong>
<p>
<strong>			</strong>
<p>
<strong>			</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Word c r un ch er</strong>
<p>
<strong>			</strong>
<p>
<strong>Word 			c r unch er</strong>
<p>
<strong>			</strong>
<p>
<strong>Word 			cr un c h er</strong>
<p>
<strong>			</strong>
<p>
<strong>Word 			cr un ch er</strong>
<p>
<strong>			</strong>
<p>
<strong>Word 			cr unch er</strong>
<p>
<strong>			</strong>
<p>
<strong>Word 			cruncher</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
  <tr>
   <td><strong>			tu, stu, p, i, d, 			pi, pid, s, pi</strong>
<p>
<strong>			</strong>
<p>
<strong>stupid</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			s tu p i d</strong>
<p>
<strong>			</strong>
<p>
<strong>s 			tu pi d</strong>
<p>
<strong>			</strong>
<p>
<strong>s 			tu pid</strong>
<p>
<strong>			</strong>
<p>
<strong>stu 			p i d</strong>
<p>
<strong>			</strong>
<p>
<strong>stu 			pi d</strong>
<p>
<strong>			</strong>
<p>
<strong>stu 			pid</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
</table>
