from collections import deque
from queue import PriorityQueue

class Edge():
  def __init__(self, first, second, weight) -> None:
    self.first = first
    self.second = second
    self.weight = weight

  def __gt__(self, other):
    return self.weight > other.weight

class Graph():
  
  def __init__(self, edges, graph) -> None:
    self.edges = edges
    self.graph = graph
    self.forest = set()
    self.forest_edges = []
    self.path = deque()
    self.pq = PriorityQueue()

  def prim(self, node):
    self.forest.add(node)
    for edge in self.graph[node]:
      self.pq.put(edge)
    while not self.pq.empty():
      min_edge = self.pq.get()
      non_tree_node = -1
      if min_edge.first in self.forest and min_edge.second not in self.forest:
        non_tree_node = min_edge.second
      elif min_edge.second in self.forest and min_edge.first not in self.forest:
        non_tree_node = min_edge.first
      if non_tree_node == -1:
        continue
      self.forest.add(non_tree_node)
      self.forest_edges.append(min_edge)
      for edge in self.graph[non_tree_node]:
        self.pq.put(edge)

  def print_path(self):
    for node in self.graph:
      if node in self.forest:
        continue
      self.prim(node)
    print(f"Total cost: {sum([edge.weight for edge in self.forest_edges])}")


def main():
  nodes = int(input())
  edges = int(input())
  graph = {}
  for _ in range(edges):
      first, second, weight = [int(n) for n in input().split(' - ')]
      if first not in graph:
        graph[first] = []
      if second not in graph:
        graph[second] = []
      graph[first].append(Edge(first, second, weight))
      graph[second].append(Edge(first, second, weight))

  solution = Graph(edges, graph)
  solution.print_path()

if __name__ == "__main__":
  main()
