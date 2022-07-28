<h2>Exercise: Graph Theory, Traversal and Topological Sorting</h2>

This document defines the exercise for[ "Algorithms with Python" course @Software University](https://softuni.bg/opencourses/algorithms-with-python)<span style="text-decoration:underline;">"</span>.

Please submit your solutions (source code) to all below-described problems in[ Judge](https://judge.softuni.org/Contests/3463/).

1. **Areas in Matrix \
   **

We are given a matrix of letters of size N \* M. Two cells are neighbors if they share a common wall. Write a program to find the connected areas of neighbor cells holding the same letter. Display the **total number of areas** and the number of **areas for each alphabetical letter** (ordered by alphabetical order).

On the **first line** is given the **number of rows**.

<h4>**Examples**</h4>

<table>
  <tr>
   <td>			<strong>Input</strong>
<p>
		
   </td>
   <td>			<strong>Picture</strong>
<p>
		
   </td>
   <td>			<strong>Output</strong>
<p>
		
   </td>
  </tr>
  <tr>
   <td>			6
<p>
			
<p>
			8
<p>
			
<p>
			aacccaac
<p>
			
<p>
			baaaaccc
<p>
			
<p>
			baabaccc
<p>
			
<p>
			bbdaaccc
<p>
			
<p>
			ccdccccc
<p>
			
<p>
ccdccccc
<p>
		
   </td>
   <td>			
<p>
		
   </td>
   <td>			Areas: 8
<p>
			
<p>
			Letter 'a' -> 			2
<p>
			
<p>
			Letter 'b' -> 			2
<p>
			
<p>
			Letter 'c' -> 			3
<p>
			
<p>
Letter 			'd' -> 1
<p>
		
   </td>
  </tr>
  <tr>
   <td>			3
<p>
			
<p>
			3
<p>
			
<p>
			aaa
<p>
			
<p>
			aaa
<p>
			
<p>
aaa
<p>
		
   </td>
   <td>			
<p>
		
   </td>
   <td>			Areas: 1
<p>
			
<p>
Letter 			'a' -> 1
<p>
		
   </td>
  </tr>
  <tr>
   <td>			5
<p>
			
<p>
			9
<p>
			
<p>
			asssaadas
<p>
			
<p>
			adsdasdad
<p>
			
<p>
			sdsdadsas
<p>
			
<p>
			sdasdsdsa
<p>
			
<p>
ssssasddd
<p>
		
   </td>
   <td>			
<p>
		
   </td>
   <td>			Areas: 21
<p>
			
<p>
			Letter 'a' -> 6 			
<p>
			
<p>
			Letter 'd' -> 7
<p>
			
<p>
Letter 			's' -> 8
<p>
		
   </td>
  </tr>
</table>

<h4>**Hint**</h4>

Initially mark all cells as **unvisited**. Start a **recursive DFS traversal** (or BFS) from each unvisited cell and mark all reached cells as visited. Each DFS traversal will find one of the **connected areas**.

1. **Cycles in a Graph \
   **

Write a program to check whether a directed graph is **acyclic** or holds any cycles. The input ends with "End" line.

<h4>**Examples**</h4>

<table>
  <tr>
   <td>			<strong>Input</strong>
<p>
		
   </td>
   <td>			<strong>Picture</strong>
<p>
		
   </td>
   <td>			<strong>Output</strong>
<p>
		
   </td>
  </tr>
  <tr>
   <td>			C-G
<p>
			
<p>
			End
<p>
			
<p>
			
<p>
		
   </td>
   <td>			
<p>
		
   </td>
   <td>			Acyclic: Yes
<p>
		
   </td>
  </tr>
  <tr>
   <td>			A-F
<p>
			
<p>
			F-D
<p>
			
<p>
			D-A
<p>
			
<p>
			End
<p>
			
<p>
			
<p>
		
   </td>
   <td>			
<p>
		
   </td>
   <td>			Acyclic: No
<p>
		
   </td>
  </tr>
  <tr>
   <td>			E-Q
<p>
			
<p>
			Q-P
<p>
			
<p>
			P-B
<p>
			
<p>
			End
<p>
			
<p>
			
<p>
		
   </td>
   <td>			
<p>
		
   </td>
   <td>			Acyclic: Yes
<p>
		
   </td>
  </tr>
  <tr>
   <td>			K-J
<p>
			
<p>
			J-N
<p>
			
<p>
			N-L
<p>
			
<p>
			N-M
<p>
			
<p>
			M-I
<p>
			
<p>
			End
<p>
			
<p>
			
<p>
		
   </td>
   <td>			
<p>
		
   </td>
   <td>			Acyclic: Yes
<p>
		
   </td>
  </tr>
</table>

1.  \
    **Salaries \
    **

We have a **hierarchy** between the employees in a company.

Employees can have one or several direct managers. People who **manage nobody** are called **regular employees** and their salaries are **1**. People who manage at least one employee are called **managers**. Each manager takes a **salary** which is equal to the **sum of the salaries of their directly managed employees**.

Managers cannot manage directly or indirectly themselves. Some employees might have no manager. See a sample hierarchy in a company along with the salaries computed following the above-described rule:

In the above example, employees 0 and 3 are regular employees and take salary 1. All others are managers and take the sum of the salaries of their directly managed employees. For example, manager 1 takes salary 3 + 2 + 1 = 6 (sum of the salaries of employees 2, 5 and 0). In the above example employees, 4 and 1 have no manager.

If we have **N** employees, they will be indexed from 0 to N – 1. For each employee, you will be given a string with N symbols. The symbols are either **'Y' or 'N'**, showing all employees that are managed by the current employee.

<h4>**Input**</h4>

-     On the first line, you will be given an integer N. \
-     On the next N lines, you will be given strings with N symbols 	(either 'Y' or 'N'). \
-     The input data will always be valid and in the format described. 	There is no need to check it explicitly. \

<h4>**Output**</h4>

-     Print the sum of the salaries of all employees. \

<h4>**Constraints**</h4>

-     N will be an integer in the range [1 … 50]. \
-     If employee A is the manager of employee B, B will not be a manager 	of A. \

<h4>**Examples**</h4>

<table>
  <tr>
   <td>			<strong>Input</strong>
<p>
		
   </td>
   <td>			<strong>Output</strong>
<p>
		
   </td>
   <td>			<strong>Comments</strong>
<p>
		
   </td>
  </tr>
  <tr>
   <td>			1
<p>
			
<p>
N
<p>
		
   </td>
   <td>			1
<p>
		
   </td>
   <td>			Only 			1 employee with salary 1.
<p>
		
   </td>
  </tr>
  <tr>
   <td>			4
<p>
			
<p>
NNYN
<p>
			
<p>
NNYN
<p>
			
<p>
NNNN
<p>
			
<p>
NYYN
<p>
		
   </td>
   <td>			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
5
<p>
		
   </td>
   <td>			We 			have 4 employees. 0, 1, and 3 are managers of 2. 3 is also a 			manager of 1. Therefore: 			
<p>
			
<p>
salary(2) 			= 1 			
<p>
			
<p>
salary(0) 			= salary(2) = 1
<p>
			
<p>
salary(1) 			= salary(2) = 1 			
<p>
			
<p>
salary(3) 			= salary(2) + salary(1) = 2
<p>
		
   </td>
  </tr>
  <tr>
   <td>			6
<p>
			
<p>
NNNNNN
<p>
			
<p>
YNYNNY
<p>
			
<p>
YNNNNY
<p>
			
<p>
NNNNNN
<p>
			
<p>
YNYNNN
<p>
			
<p>
YNNYNN
<p>
		
   </td>
   <td>			17
<p>
		
   </td>
   <td>			
<p>
		
   </td>
  </tr>
</table>

1. **Break Cycles \
   **

You are given an **undirected multi-graph**. Remove a minimal number of edges to **make the graph acyclic** (to break all cycles). As a result, print the number of edges removed and the removed edges. If several edges can be removed to break a certain cycle, remove the smallest of them in alphabetical order (smallest start vertex in alphabetical order and smallest end vertex in alphabetical order).

<h4>**Examples**</h4>

<table>
  <tr>
   <td>				<strong>Input</strong>
<p>
			
   </td>
   <td>				<strong>Picture</strong>
<p>
			
   </td>
   <td>				<strong>Output</strong>
<p>
			
   </td>
   <td>				<strong>Picture After Removal</strong>
<p>
			
   </td>
  </tr>
  <tr>
   <td>				8
<p>
				
<p>
1 				-> 2 5 4
<p>
				
<p>
2 				-> 1 3
<p>
				
<p>
3 				-> 2 5
<p>
				
<p>
4 				-> 1
<p>
				
<p>
5 				-> 1 3
<p>
				
<p>
6 				-> 7 8
<p>
				
<p>
7 				-> 6 8
<p>
				
<p>
8 -> 				6 7
<p>
			
   </td>
   <td>				
<p>
			
   </td>
   <td>				Edges to remove: 2
<p>
				
<p>
				1 				- 2
<p>
				
<p>
6 				- 7
<p>
			
   </td>
   <td>				
<p>
			
   </td>
  </tr>
  <tr>
   <td>				14
<p>
				
<p>
K 				-> X J
<p>
				
<p>
J 				-> K N
<p>
				
<p>
N 				-> J X L M
<p>
				
<p>
X 				-> K N Y
<p>
				
<p>
M 				-> N I
<p>
				
<p>
Y 				-> X L
<p>
				
<p>
L 				-> N I Y
<p>
				
<p>
I 				-> M L
<p>
				
<p>
A 				-> Z Z Z
<p>
				
<p>
Z 				-> A A A
<p>
				
<p>
F 				-> E B P
<p>
				
<p>
E 				-> F P
<p>
				
<p>
P 				-> B F E
<p>
				
<p>
B -> 				F P
<p>
			
   </td>
   <td>				
<p>
			
   </td>
   <td>				Edges to remove: 7
<p>
				
<p>
				A - Z
<p>
				
<p>
				A - Z
<p>
				
<p>
				B - F
<p>
				
<p>
				E - F
<p>
				
<p>
				I - L
<p>
				
<p>
				J - K
<p>
				
<p>
L 				- N
<p>
			
   </td>
   <td>				
<p>
			
   </td>
  </tr>
</table>

<h4>**Hint**</h4>

-     Enumerate edges {**source**, 	**destination**} in 	alphabetical order. For each edge {**source**, 	**destination**} check 	whether it closes a cycle. If yes - remove it. 	 \

  -     	To check whether an edge {**source**, 		**destination**} closes a 		cycle, temporarily remove the edge {**source**, 		**destination**} and then 		try to find a path from **source** 		to **destination** using DFS 		or BFS. \

1. **Road Reconstruction \
   **

Write a program that finds all the roads without which **buildings** in the city will become **unreachable**.

You will receive how many **buildings** the town has on the first line, then you will receive the number of **streets** and finally, for **each street,** you will receive which **buildings it connects**. Find all the streets that are important and **cannot be removed** and print them in ascending order (e. g. **3 0** should be printed as **0 3**).

<h4>**Input**</h4>

- On the first line, you will receive the **number** of **buildings**. \
- On the second line, you will receive the **amount** of the **streets** (**n**)**. \
  **
- On the next **"n"** lines you will receive which **buildings** each **street connects**. \

<h4>**Output**</h4>

- On the first line print: **"Important streets:"**. \
- On the next lines (if any) print the street in the format: **"{firstBuilding} {secondBuilding}"**. \
- The **order** of the output does **not matter** if you print all the important streets. \

<h4>**Examples**</h4>

<table>
  <tr>
   <td>			<strong>Input</strong>
<p>
		
   </td>
   <td>			<strong>Output</strong>
<p>
		
   </td>
  </tr>
  <tr>
   <td>			5
<p>
			
<p>
5
<p>
			
<p>
1 			- 0
<p>
			
<p>
0 			- 2
<p>
			
<p>
2 			- 1
<p>
			
<p>
0 			- 3
<p>
			
<p>
3 			- 4
<p>
			
<p>
			
<p>
		
   </td>
   <td>			Important streets:
<p>
			
<p>
0 			3
<p>
			
<p>
3 			4
<p>
			
<p>
		
   </td>
  </tr>
  <tr>
   <td>			7
<p>
			
<p>
8
<p>
			
<p>
0 			- 1
<p>
			
<p>
1 			- 2
<p>
			
<p>
2 			- 0
<p>
			
<p>
1 			- 3
<p>
			
<p>
1 			- 4
<p>
			
<p>
1 			- 6
<p>
			
<p>
3 			- 5
<p>
			
<p>
4 			- 5
<p>
		
   </td>
   <td>			Important streets:
<p>
			
<p>
1 			6
<p>
			
<p>
		
   </td>
  </tr>
</table>
