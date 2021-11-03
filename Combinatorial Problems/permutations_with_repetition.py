class Permute:
    def __init__(self, elements):
        self.elements = elements

    def solve(self, index):
        if index >= len(self.elements):
            print(self.elements)

        else:
            self.solve(index + 1)
            swapped = {self.elements[index]}
            for i in range(index + 1, len(self.elements)):
                if not self.elements[i] in swapped:
                    self.elements[index], self.elements[i] = self.elements[i], self.elements[index]
                    self.solve(index + 1)
                    self.elements[index], self.elements[i] = self.elements[i], self.elements[index]
                    swapped.add(self.elements[i])


permute = Permute(['A', 'B', 'B'])
permute.solve(0)