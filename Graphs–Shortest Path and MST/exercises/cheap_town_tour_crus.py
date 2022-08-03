class Edge():
  def __init__(self, first, second, weight) -> None:
    self.first = first
    self.second = second
    self.weight = weight

class Graph():
  
  def __init__(self, edges, graph, max_node) -> None:
    self.edges = edges
    self.graph = graph
    self.max_node = max_node
    self.forest = []
    self.parent = [num for num in range(max_node + 1)]
    
  def find_root(self, node):
    while node != self.parent[node]:
      node = self.parent[node]
    return node

  def kruskal(self):
    for edge in sorted(self.graph, key=lambda e: e.weight):
      first_node_root = self.find_root(edge.first)
      second_node_root = self.find_root(edge.second)
      if first_node_root != second_node_root:
        self.parent[first_node_root] = second_node_root
        self.forest.append(edge)

  def print_path(self):
    print(f"Total cost: {sum([edge.weight for edge in self.forest])}")


def main():
  max_node = int(input())
  edges = int(input())
  graph = []
  for _ in range(edges):
    first, second, weight = [int(n) for n in input().split(' - ')]
    graph.append(Edge(first, second, weight))

  solution = Graph(edges, graph, max_node)
  solution.kruskal()
  solution.print_path()

if __name__ == "__main__":
  main()
