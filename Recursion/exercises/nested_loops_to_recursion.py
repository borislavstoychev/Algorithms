def vectors_1_n(index, vector):
    if index >= len(vector):
        print(*vector, sep=" ")
    else:
        for i in range(1, len(vector)+1):
            vector[index] = i
            vectors_1_n(index + 1, vector)


vectors_1_n(0, int(input())*[1])