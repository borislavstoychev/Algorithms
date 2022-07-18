class ReverseArray:
    def __init__(self, arr):
        self.arr = arr

    def reverse(self, left=0):
        if left >= len(self.arr) // 2:
            print(*self.arr, sep=" ")
        else:
            right = len(self.arr) - 1 - left
            self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
            self.reverse(left + 1)


reverse = ReverseArray(input().split())
reverse.reverse()
