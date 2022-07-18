def get_param(arr, n, r):
    data = [0] * r
    combinations(arr, data, 0, n - 1, 0, r)


def combinations(arr, data, start, end, index, r):
    if index == r:
        for j in range(r):
            print(data[j], end=" ")
        print()
        return

    i = start
    while i <= end and end - i + 1 >= r - index:
        data[index] = arr[i]
        combinations(arr, data, i + 1, end, index + 1, r)
        i += 1


arr = input().split(" ")
r = int(input())
n = len(arr)
get_param(arr, n, r)

