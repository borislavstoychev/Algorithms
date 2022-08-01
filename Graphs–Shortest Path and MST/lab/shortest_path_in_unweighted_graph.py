from collections import deque

class UnweightedGraph():
  def __init__(self, nodes=int(input()), edges=int(input())) -> None:
    self.nodes = nodes
    self.edges = edges
    self.graph = [[] for _ in range(self.nodes + 1)]
    self.start_node = 0
    self.destination_node = 0
    self.parent = [None] * (self.nodes + 1)
    self.path = deque()

    
  def create_graph(self):
    for _ in range(self.edges):
      sorce, destination = list(map(int, input().split()))
      self.graph[sorce].append(destination)
    self.start_node = int(input())
    self.destination_node = int(input())

  def shortest_path(self):
    visited = [False]* (self.nodes + 1)
    visited[self.start_node] = True
    queue = deque([self.start_node]) 

    while queue:
      node = queue.popleft()
      if node == self.destination_node:
        break
      for child in self.graph[node]:
        if visited[child]:
          continue
        visited[child] = True
        queue.append(child)
        self.parent[child] = node

  def show_path(self):
    node = self.destination_node
    while node is not None:
      self.path.appendleft(node)
      node = self.parent[node]

    print(f"Shortest path length is: {len(self.path) - 1 }")
    print(*self.path, sep=" ")


solution = UnweightedGraph()
solution.create_graph()
solution.shortest_path()
solution.show_path()
  