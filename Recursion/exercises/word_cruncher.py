class WordCruncher():
  def __init__(self, strings, target) -> None:
      self.strings = strings
      self.target = target
      self.str_idx = {}
      self.str_count = {}
      self.used_str = []

  def tracking_parameters(self):
    for string in self.strings:
      if string in self.str_count:
          self.str_count[string] += 1
          continue
      self.str_count[string] = 1

      try:
          i = 0
          while True:
              i = self.target.index(string, i)
            
              if i not in self.str_idx:
                  self.str_idx[i] = []
              self.str_idx[i].append(string)
              i += len(string)
      except ValueError:
          pass

  def find_all_solutions(self, idx=0 ):
    if idx >= len(self.target):
        print(' '.join(self.used_str))
        return
    if idx not in self.str_idx:
        return
    for word in self.str_idx[idx]:
        if self.str_count[word] == 0:
            continue
        self.used_str.append(word)
        self.str_count[word] -= 1
        self.find_all_solutions(idx + len(word))
        self.used_str.pop()
        self.str_count[word] += 1

def main():
  strings = input().split(', ')
  target = input()
  cruncher = WordCruncher(strings, target)
  cruncher.tracking_parameters()
  cruncher.find_all_solutions()

if __name__ == "__main__":
  main()