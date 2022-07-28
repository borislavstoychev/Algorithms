class Salaries():
  def __init__(self, node = int(input())) -> None:
    self.graph = []
    self.node = node
    self.salaries = [None]* self.node

  def dfs(self, n):
    if self.salaries[n] is not None:
      return self.salaries[n]
    if len(self.graph[n]) == 0:
      self.salaries[n] = 1
      return 1
    salary = 0
    for child in self.graph[n]:
      salary += self.dfs(child)
    self.salaries[n] = salary
    return salary

  def create_graph(self):
    for _ in range(self.node):
      line = input()
      children =[]
      for idx, state in enumerate(line):
        if state == "Y":
          children.append(idx)
      self.graph.append(children)

  def calculate_salary(self):
    salary = 0
    for node in range(self.node):
      salary += self.dfs(node)
    print(salary)


g = Salaries()


g.create_graph()
g.calculate_salary()
