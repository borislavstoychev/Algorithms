from collections import deque

class Graph():
  def __init__(self, nodes, graph, start, end) -> None:
    self.nodes = nodes
    self.graph = graph
    self.start_node = start
    self.destination_node = end
    self.parent = {self.start_node: None}
    self.path = deque()


  def shortest_path(self):
    visited = {self.start_node}
    queue = deque([self.start_node]) 

    while queue:
      node = queue.popleft()
      if node == self.destination_node:
        break
      for child in self.graph[node]:
        if child in visited:
          continue
        visited.add(child)
        queue.append(child)
        self.parent[child] = node

  def show_path(self):
    node = self.destination_node
    if self.destination_node not in self.parent:
      print(f"{{{self.start_node}, {self.destination_node}}} -> -1")
      return
    while node is not None:
      self.path.appendleft(node)
      node = self.parent[node]
    print(f"{{{self.start_node}, {self.destination_node}}} -> {len(self.path) - 1}")

def main():
  nodes = int(input())
  pairs = int(input())
  graph = {}
  for _ in range(nodes):
    source, destination = input().split(":")
    node = int(source)
    children = [int(n) for n in destination.split()] if destination else []
    graph[node] = children
  for _ in range(pairs):
    start, end = list(map(int, input().split("-")))
    solution = Graph(nodes, graph, start, end)
    solution.shortest_path()
    solution.show_path()

if __name__ == "__main__":
  main()
