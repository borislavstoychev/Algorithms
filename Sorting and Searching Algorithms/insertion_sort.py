# Първия цикъл обхожда целия масив и докато има елемент по малък от ляво ги разменя. 
# swap evry elements to the left, while current num is smaller then left num
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

print(insertion_sort([9, 8, 7, 55, 35, 17]))