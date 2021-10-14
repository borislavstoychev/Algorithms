class Queens:
    def __init__(self, size):
        self.size = size
        self.attack_row = set()
        self.attack_col = set()
        self.attack_left_diagonal = set()
        self.attack_right_diagonal = set()
        self.matrix = [[False] * size for i in range(0, size)]
        self.count = 0

    def put_q(self, r=0):
        if r == self.size:
            self.count += 1
            self.__str__()
            return

        for c in range(0, self.size):
            if not self.__is_attacked(r, c):
                self.matrix[r][c] = True
                self.attack_row.add(r)
                self.attack_col.add(c)
                self.attack_left_diagonal.add(r - c)
                self.attack_right_diagonal.add(r + c)

                self.put_q(r + 1)

                self.matrix[r][c] = False
                self.attack_row.remove(r)
                self.attack_col.remove(c)
                self.attack_left_diagonal.remove(r - c)
                self.attack_right_diagonal.remove(r + c)

    def __is_attacked(self, r, c):
        return c in self.attack_col or \
               r in self.attack_row or \
               r - c in self.attack_left_diagonal or \
               r + c in self.attack_right_diagonal

    def __str__(self):
        for i in range(0, self.size):
            result = ''
            for j in range(0, self.size):
                if self.matrix[i][j]:
                    result += "* "
                else:
                    result += "- "
            print(result)
        print('')


def main():
    """Initialize and solve the n queens puzzle"""
    q = Queens(int(input()))
    q.put_q()
    print(f"Total combinations are {q.count}")


if __name__ == "__main__":
    # execute only if run as a script
    main()
