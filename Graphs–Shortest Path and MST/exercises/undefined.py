from collections import deque


class Edge():
  def __init__(self, source, destination, weight) -> None:
    self.source = source
    self.destination = destination
    self.weight = weight

class Graph():
  def __init__(self, nodes, edges, graph, start, target ) -> None:
    self.nodes = nodes
    self.edges = edges
    self. graph = graph
    self.start = start
    self.target = target
    self.distance = [float('inf')] * (self.nodes + 1)
    self.parent = [None] * (self.nodes + 1)
    self.path = deque()

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
          print('Undefined')
          return
    node = self.target
    while node is not None:
        self.path.appendleft(node)
        node = self.parent[node]

    print(*self.path, sep=" ")
    print(self.distance[self.target])


def main():
  nodes = int(input())
  edges = int(input())
  graph = []
  for _ in range(edges):
      source, destination, weight = list(map(int, input().split()))
      graph.append(Edge(source, destination, weight))
  start = int(input())
  target = int(input())

  solution = Graph(nodes, edges, graph, start, target)
  solution.find_path()

if __name__ == "__main__":
  main()

      


    