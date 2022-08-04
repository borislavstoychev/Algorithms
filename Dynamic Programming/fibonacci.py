def fibonacci(n, memo={}):
    if n in memo:
      return memo[n]
    if n <= 2:
        return 1
    else:
      result = fibonacci(n - 1) + fibonacci(n - 2)
      memo[n] = result
      return result

print(fibonacci(int(input())))