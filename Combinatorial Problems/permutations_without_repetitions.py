class Permute:
    def __init__(self, elements):
        self.elements = elements

    def solve(self, index):
        if index >= len(self.elements):
            print(self.elements)

        else:
            self.solve(index + 1)
            for i in range(index + 1, len(self.elements)):
                self.elements[index], self.elements[i] = self.elements[i], self.elements[index]
                self.solve(index + 1)
                self.elements[index], self.elements[i] = self.elements[i], self.elements[index]



permute = Permute(['A', 'B', 'C'])
permute.solve(0)

# class Permute:
#     def __init__(self, elements):
#         self.used = [False]*len(elements)
#         self.elements = elements
#         self.permutations = elements[::]
#
#     def solve(self, index):
#         if index >= len(self.permutations):
#             print(self.permutations)
#
#         else:
#             for i in range(0, len(self.elements)):
#                 if not self.used[i]:
#                     self.used[i] = True
#                     self.permutations[index] = self.elements[i]
#                     self.solve(index + 1)
#                     self.used[i] = False
#
#
# permute = Permute(['A', 'B', 'C'])
# permute.solve(0)
