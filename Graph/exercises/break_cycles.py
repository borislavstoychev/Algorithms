class BreakCycles():
  def __init__(self, nodes = int(input())) -> None:
    self.graph = {}
    self.nodes = nodes
    self.edges = []
    self.remove_edges = []

  def dfs(self, n, destination, visited) -> None:
    if n in visited:
      return
    visited.add(n)
    if n == destination:
      return
    for child in self.graph[n]:
      self.dfs(child, destination, visited)

  def create_graph(self):
    for _ in range(self.nodes):
      node, children_str = input().split(" -> ")
      children = children_str.split()
      self.graph[node] = children
      for child in children:
        self.edges.append((node, child))

  def path_exist(self, s, d) -> bool:
    visited = set()

    self.dfs(s, d, visited)
    return d in visited

  def make_the_graph_acyclic(self):
    for sorce, destination in sorted(self.edges, key=lambda x: (x[0],x[1])):
      if destination not in self.graph[sorce] or sorce not in self.graph[destination]:
        continue
      self.graph[sorce].remove(destination)
      self.graph[destination].remove(sorce)

      if self.path_exist(sorce, destination):
        self.remove_edges.append((sorce, destination))
      else:
        self.graph[sorce].append(destination)
        self.graph[destination].append(sorce)

    print(f"Edges to remove: {len(self.remove_edges)}")
    for first, second in self.remove_edges:
      print(f"{first} - {second}")


g = BreakCycles()


g.create_graph()
g.make_the_graph_acyclic()
