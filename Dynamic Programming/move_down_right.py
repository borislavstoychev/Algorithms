from collections import deque


def main():
  row = int(input())
  col = int(input())
  matrix = [list(map(int, input().split())) for _ in range(row)]
  dp = [[0]*col for _ in range(row)]

  dp[0][0] = matrix[0][0]

  for c in range(1, col):
    dp[0][c] = dp[0][c-1] + matrix[0][c]

  for r in range(1, row):
    dp[r][0] = dp[r-1][0] + matrix[r][0]

  for r in range(1, row):
    for c in range(1, col):
      dp[r][c] = max(dp[r- 1][c], dp[r][c-1]) + matrix[r][c]

  r = row - 1 
  c = col - 1 
  result = deque()
  while r > 0 and c > 0:
    result.appendleft([r, c])
    if dp[r][c-1] >= dp[r-1][c]:
      c -= 1
    else:
      r -= 1
  while r > 0:
    result.appendleft([r,c])
    r -= 1
  while c > 0:
    result.appendleft([r,c])
    c -= 1
  result.appendleft([0,0])
  print(*result, sep=" ")

main()