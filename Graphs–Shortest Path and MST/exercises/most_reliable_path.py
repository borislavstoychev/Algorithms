from collections import deque
from queue import PriorityQueue

class Edge():
  def __init__(self, source, destination, weight) -> None:
    self.source = source
    self.destination = destination
    self.weight = weight

class Graph():
  
  def __init__(self, edges, graph, max_node, start, end) -> None:
    self.edges = edges
    self.graph = graph
    self.start = start
    self.end = end
    self.max_node = max_node
    self.distance = [float('-inf')] * (self.max_node)
    self.parent = [None] * (self.max_node)
    self.path = deque()
    self.pq = PriorityQueue()

  def dijkstras(self):
    self.pq.put((-100, self.start))
    self.distance[self.start] = 100
    while not self.pq.empty():
      max_distance, node = self.pq.get()
      if node == self.end:
        return
      for edge in self.graph[node]:
        child = edge.destination if edge.source == node else edge.source
        new_distance = -max_distance * edge.weight / 100
        if new_distance > self.distance[child]:
          self.distance[child] = new_distance
          self.parent[child] = node
          self.pq.put((-new_distance, child))

  def print_path(self):
    if self.distance[self.end] == float('-inf'):
      print('There is no such path.')

    else:
      print(f"Most reliable path reliability: {self.distance[self.end]:.2f}%")
      node = self.end
      while node is not None:
        self.path.appendleft(node)
        node = self.parent[node]

      print(*self.path, sep=" -> ")


def main():
  nodes = int(input())
  edges = int(input())
  graph = [[] for _ in range(nodes + 1)]
  for _ in range(edges):
      source, destination, weight = [int(n) for n in input().split()]
      graph[source].append(Edge(source, destination, weight))
      graph[destination].append(Edge(source, destination, weight))
  start = int(input())
  end = int(input())
  solution = Graph(edges, graph, nodes, start, end)
  solution.dijkstras()
  solution.print_path()

if __name__ == "__main__":
  main()
