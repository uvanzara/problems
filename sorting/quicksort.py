'''
Implement the quicksort sorting algorithms!
'''
import random

# Quicksort

def Quicksort(arr):
    res = quicksorthelper(arr, 0, len(arr)-1)
    return res

def quicksorthelper(arr, start, end):
    if start >= end:
        return
    randindex = random.randint(start, end)
    # print("pivot index = {}".format(randindex))
    # swap the pivot element with the start element
    arr[start], arr[randindex] = arr[randindex], arr[start]
    # pivot = arr[start]
    smaller = start

    for bigger in range(start+1, end+1):
        if arr[bigger] < arr[start]:
            smaller += 1
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]

    arr[start], arr[smaller] = arr[smaller], arr[start]

    quicksorthelper(arr, start, smaller - 1)
    quicksorthelper(arr, smaller + 1, end)

    return arr    

print(Quicksort([6,5,4,4, 6, 9, 7, 5, 3,2,1]))