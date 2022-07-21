# Lab: Graph Theory, Traversal, and Topological Sorting

**This document defines the lab for[ "Algorithms with Python" course @Software University](https://softuni.bg/opencourses/algorithms-with-python)<span style="text-decoration:underline;">"</span>.**

**Please submit your solutions (source code) of all below-described problems in[ Judge](https://judge.softuni.org/Contests/3462).**



## Connected Components 
**The first part of this lab aims to implement the DFS algorithm (Depth-First-Search) to traverse a graph and find its connected components (nodes connected either directly, or through other nodes). The graph nodes are numbered from 0 to n-1. The graph comes from the console in the following format:**



* **First line: 	number of lines n \
 	**
* **Next n 	lines: list of child nodes for the nodes 0 	… n-1 (separated by a 	space) \
**

**Print the connected components in the same format as in the examples below.**


### Example


<table>
  <tr>
   <td><strong>			Input</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Graph</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Output</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
  <tr>
   <td><strong>			9</strong>
<p>
<strong>			</strong>
<p>
<strong>3 			6</strong>
<p>
<strong>			</strong>
<p>
<strong>3 			4 5 6</strong>
<p>
<strong>			</strong>
<p>
<strong>8</strong>
<p>
<strong>			</strong>
<p>
<strong>0 			1 5</strong>
<p>
<strong>			</strong>
<p>
<strong>1 			6</strong>
<p>
<strong>			</strong>
<p>
<strong>1 			3</strong>
<p>
<strong>			</strong>
<p>
<strong>0 			1 4</strong>
<p>
<strong>			</strong>
<p>
<strong>			</strong>
<p>
<strong>			</strong>
<p>
<strong>2</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Connected component: 6 4 5 1 3 0</strong>
<p>
<strong>			</strong>
<p>
<strong>Connected 			component: 8 2</strong>
<p>
<strong>			</strong>
<p>
<strong>			Connected component: 7</strong>
<p>
<strong>			</strong>
<p>
<strong>			</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
  <tr>
   <td><strong>			0</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			(empty graph)</strong>
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



### Hints


#### **Read Input**

**Let's implement the data entry logic (read the graph from the console):**


#### **DFS Algorithm**

**First, create a bool array that will be with the size of your graph:**

**Next, implement the DFS algorithm (Depth-First-Search) to traverse all nodes connected to the specified start node:**


#### **Find All Components**

**We want to find all connected components. We can just run the DFS algorithm for each node taken as a start (which was not visited already):**


#### **Test**

**Now let's test the above code. The output is as expected. It prints all connected components in the graph:**


## Source Removal Topological 	Sorting 
**We’re given a directed graph which means that if node A is connected to node B and the vertex is directed from A to B, we can move from A to B, but not the other way around, i.e. we have a one-way street. We’ll call A "source" or "predecessor" and B – "child".**

**Let’s consider the tasks a SoftUni student needs to perform during an exam – "Read description", "Receive input", "Print output", etc.**

**Some of the tasks depend on other tasks – we cannot print the output of a problem before we get the input. If all such tasks are nodes in a graph, a directed vertex will represent dependency between two tasks, e.g. if A -> B (A is connected to B and the direction is from A to B), this means B cannot be performed before completing A first. Having all tasks as nodes and the relationships between them as vertices, we can order the tasks using topological sorting.**

**After the sorting procedure, we’ll obtain a list showing all tasks in the order in which they should be performed. Of course, there may be more than one such order, and there usually is, but in general, the tasks which are less dependent on other tasks will appear first in the resulting list.**

**For this problem, you need to implement topological sorting over a directed graph of strings.**


### Input



* **On the 	first line, you will receive an integer n 	–nodes count. \
 	**
* **On the next n 	lines, you will receive nodes in the following format: "{key} 	-> {children1}, {children2},… {childrenN}". \
 	**
    * **It is possible some of the 		keys to not having any children. \
 	**


### Output



* **If the 	sorting is possible then print "Topological 	sorting: {sortedKey1}, {sortedKey2}, …{sortedKeyN}". \
 	**
* **Otherwise, 	print "Invalid topological 	sorting". \
**


### Example


<table>
  <tr>
   <td><strong>			Input</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Picture</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Output</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
  <tr>
   <td><strong>			6</strong>
<p>
<strong>			</strong>
<p>
<strong>			A -> B, C</strong>
<p>
<strong>			</strong>
<p>
<strong>			B -> E, D</strong>
<p>
<strong>			</strong>
<p>
<strong>			C -> F</strong>
<p>
<strong>			</strong>
<p>
<strong>			D -> C, F</strong>
<p>
<strong>			</strong>
<p>
<strong>			E -> D</strong>
<p>
<strong>			</strong>
<p>
<strong>F -></strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Topological sorting: A, B, E, D, C, F</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
  <tr>
   <td><strong>			5</strong>
<p>
<strong>			</strong>
<p>
<strong>IDEs 			-> variables, loops</strong>
<p>
<strong>			</strong>
<p>
<strong>variables 			-> conditionals, loops, bits</strong>
<p>
<strong>			</strong>
<p>
<strong>conditionals 			-> loops</strong>
<p>
<strong>			</strong>
<p>
<strong>loops 			-> bits</strong>
<p>
<strong>			</strong>
<p>
<strong>bits -></strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Topological sorting: IDEs, variables, 			conditionals, loops, bits</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
  <tr>
   <td><strong>			2</strong>
<p>
<strong>			</strong>
<p>
<strong>A 			-> B</strong>
<p>
<strong>			</strong>
<p>
<strong>B -> 			A</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			</strong>
<p>
<strong>		</strong>
   </td>
   <td><strong>			Invalid topological sorting</strong>
<p>
<strong>		</strong>
   </td>
  </tr>
</table>


**We’ll solve this using two different algorithms – source removal and DFS.**


### Source Removal Algorithm

**The source removal algorithm is pretty simple – it finds the node which isn’t dependent on any other node and removes it along with all vertices connected to it.**

**We continue removing each node recursively until we’re done and all nodes have been removed. If there are nodes in the graph after the algorithm is complete, there are circular dependencies (we will throw an exception).**


#### **Compute Predecessors**

**To efficiently remove a node at each step, we need to know the number of predecessors for each node. To do this, we will calculate the number of predecessors beforehand.**

**Compute the predecessor count for each node:**


#### **Remove Independent Nodes**

**Now that we know how many predecessors each node has, we just need to:**



1. **Find a node without 	predecessors and remove it 	 \
 	**
2. **Repeat until we’re done \
**

**We’ll keep the result in a list and start a loop that will stop when there is no independent node:**

**Finding a source can be done by a custom function.**

**We just need to check if such a node exists; if not, we break the loop:**

**Removing a node involves several steps:**



1. **All its child 	nodes lose a predecessor -> decrement the count of predecessors 	for each of the children \
 	**
2. **Remove the node 	from the predecessor dictionary \
 	**
3. **Add the node to 	the list of removed nodes \
**

**Finally, print the sorted nodes.**


#### **Detect Cycles**

### If we ended the loop and the predecessor_count still has nodes, this means there is a cycle. Just add a check after the while loop and print the proper message if the predecessor_count is not empty:


### DFS Topological Sorting


#### **DFS Algorithm**

**The second algorithm we’ll use is DFS. For this one, we’ll need the following collections:**

**The DFS topological sort is simple – loop through each node. We create a deque for all sorted nodes because the DFS will find them in reverse order (we will add nodes in the beginning):**

**The DFS method shouldn’t do anything if the node is already visited; otherwise, it should mark the node as visited and add it to the list of sorted nodes. It should also do this for its children (if there are any):**

**Note that we add the node to the result after we traverse its children. This guarantees that the node will be added after the nodes that depend on it.**


#### **Add Cycle Detection**

**How do we know if a node forms a cycle? We can add it to a list of cycle nodes before traversing its children. If we enter a node with the same value, it will be in the cycles collection, so we throw an exception. If there are no descendants with the same value then there are no cycles, so once we finish traversing the children, we remove the current node from cycles.**

**Exiting the method with an exception is easy, just check if the current node is in the list of cycle nodes at the very beginning of the DFS method then, keep track of the cycle nodes:**
