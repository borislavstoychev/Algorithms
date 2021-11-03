def binom(num, k):
    if num <= 1:
        return 1
    if k == 0 or k == num:
        return 1
    return binom(num - 1, k) + binom(num - 1, k - 1)


print(binom(5, 3))
