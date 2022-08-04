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
  
  def __init__(self, edges, graph, forest, budget) -> None:
    self.edges = edges
    self.graph = graph
    self.forest = forest
    self.pq = PriorityQueue()
    self.budget_used = 0
    self.budget = budget

  def prim(self):
    for node in self.forest:
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
      if self.budget_used + min_edge.weight > self.budget:
        return
      self.forest.add(non_tree_node)
      self.budget_used += min_edge.weight
      for edge in self.graph[non_tree_node]:
        self.pq.put(edge)

  def print_path(self):
    print(f"Budget used: {self.budget_used}")


def main():
  budget = int(input())
  nodes = int(input())
  edges = int(input())
  graph = {}
  forest = set()
  for _ in range(edges):
      data = input().split()
      first, second, weight = [int(n) for n in data[:3]]
      if first not in graph:
        graph[first] = []
      if second not in graph:
        graph[second] = []
      graph[first].append(Edge(first, second, weight))
      graph[second].append(Edge(first, second, weight))
      if len(data) == 4:
        forest.add(first)
        forest.add(second)


  solution = Graph(edges, graph, forest, budget)
  solution.prim()
  solution.print_path()

if __name__ == "__main__":
  main()
