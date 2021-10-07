def vectors_0_1(index, vector):
    if index >= len(vector):
        print(vector)
    else:
        for i in range(0, 2):
            vector[index] = i
            vectors_0_1(index + 1, vector)


vectors_0_1(0, 3*[0])