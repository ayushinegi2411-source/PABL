#Given an array and a range a, b. The task is to partition the array around the range
#such that the array is divided into three parts.
#1) All elements smaller than a come first.
#2) All elements in range a to b come next.
#3) All elements greater than b appear in the end.
#The individual elements of three sets can appear in any order. You are required to
#return the modified array.

def three_way_partition(arr, a, b):
    n = len(arr)
    
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if arr[mid] < a:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] > b:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

        else:  
            mid += 1

    return arr

arr = [1, 2, 3, 3, 4]
a = 1
b = 2
print(three_way_partition(arr,a,b))