class RoadReconstruction():
  def __init__(self, nodes = int(input()),edges_count = int(input())) -> None:
    self.nodes = nodes
    self.graph = [[] for _ in range(self.nodes)]
    self.edges_count = edges_count
    self.edges = []
    self.importan_street = []

  def dfs(self, n, visited) -> None:
    if visited[n]:
      return
    visited[n] = True
    
    for child in self.graph[n]:
      self.dfs(child, visited)

  def create_graph(self):
    for _ in range(self.edges_count):
      first, second = list(map(int, input().split(" - ")))
      self.graph[first].append(second)
      self.graph[second].append(first)
      self.edges.append((min(first, second), max(first, second)))

  def street_connects(self):
    for first, second in self.edges:
      self.graph[first].remove(second)
      self.graph[second].remove(first)
      
      visited = [False] * self.nodes
      self.dfs(0, visited)

      if not all(visited):
        self.importan_street.append((first,second))

      self.graph[first].append(second)
      self.graph[second].append(first)

    print('Important streets:')
    for first, second in self.importan_street:
      print(f"{first} {second}")


g = RoadReconstruction()



g.create_graph()
g.street_connects()
