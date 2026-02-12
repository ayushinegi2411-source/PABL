#Given an integer array arr[] and an integer k, your task is to find and return the kth smallest 
#element in the given array. 

import random

def kth_smallest(arr, k):
    def quickselect(left, right):
        pivot_index = random.randint(left, right)
        pivot_value = arr[pivot_index]

        
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1

        
        arr[store_index], arr[right] = arr[right], arr[store_index]

        if store_index == k - 1:
            return arr[store_index]
        elif store_index > k - 1:
            return quickselect(left, store_index - 1)
        else:
            return quickselect(store_index + 1, right)

    return quickselect(0, len(arr) - 1)

arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
print(kth_smallest(arr,k))