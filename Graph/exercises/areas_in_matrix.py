def create_matrix(rows, cols):
  m = []
  v = []
  for _ in range(rows):
    m.append(list(input()))
    v.append([False] * cols)
  return m, v

def dfs(parent, row, col, matrix, visited):
  if row < 0 or row >= len(matrix) or col >= len(matrix[0]) or col < 0:
    return
  if visited[row][col]:
    return
  if matrix[row][col] != parent:
    return

  visited[row][col] = True
  dfs(parent, row - 1, col, matrix, visited)
  dfs(parent, row + 1, col, matrix, visited)
  dfs(parent, row, col - 1, matrix, visited)
  dfs(parent, row, col + 1, matrix, visited)

def main():
  rows = int(input())
  cols = int(input())
  matrix, visited = create_matrix(rows, cols)
  areas = {}
  total = 0
  for row in range(rows):
    for col in range(cols):
      if visited[row][col]:
        continue
      key = matrix[row][col]
      dfs(key, row, col, matrix, visited)
      if key not in areas:
        areas[key] = 1
      else:
        areas[key] += 1
      total += 1
  print(f"Areas: {total}")
  for key, value in sorted(areas.items()):
    print(f"Letter '{key}' -> {value}")

main()
  
