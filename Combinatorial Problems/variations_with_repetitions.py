class Variations:
    def __init__(self, elements, num):
        self.elements = elements
        self.variations = elements[:num]

    def solve(self, index):
        if index >= len(self.variations):
            print(self.variations)

        else:
            for i in range(0, len(self.elements)):
                self.variations[index] = self.elements[i]
                self.solve(index + 1)


permute = Variations(['A', 'B', 'C'], 2)
permute.solve(0)