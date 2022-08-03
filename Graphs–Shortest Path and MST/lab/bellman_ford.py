from collections import deque


class Edge():
  def __init__(self, source, destination, weight) -> None:
    self.source = source
    self.destination = destination
    self.weight = weight

class BellmanFord():
  def __init__(self, nodes = int(input()), edges= int(input())) -> None:
    self.nodes = nodes
    self.edges = edges
    self. graph = []
    self.start = None
    self.target = None
    self.distance = [float('inf')] * (self.nodes + 1)
    self.parent = [None] * (self.nodes + 1)
    self.path = deque()


  def create_graph(self):
    for _ in range(self.edges):
      source, destination, weight = list(map(int, input().split()))
      self.graph.append(Edge(source, destination, weight))
    self.start = int(input())
    self.target = int(input())

  def find_path(self):
    self.distance[self.start] = 0
    for _ in range(self.nodes - 1):
      updated = False
      for edge in self.graph:
        if self.distance[edge.source] == float('inf'):
          continue
        new_distance = self.distance[edge.source] + edge.weight
        if new_distance < self.distance[edge.destination]:
          self.distance[edge.destination] = new_distance
          self.parent[edge.destination] = edge.source
          updated = True
      if not updated:
        break
    for edge in self.graph:
        new_distance = self.distance[edge.source] + edge.weight
        if new_distance < self.distance[edge.destination]:
          print('Negative Cycle Detected')
          return
    node = self.target
    while node is not None:
        self.path.appendleft(node)
        node = self.parent[node]

    print(*self.path, sep=" ")
    print(self.distance[self.target])



solution = BellmanFord()
solution.create_graph()
solution.find_path()

      


    