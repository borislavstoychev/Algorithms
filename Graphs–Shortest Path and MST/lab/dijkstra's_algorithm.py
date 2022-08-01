from collections import deque
from queue import PriorityQueue

class Edge():
  def __init__(self, sorce, destination, weight) -> None:
    self.sorce = sorce
    self.destination = destination
    self.weight = weight

class DijkstraAlgorithm():
  
  def __init__(self, edges= int(input())) -> None:
    self.edges = edges
    self.graph = {}
    self.start = 0
    self.end = 0
    self.path = deque()
    self.pq = PriorityQueue()
  
  def create_graph(self):
    for _ in range(self.edges):
      sorce, destination, weight = list(map(int, input().split(', ')))
      if sorce not in self.graph:
        self.graph[sorce] = []
      if destination not in self.graph:
        self.graph[destination] = []
      self.graph[sorce].append(Edge(sorce, destination, weight))
    self.start = int(input())
    self.end = int(input())
    self.max_node = max(self.graph.keys())
    self.distance = [float('inf')] * (self.max_node + 1)
    self.parent = [None] * (self.max_node + 1)

  def shortest_path(self):
    self.pq.put((0, self.start))
    while not self.pq.empty():
      min_distance, node = self.pq.get()
      if node == self.end:
        break
      for child in self.graph[node]:
        new_distance = min_distance + child.weight
        if new_distance < self.distance[child.destination]:
          self.distance[child.destination] = new_distance
          self.parent[child.destination] = node
          self.pq.put((new_distance, child.destination))

  def show_path(self):
    if self.distance[self.end] == float('inf'):
      print('There is no such path.')

    else:
      print(self.distance[self.end])
      node = self.end
      while node is not None:
        self.path.appendleft(node)
        node = self.parent[node]

      print(*self.path, sep=" ")



solution = DijkstraAlgorithm()
solution.create_graph()
solution.shortest_path()
solution.show_path()
