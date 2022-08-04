<h2>Exercise: Graphs Shortest Path and MST</h2>

This document defines the exercise for[ "Algorithms with Python" course @Software University](https://softuni.bg/opencourses/algorithms-with-python)<span style="text-decoration:underline;">"</span>.

Please submit your solutions (source code) to all below-described problems in[ Judge](https://judge.softuni.org/Contests/3465).

1. ### Distance Between Vertices

We are given a **directed graph**. We are given also a set of **pairs of vertices**. Find the **shortest distance between each pair** of vertices or **-1** if there is no path connecting them.

On the first line, you will get **N**, the number of vertices in the graph. On the second line, you will get P, the number of pairs between which to find the shortest distance.

On the next **N** lines will be the edges of the graph and on the next **P** lines, the pairs.

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
   <td>			2
<p>
			
<p>
			2
<p>
			
<p>
			1:2
<p>
			
<p>
			2:
<p>
			
<p>
			1-2
<p>
			
<p>
2-1
<p>
		
   </td>
   <td>			
<p>
		
   </td>
   <td>			{1, 2} -> 1
<p>
			
<p>
{2, 			1} -> -1
<p>
		
   </td>
  </tr>
  <tr>
   <td>			8
<p>
			
<p>
			4
<p>
			
<p>
			1:4
<p>
			
<p>
			2:4
<p>
			
<p>
			3:4 5
<p>
			
<p>
			4:6
<p>
			
<p>
			5:3 7 8
<p>
			
<p>
			6:
<p>
			
<p>
			7:8
<p>
			
<p>
			8:
<p>
			
<p>
			1-6
<p>
			
<p>
			1-5
<p>
			
<p>
			5-6
<p>
			
<p>
5-8
<p>
		
   </td>
   <td>			
<p>
		
   </td>
   <td>			{1, 6} -> 2
<p>
			
<p>
			{1, 5} -> -1
<p>
			
<p>
			{5, 6} -> 3
<p>
			
<p>
{5, 			8} -> 1
<p>
		
   </td>
  </tr>
  <tr>
   <td>			9
<p>
			
<p>
			8
<p>
			
<p>
			11:4
<p>
			
<p>
			4:12 			1
<p>
			
<p>
			1:12 			21 7
<p>
			
<p>
			7:21
<p>
			
<p>
			12:4 			19
<p>
			
<p>
			19:1 			21
<p>
			
<p>
			21:14 			31
<p>
			
<p>
			14:14
<p>
			
<p>
			31:
<p>
			
<p>
			11-7
<p>
			
<p>
			11-21
<p>
			
<p>
			21-4
<p>
			
<p>
			19-14
<p>
			
<p>
			1-4
<p>
			
<p>
			1-11
<p>
			
<p>
			31-21
<p>
			
<p>
11-14
<p>
		
   </td>
   <td>			
<p>
		
   </td>
   <td>			{11, 7} -> 3
<p>
			
<p>
			{11, 21} -> 3
<p>
			
<p>
			{21, 4} -> -1
<p>
			
<p>
			{19, 14} -> 2
<p>
			
<p>
			{1, 4} -> 2
<p>
			
<p>
			{1, 11} -> -1
<p>
			
<p>
			{31, 21} -> -1
<p>
			
<p>
{11, 			14} -> 4
<p>
		
   </td>
  </tr>
</table>

2.  ### Most Reliable Path

We have a set of **towns** and some of them are connected by **direct paths**. Each path has a coefficient of reliability (in percentage): the chance to pass without incidents.

Your goal is to compute the **most reliable path** between two given nodes. Assume all percentages will be integer numbers and round the result to the second digit after the decimal separator. For example, let's consider the graph below:

The **most reliable path** **between 0 and 6** is shown on the right: 0 **→** 4 **→** 5 **→** 3 **→** 1 **→** 6. Its cost = 88% _ 99% _ 98% _ 95% _ 100% = **81.11%**. The table below shows the optimal reliability coefficients for all paths starting from node 0:

<table>
  <tr>
   <td>			<strong>v</strong>
<p>
		
   </td>
   <td>			<strong>0</strong>
<p>
		
   </td>
   <td>			<strong>1</strong>
<p>
		
   </td>
   <td>			<strong>2</strong>
<p>
		
   </td>
   <td>			<strong>3</strong>
<p>
		
   </td>
   <td>			<strong>4</strong>
<p>
		
   </td>
   <td>			<strong>5</strong>
<p>
		
   </td>
   <td>			<strong>6</strong>
<p>
		
   </td>
  </tr>
  <tr>
   <td>			<strong>reliability[s → d]</strong>
<p>
		
   </td>
   <td>			100%
<p>
		
   </td>
   <td>			81.11%
<p>
		
   </td>
   <td>			77.05%
<p>
		
   </td>
   <td>			85.38%
<p>
		
   </td>
   <td>			88%
<p>
		
   </td>
   <td>			87.12%
<p>
		
   </td>
   <td>			81.11%
<p>
		
   </td>
  </tr>
</table>

<h4>**Input**</h4>

- On the first line, you will receive an integer – **n** – number of nodes. \
- On the second line, you will receive an integer – **e** – number of edges. \
- On the next **e** lines, you will receive edges in the following format: **"{first} {second} {weight}"**. \
- On the next line, you will receive an integer – **source** – starting of the path. \
- On the last line, you will receive an integer – **destination** – end of the path. \

<h4>**Output**</h4>

- First print **"** **Most reliable path reliability: {reliability}%"** on the console. \

  - **reliability** should be formatted to 2<sup>nd</sup> digit after the decimal point. \

-
- **Print the most reliable path in the following format:** **"{sourceNode} -> {node1} -> … -> {destination"}". \
  **

<h4>**Examples**</h4>

<table>
  <tr>
   <td>			<strong>Input</strong>
<p>
		
   </td>
   <td>			<strong>Output</strong>
<p>
		
   </td>
   <td>			<strong>Picture</strong>
<p>
		
   </td>
  </tr>
  <tr>
   <td>			7
<p>
			
<p>
10
<p>
			
<p>
0 			3 85
<p>
			
<p>
0 			4 88
<p>
			
<p>
3 			1 95
<p>
			
<p>
3 			5 98
<p>
			
<p>
4 			5 99
<p>
			
<p>
4 			2 14
<p>
			
<p>
5 			1 5
<p>
			
<p>
5 			6 90
<p>
			
<p>
1 			6 100
<p>
			
<p>
2 			6 95
<p>
			
<p>
0
<p>
			
<p>
6
<p>
		
   </td>
   <td>			Most reliable path reliability: 			81.11%
<p>
			
<p>
0 -> 			4 -> 5 -> 3 -> 1 -> 6
<p>
		
   </td>
   <td>			
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
0 			1 94
<p>
			
<p>
0 			2 97
<p>
			
<p>
2 			3 99
<p>
			
<p>
1 			3 98
<p>
			
<p>
0
<p>
			
<p>
1
<p>
		
   </td>
   <td>			Most reliable path reliability: 			94.11%
<p>
			
<p>
0 -> 			2 -> 3 -> 1
<p>
		
   </td>
   <td>			
<p>
		
   </td>
  </tr>
</table>

<h4>**Hints**</h4>

Modify Dijkstra's algorithm.

3. ### Cheap Town Tour

You now live in a new country and you want to start a tour and **visit every town** in the country and since you are new in the country your finances are **minimalized**, so you want your trip to be as **cheap** as possible.

You will be given the **amount** of the **cities** on the first line, then the amount of the **roads** (**n**), and on the next **n** lines you will receive which tows the road connects and the cost to use it.

Assume you can **start from any** town and your target is to **visit every one** of them with the **minimum **cost.

<h4>**Input**</h4>

- On the **first line,** you will be given the **number of** the **towns \
  **
- On the **second** line, you will be given the **number of streets** (**n**) \
- On the** next n** **lines,** you will be given a connection in the format: **"{first} - {second} - {cost}" \
  **

<h4>**Output**</h4>

- Print the **total cost** of the road you have chosen in the format: **"Total cost: {totalCost}" \
  **

<h4>**Examples**</h4>

<table>
  <tr>
   <td>			<strong>Input</strong>
<p>
		
   </td>
   <td>			<strong>Output</strong>
<p>
		
   </td>
   <td>			<strong>Comment</strong>
<p>
		
   </td>
  </tr>
  <tr>
   <td>			4
<p>
			
<p>
5
<p>
			
<p>
0 			- 1 - 10
<p>
			
<p>
0 			- 2 - 6
<p>
			
<p>
0 			- 3 - 5
<p>
			
<p>
1 			- 3 - 15
<p>
			
<p>
2 			- 3 - 4
<p>
		
   </td>
   <td>			Total cost: 19
<p>
			
<p>
			
<p>
		
   </td>
   <td>			
<p>
			
<p>
The 			cheapest way to visit all the towns is using the roads with a 			cost:
<p>
4 + 5 + 10 = 19
<p>
		
   </td>
  </tr>
</table>

4.  ### Undefined

Your **task** is to find the **shortest** **path in a graph from S vertex to D vertex**. However, edges might have **negative weights** and for this reason, you should be cautious for negative cycles.

<h4>**Input**</h4>

- On the first line, you will receive an integer – **n** – number of nodes. \
- On the second line, you will receive an integer – **e** – number of edges. \
- On the next **e** lines, you will receive edges in the following format: **"{source} {destination} {weight}". \
  **
- On the next line, you will receive an integer – **source** – the start of the path. \
- On the last line, you will receive an integer – **destination** – end of the path. \

<h4>**Output**</h4>

- If there is a negative cycle you should print **"Undefined". \
  **
- Otherwise, first, print on a single line the **path,** and after that, print the path** weight**. \

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
   <td>			5
<p>
			
<p>
8
<p>
			
<p>
1 			2 -1
<p>
			
<p>
1 			3 4
<p>
			
<p>
2 			3 3
<p>
			
<p>
2 			4 2
<p>
			
<p>
2 			5 2
<p>
			
<p>
4 			2 1
<p>
			
<p>
4 			3 5
<p>
			
<p>
5 			4 -3
<p>
			
<p>
1
<p>
			
<p>
4
<p>
		
   </td>
   <td>			1 2 5 4
<p>
			
<p>
-2
<p>
		
   </td>
  </tr>
  <tr>
   <td>			5
<p>
			
<p>
8
<p>
			
<p>
1 			2 -1
<p>
			
<p>
1 			3 4
<p>
			
<p>
2 			3 3
<p>
			
<p>
2 			4 2
<p>
			
<p>
2 			5 2
<p>
			
<p>
4 			2 -1
<p>
			
<p>
4 			3 5
<p>
			
<p>
5 			4 -3
<p>
			
<p>
1
<p>
			
<p>
4
<p>
		
   </td>
   <td>			Undefined
<p>
		
   </td>
  </tr>
</table>

5.  ### Cable Network

A cable networking company plans to extend its existing **cable network** by connecting as many customers as possible within a **fixed budget limit**. The company has calculated the **cost** of building some prospective connections.

You are given the existing cable network (a set of **customers** and **connections** between them) along with the **estimated connection costs** between some pairs of customers and prospective customers. A customer can only be connected to the network via a direct connection with an **already connected customer**.

Example:

In the above example, we have an existing cable network (the solid blue lines), the estimated costs for connecting some of the customers (dotted blue lines), and a budget limit of 20.

Within this budget, the company can connect 3 new customers by the following new connections (solid green lines): {3 → 5}, {8 → 7} and {7 → 1}. The total cost for those new connections will be 2 + 4 + 7 = 13, which fits in the budget limit of 20. No more customers can be connected within this budget limit.

**NOTE** that each edge, at the time of its addition to the network, **connects a new customer with an existing one**.

<h4>**Input**</h4>

- On the first line, you will receive an integer – budget. \
- On the second line, you will receive an integer – **n** – number of nodes. \
-     On the third line, you will receive an integer – **e** 	– number of edges. \
- On the next **e** lines, you will receive edges in the following format: **"{first} {second} {weight} {connected}"**. \

<h4>**Output**</h4>

- Print **"Budget used: {used_budget}"** on the console. \

<h4>**Examples**</h4>

<table>
  <tr>
   <td>			<strong>Input</strong>
<p>
		
   </td>
   <td>			<strong>Picture (Before)</strong>
<p>
		
   </td>
   <td>			<strong>Output</strong>
<p>
		
   </td>
   <td>			<strong>Picture (After)</strong>
<p>
		
   </td>
  </tr>
  <tr>
   <td>			20
<p>
			
<p>
9
<p>
			
<p>
15
<p>
			
<p>
1 			4 8
<p>
			
<p>
4 			0 6 connected
<p>
			
<p>
1 			7 7
<p>
			
<p>
4 			7 10
<p>
			
<p>
4 			8 3
<p>
			
<p>
7 			8 4
<p>
			
<p>
0 			8 5 connected
<p>
			
<p>
8 			6 9
<p>
			
<p>
8 			3 20 connected
<p>
			
<p>
0 			5 4
<p>
			
<p>
0 			3 9 connected
<p>
			
<p>
6 			3 8
<p>
			
<p>
6 			2 12
<p>
			
<p>
5 			3 2
<p>
			
<p>
3 2 14 			connected
<p>
		
   </td>
   <td>			
<p>
		
   </td>
   <td>			Budget used: 13
<p>
		
   </td>
   <td>			
<p>
		
   </td>
  </tr>
  <tr>
   <td>			7
<p>
			
<p>
4
<p>
			
<p>
5
<p>
			
<p>
0 			1 9
<p>
			
<p>
0 			3 4 connected
<p>
			
<p>
3 			1 6
<p>
			
<p>
3 			2 11 connected
<p>
			
<p>
1 2 5
<p>
		
   </td>
   <td>			
<p>
		
   </td>
   <td>			Budget used: 5
<p>
		
   </td>
   <td>			
<p>
		
   </td>
  </tr>
  <tr>
   <td>			20
<p>
			
<p>
8
<p>
			
<p>
16
<p>
			
<p>
0 			1 4
<p>
			
<p>
0 			2 5
<p>
			
<p>
0 			3 1 connected
<p>
			
<p>
1 			2 8
<p>
			
<p>
1 			3 2
<p>
			
<p>
2 			3 3
<p>
			
<p>
2 			4 16
<p>
			
<p>
2 			5 9
<p>
			
<p>
3 			4 7
<p>
			
<p>
3 			5 14
<p>
			
<p>
4 			5 12
<p>
			
<p>
4 			6 22
<p>
			
<p>
4 			7 9
<p>
			
<p>
5 			6 6
<p>
			
<p>
5 			7 18
<p>
			
<p>
6 7 15
<p>
		
   </td>
   <td>			
<p>
		
   </td>
   <td>			Budget used: 12
<p>
		
   </td>
   <td>			
<p>
		
   </td>
  </tr>
</table>

<h4>**Hints**</h4>

Modify Prims's algorithm. Until the budget is spent, connect the smallest possible edge from the connected node to the non-connected node.
