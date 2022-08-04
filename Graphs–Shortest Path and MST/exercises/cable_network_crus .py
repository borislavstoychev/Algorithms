class Edge():
  def __init__(self, first, second, weight) -> None:
    self.first = first
    self.second = second
    self.weight = weight

class Graph():
  
  def __init__(self, edges, graph, max_node, parent, budget, forest) -> None:
    self.edges = edges
    self.graph = graph
    self.max_node = max_node
    self.forest = forest
    self.parent = parent
    self.budget = budget
    self.used_budget = 0
    
  def find_root(self, node):
    while node != self.parent[node]:
      node = self.parent[node]
    return node

  def kruskal(self):
    for edge in sorted(self.graph, key=lambda e: e.weight):
      first_node_root = self.find_root(edge.first)
      second_node_root = self.find_root(edge.second)
      non_tree_node = -1
      if edge.first in self.forest and edge.second not in self.forest:
        non_tree_node = edge.second
      elif edge.second in self.forest and edge.first not in self.forest:
        non_tree_node = edge.first
      if non_tree_node == -1:
        continue

      # if first_node_root != second_node_root:
      if self.used_budget + edge.weight > self.budget:
          return
      self.forest.add(non_tree_node)
      self.parent[first_node_root] = second_node_root
      self.used_budget += edge.weight

  def print_path(self):
    print(f"Budget used: {self.used_budget}")
    # print(self.forest)


def main():
  budget = int(input())
  nodes = int(input())
  edges = int(input())
  parent = [num for num in range(nodes)]
  forest = set()
  graph = []
  for _ in range(edges):
    data = input().split()
    first, second, weight = [int(n) for n in data[:3]]
    graph.append(Edge(first, second, weight))
    if len(data) == 4:
        parent[first]= second
        forest.add(first)
        forest.add(second)


  solution = Graph(edges, graph, nodes, parent, budget, forest)
  solution.kruskal()
  solution.print_path()
#ToDo 80/100
if __name__ == "__main__":
  main()
