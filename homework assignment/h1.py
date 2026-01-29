
"""Given an integer array arr[] and an integer k, your task is to find and return 
the kth smallest element in the given array"""
def kth_smallest(arr,k):  
            n = len(arr)

            for i in range(n-1):
                  min = i
                  for j in range(i+1,n):
                        if arr[j] < arr[min]:
                              min = j

                  arr[i],arr[min] = arr[min],arr[i]
            return [k-1]
    

arr =  [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

print(kth_smallest(arr, k))