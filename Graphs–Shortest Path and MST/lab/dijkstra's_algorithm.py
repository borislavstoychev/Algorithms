from collections import deque
from queue import PriorityQueue

class Edge():
  def __init__(self, sorce, destination, weight) -> None:
    self.sorce = sorce
    self.destination = destination
    self.weight = weight

class Graph():
  
  def __init__(self, edges, graph, max_node, start, end) -> None:
    self.edges = edges
    self.graph = graph
    self.start = start
    self.end = end
    self.max_node = max_node
    self.distance = [float('inf')] * (self.max_node + 1)
    self.parent = [None] * (self.max_node + 1)
    self.path = deque()
    self.pq = PriorityQueue()

  def dijkstras(self):
    self.pq.put((0, self.start))
    while not self.pq.empty():
      min_distance, node = self.pq.get()
      if node == self.end:
        return
      for child in self.graph[node]:
        new_distance = min_distance + child.weight
        if new_distance < self.distance[child.destination]:
          self.distance[child.destination] = new_distance
          self.parent[child.destination] = node
          self.pq.put((new_distance, child.destination))

  def print_path(self):
    if self.distance[self.end] == float('inf'):
      print('There is no such path.')

    else:
      print(self.distance[self.end])
      node = self.end
      while node is not None:
        self.path.appendleft(node)
        node = self.parent[node]

      print(*self.path, sep=" ")


def main():
  edges = int(input())
  graph = {}
  for _ in range(edges):
      sorce, destination, weight = [int(n) for n in input().split(', ')]
      if sorce not in graph:
        graph[sorce] = []
      if destination not in graph:
        graph[destination] = []
      graph[sorce].append(Edge(sorce, destination, weight))
  start = int(input())
  end = int(input())
  max_node = max(graph.keys())
  solution = Graph(edges, graph, max_node, start, end)
  solution.dijkstras()
  solution.print_path()

if __name__ == "__main__":
  main()
