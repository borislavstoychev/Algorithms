

text = 'Reverse all words'

def recursive_solution(arr):
  if not len(arr):
    return

  word = arr.pop()[::-1]
  recursive_solution(arr)
  print(word, end=" ")

recursive_solution(text.split())