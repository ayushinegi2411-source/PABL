#Given three sorted arrays in non-decreasing order,
#print all common elements in non-decreasing order across these arrays.
#If there are no such elements return an empty array.
#In this case, the output will be -1.

def common_elements(arr1, arr2, arr3):
    i = j = k = 0
    n1, n2, n3 = len(arr1), len(arr2), len(arr3)
    result = []

    while i < n1 and j < n2 and k < n3:

        
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            val = arr1[i]

            
            while i < n1 and arr1[i] == val:
                i += 1
            while j < n2 and arr2[j] == val:
                j += 1
            while k < n3 and arr3[k] == val:
                k += 1

        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return result if result else [-1]

arr1 = [1, 5, 10, 20, 40, 80] 
arr2 = [6, 7, 20, 80, 100] 
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
print(common_elements(arr1,arr2,arr3))