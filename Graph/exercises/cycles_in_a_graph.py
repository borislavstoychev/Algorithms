class AcyclicGraph():
  def __init__(self) -> None:
    self.graph = {}
    self.visited = set()
    self.cylles = set()

  def dfs(self, node):
    if node in self.cylles:
      raise Exception
    if node in self.visited:
      return

    self.visited.add(node)
    self.cylles.add(node)
    for child in self.graph[node]:
      self.dfs(child)

    self.cylles.remove(node)

  def create_graph(self):
    while True:
      command = input()
      if command == "End":
        break
      sorce, destination = command.split('-')
      if sorce not in self.graph:
        self.graph[sorce] = []
      if destination not in self.graph:
        self.graph[destination] = []
      self.graph[sorce].append(destination)
  
  def acyclic_check(self):
    try:
      for node in self.graph:
        self.dfs(node)
      print('Acyclic: Yes')
    except Exception:
      print('Acyclic: No')

g = AcyclicGraph()
g.create_graph()
g.acyclic_check()