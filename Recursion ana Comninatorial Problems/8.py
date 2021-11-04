class Combinations:
    def __init__(self, elements, num):
        self.elements = elements
        self.slots = elements[:num]
        self.all = []

    def solve(self, index=0, start=0):
        if index >= len(self.slots):
            self.all.append(self.slots[::])

        else:
            for i in range(start, len(self.elements)):
                self.slots[index] = self.elements[i]
                self.solve(index + 1, i + 1)


def main():
    all_girls = input().split(", ")
    all_boys = input().split(", ")

    girls = Combinations(all_girls, 3)
    boys = Combinations(all_boys, 2)
    girls.solve()
    boys.solve()
    for comb_g in girls.all:
        for comb_b in boys.all:
            print(*comb_g + comb_b, sep=", ")


if __name__ == "__main__":
    main()

# Lisa, Yoana, Marta, Rachel
# Georgi, Garry, Bob
