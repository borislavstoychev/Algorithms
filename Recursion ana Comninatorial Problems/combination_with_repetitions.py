class Combinations:
    def __init__(self, elements, num):
        self.elements = elements
        self.slots = elements[:num]

    def solve(self, index, start=0):
        if index >= len(self.slots):
            print(self.slots)

        else:
            for i in range(start, len(self.elements)):
                self.slots[index] = self.elements[i]
                self.solve(index + 1, i)


permute = Combinations([i for i in range(1, int(input()) + 1)], int(input()))
permute.solve(0)
