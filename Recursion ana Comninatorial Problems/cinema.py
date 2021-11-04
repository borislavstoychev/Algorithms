class Permute:
    def __init__(self, elements, seats, locked_seats):
        self.elements = elements
        self.seats = seats
        self.locked_seats = locked_seats

    def solve(self, index):
        if index >= len(self.elements):
            name_index = 0
            for i in range(len(self.seats)):
                if i in self.locked_seats:
                    continue
                self.seats[i] = self.elements[name_index]
                name_index += 1
            print(self.seats)

        else:
            self.solve(index + 1)
            for i in range(index + 1, len(self.elements)):
                self.elements[index], self.elements[i] = self.elements[i], self.elements[index]
                self.solve(index + 1)
                self.elements[index], self.elements[i] = self.elements[i], self.elements[index]


def main():
    names = input().split(", ")
    seats = [None] * len(names)
    locked_seat = []
    while True:
        parts = input()
        if parts == 'generate':
            break
        name, seat = parts.split(" - ")
        seats[int(seat) - 1] = name
        locked_seat.append(int(seat) - 1)

        names.remove(name)
    return names, seats, locked_seat


if __name__ == "__main__":
    Permute(*main()).solve(0)

# Peter, Amy, Georgy, Rick
# Amy - 1
# Rick - 4
# generate
