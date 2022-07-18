def find_path(row, col, rows, cols):
  if row >= rows or col >= cols:
    return 0
  if row == row-1 or col == cols - 1:
    return 1

  result = 0
  result += find_path(row, col+1, rows, cols)
  result += find_path(row+1, col, rows, cols) 

  return result

print(find_path(0,0, int(input()), int(input())))