def dfs (node, graph, visited, component):
  if visited[node]:
    return
  visited[node] = True
  for child in graph[node]:
    dfs(child, graph, visited, component)
  component.append(node)

def main ():
  graph = []
  for _ in range(int(input())):
    graph.append(list(map(int, input().split())))
  visited = [False] * len(graph)
  for node in range(len(graph)):
    if visited[node]:
      continue
    component = []
    dfs(node, graph, visited, component)
    print(f'Connected component: {" ".join(list(map(str, component)))}')

main()