from collections import deque


def main():
  str1 = input()
  str2 = input()

  rows = len(str1) + 1
  cols = len(str2) + 1

  dp = [[0]*cols for _ in range(rows)]

  for row in range(1, rows):
    for col in range(1, cols):
      if str1[row - 1] == str2[col -1]:
        dp[row][col] = dp[row -1][col - 1] + 1
      else:
        dp[row][col] = max(dp[row -1 ][col], dp[row][col-1])

  print(dp[rows -1][cols - 1])  

  row = rows -1 
  col = cols - 1
  result = deque()
  while row > 0 and col > 0:
    
    if str1[row - 1] == str2[col -1]:
      result.appendleft(str1[row - 1])
      row -= 1
      col -= 1
    elif dp[row -1][col] > dp[row][col -1]:
      row -= 1
    else:
      col -= 1
  print(*result, sep=" ")

main()