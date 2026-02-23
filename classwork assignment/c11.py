#Given an array arr[] of integers, calculate the median.

def find_median(arr):
    arr.sort()
    n = len(arr)

    if n % 2 == 1:  
        return arr[n // 2]
    else:            
        mid1 = arr[n // 2 - 1]
        mid2 = arr[n // 2]
        return (mid1 + mid2) / 2
    
arr = [90, 100, 78, 89, 67]
print(find_median(arr))