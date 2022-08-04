<h2>Lab: Graphs –Shortest Path and MST</h2>

This document defines the lab for[ "Algorithms with Python" course @Software University](https://softuni.bg/opencourses/algorithms-with-python)<span style="text-decoration:underline;">"</span>.

Please submit your solutions (source code) to all below-described problems in[ Judge](https://judge.softuni.org/Contests/3464).

1. **Shortest Path in Unweighted Graph \
   **

You will be given a graph from the console your task is to find the shortest path and print it back on the console. The first line will be the number of Nodes - **N** the second one the number of Edges - **E**, then on each **E **line the\*\* **edge in form** {destination} – {source}. \*\*On the last two lines, you will read the start node and the end node.

Print on the first line the **length** of the shortest path and the second the **path** **itself, **see the examples below.

<h4>**Example**</h4>

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
   <td>			8
<p>
			
<p>
10
<p>
			
<p>
1 			2
<p>
			
<p>
1 			4
<p>
			
<p>
2 			3
<p>
			
<p>
4 			5
<p>
			
<p>
5 			8
<p>
			
<p>
5 			6
<p>
			
<p>
5 			7
<p>
			
<p>
5 			8
<p>
			
<p>
6 			7
<p>
			
<p>
7 			8
<p>
			
<p>
1
<p>
			
<p>
7
<p>
		
   </td>
   <td>			Shortest path length is: 3
<p>
			
<p>
1 			4 5 7 			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
			
<p>
		
   </td>
  </tr>
  <tr>
   <td>			11
<p>
			
<p>
11
<p>
			
<p>
1 			5
<p>
			
<p>
1 			4
<p>
			
<p>
5 			7
<p>
			
<p>
7 			8
<p>
			
<p>
8 			2
<p>
			
<p>
2 			3
<p>
			
<p>
3 			4
<p>
			
<p>
4 			1
<p>
			
<p>
6 			2
<p>
			
<p>
9 			10
<p>
			
<p>
11 			9
<p>
			
<p>
6
<p>
			
<p>
3
<p>
		
   </td>
   <td>			Shortest path length is: 2
<p>
			
<ol>

<li>2 				3 \


<p>
		
</li>
</ol>
   </td>
  </tr>
</table>

1. **Dijkstra's Algorithm \
   **

Finding the **shortest path between two nodes** in an unweighted graph is done by applying simple BFS. When we’re working with weighted graphs though, things get more complicated. **Dijkstra’s algorithm** is one of the most famous ones that solve this task.

A classical application of the shortest path algorithm might be to find the shortest path between two towns on a map holding towns connected with roads where each road holds the distance between two towns.

In this problem, we’ll try to implement the optimized version of Dijkstra’s algorithm using a priority queue.

Example: Find the shortest path between **node 0** and **node 9** in the following weighted undirected graph:

<h4>**Input**</h4>

- On the first, you will receive an integer – **e** – number of edges. \
- On the next **e** lines, you will receive an edge in the following format: **"{start}, {end}, {weight}"**. \
- On the next line, you will receive a **start node**. \
- On the last line, you will receive an **end node**. \

<h4>**Output**</h4>

- Print the cost of the shortest path. \
- Print all nodes that form the shortest path. \
- If the end node can’t be reached from the start node, then you have to print: **"There is no such path." \
  **

<h4>**Example**</h4>

<table>
  <tr>
   <td>			<strong>Input</strong>
<p>
		
   </td>
   <td colspan="2" >			<strong>Output</strong>
<p>
		
   </td>
   <td>			<strong>Graph</strong>
<p>
		
   </td>
  </tr>
  <tr>
   <td>			18
<p>
			
<p>
0, 			6, 10
<p>
			
<p>
0, 			8, 12
<p>
			
<p>
6, 			4, 17
<p>
			
<p>
6, 			5, 6
<p>
			
<p>
8, 			5, 3
<p>
			
<p>
5, 			4, 5
<p>
			
<p>
5, 			11, 33
<p>
			
<p>
8, 			2, 14
<p>
			
<p>
2, 			11, 9
<p>
			
<p>
2, 			7, 15
<p>
			
<p>
4, 			1, 20
<p>
			
<p>
4, 			11, 11
<p>
			
<p>
11, 			1, 6
<p>
			
<p>
11, 			7, 20
<p>
			
<p>
1, 			9, 5
<p>
			
<p>
1, 			7, 26
<p>
			
<p>
7, 			9, 3
<p>
			
<p>
3, 			10, 7
<p>
			
<p>
0
<p>
			
<p>
9
<p>
		
   </td>
   <td>			42
<p>
			
<p>
0 8 5 4 			11 1 9
<p>
		
   </td>
   <td colspan="2" >			
<p>
		
   </td>
  </tr>
  <tr>
   <td>			18
<p>
			
<p>
0, 			6, 10
<p>
			
<p>
0, 			8, 12
<p>
			
<p>
6, 			4, 17
<p>
			
<p>
6, 			5, 6
<p>
			
<p>
8, 			5, 3
<p>
			
<p>
5, 			4, 5
<p>
			
<p>
5, 			11, 33
<p>
			
<p>
8, 			2, 14
<p>
			
<p>
2, 			11, 9
<p>
			
<p>
2, 			7, 15
<p>
			
<p>
4, 			1, 20
<p>
			
<p>
4, 			11, 11
<p>
			
<p>
11, 			1, 6
<p>
			
<p>
11, 			7, 20
<p>
			
<p>
1, 			9, 5
<p>
			
<p>
1, 			7, 26
<p>
			
<p>
7, 			9, 3
<p>
			
<p>
3, 			10, 7
<p>
			
<p>
0
<p>
			
<p>
10
<p>
		
   </td>
   <td>			There is no such path.
<p>
		
   </td>
   <td colspan="2" >			
<p>
		
   </td>
  </tr>
</table>

1.  \
    **Bellman-Ford \
    **

Find the **shortest** **path in a graph **and print it as a sequence** from S vertex to D vertex**.

Implement the Bellman-Ford algorithm.

<h4>**Input**</h4>

The input comes from the console.

- On the first line, you will receive an integer – **n** – the number of **nodes**. \
- On the next line, you will receive an integer – **e** – the number of edges. \
- On the next **e** lines, you will receive an edge in the following format:** "{from} {to} {weight}". ** \
- On the last two lines, you will receive **source** and **destination** nodes. \

<h4>**Output**</h4>

- Print **"Negative Cycle Detected" **if detect a negative cycle. \
- Otherwise, print the **shortest path** separated by a space and the total **distance**. \

<h4>**Example**</h4>

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
   <td>			6
<p>
			
<p>
8
<p>
			
<p>
1 			2 8
<p>
			
<p>
1 			3 10
<p>
			
<p>
2 			4 1
<p>
			
<p>
3 			6 2
<p>
			
<p>
4 			3 -4
<p>
			
<p>
4 			6 -1
<p>
			
<p>
6 			5 -2
<p>
			
<p>
5 			3 1
<p>
			
<p>
1
<p>
			
<p>
6
<p>
		
   </td>
   <td>			1 2 4 3 6
<p>
			
<p>
7
<p>
		
   </td>
  </tr>
  <tr>
   <td>			4
<p>
			
<p>
4
<p>
			
<p>
1 			2 1
<p>
			
<p>
2 			3 -1
<p>
			
<p>
3 			4 -1
<p>
			
<p>
4 			1 -1
<p>
			
<p>
1
<p>
			
<p>
4
<p>
		
   </td>
   <td>			Negative Cycle Detected
<p>
		
   </td>
  </tr>
</table>

1.  \
    **Kruskal’s Algorithm \
    **

If we have a weighted undirected graph, we can extract a sub-graph where all nodes (vertices) of the original graph are connected by edges without any cycles. This is referred to as a **spanning tree**. A **minimum spanning tree (MST)** is the spanning tree with the smallest weight (several MST could exist in some graphs).

For example, a cable operator wants to connect its customers to a **cable network**. The homes of the customers are connected by streets (edges) with different lengths (weights). To find out how to connect all homes to its network most efficiently (least distance covered) you need to find the **MST**.

One simple algorithm to find the MST of a given graph is[ Kruskal’s algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm).

<h4>**Input**</h4>

- On the first line you will receive **e** – an integer – number of edges that you have to read. \
- On the next **e** lines, you will receive an edge in the following format: **"{firstNode}, {seconNode}, {weight}"**. \

<h4>**Example**</h4>

<table>
  <tr>
   <td>			<strong>Input</strong>
<p>
		
   </td>
   <td>			<strong>Output</strong>
<p>
		
   </td>
   <td>			<strong>Details</strong>
<p>
		
   </td>
  </tr>
  <tr>
   <td>			11
<p>
			
<p>
0, 			3, 9
<p>
			
<p>
0, 			5, 4
<p>
			
<p>
0, 			8, 5
<p>
			
<p>
1, 			4, 8
<p>
			
<p>
1, 			7, 7
<p>
			
<p>
2, 			6, 12
<p>
			
<p>
3, 			5, 2
<p>
			
<p>
3, 			6, 8
<p>
			
<p>
3, 			8, 20
<p>
			
<p>
4, 			7, 10
<p>
			
<p>
6, 8, 7
<p>
		
   </td>
   <td>			3 - 5
<p>
			
<p>
0 			- 5
<p>
			
<p>
0 			- 8
<p>
			
<p>
1 			- 7
<p>
			
<p>
6 			- 8
<p>
			
<p>
1 			- 4
<p>
			
<p>
2 - 6
<p>
		
   </td>
   <td>			<strong>Graph:</strong>
<p>
			
<p>
			
<p>
<strong>MST:</strong>
<p>
			
<p>
		
   </td>
  </tr>
</table>

1.  \
    **Prim's Algorithm \
    **

If we have a weighted undirected graph, we can extract a sub-graph where all nodes (vertices) of the original graph are connected by edges without any cycles. This is referred to as a spanning tree. A minimum spanning tree (MST) is the spanning tree with the smallest weight (several MST could exist in some graphs).

For example, a cable operator wants to connect its customers to a cable network. The homes of the customers are connected by streets (edges) with different lengths (weights). To find out how to connect all homes to its network most efficiently (least distance covered) you need to find the MST.

One simple algorithm to find the MST of a given graph is Prim’s algorithm.

<h4>**Input**</h4>

- On the first line, you will receive **e** – an integer – number of edges that you have to read. \
- On the next **e** lines, you will receive an edge in the following format: **"{firstNode}, {seconNode}, {weight}"**. \

<h4>**Output**</h4>

- Print all edges part of the minimum spanning tree in the following format: **"{first} - {second}"**. \

- The order of the output **doesn’t matter**. \

<h4>**Example**</h4>

<table>
  <tr>
   <td>			<strong>Input</strong>
<p>
		
   </td>
   <td>			<strong>Output</strong>
<p>
		
   </td>
   <td>			<strong>Details</strong>
<p>
		
   </td>
  </tr>
  <tr>
   <td>			11
<p>
			
<p>
0, 			2, 5
<p>
			
<p>
2, 			4, 7
<p>
			
<p>
4, 			5, 12
<p>
			
<p>
0, 			1, 4
<p>
			
<p>
1, 			3, 2
<p>
			
<p>
0, 			3, 9
<p>
			
<p>
2, 			3, 20
<p>
			
<p>
3, 			4, 8
<p>
			
<p>
6, 			7, 8
<p>
			
<p>
6, 			8, 10
<p>
			
<p>
7, 8, 7
<p>
		
   </td>
   <td>			0 - 1
<p>
			
<p>
1 			- 3
<p>
			
<p>
0 			- 2
<p>
			
<p>
2 			- 4
<p>
			
<p>
4 			- 5
<p>
			
<p>
6 			- 7
<p>
			
<p>
7 - 8
<p>
		
   </td>
   <td>			<strong>Graph:</strong>
<p>
			
<p>
			
<p>
<strong>MST:</strong>
<p>
			
<p>
		
   </td>
  </tr>
</table>
