"Given an array arr[]. Your task is to find the minimum and maximum elements in the array"

def getMinMax(arr):
    minimum = arr[0]
    maximum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
        if arr[i] > maximum:
            maximum = arr[i]

    return [minimum, maximum]


arr = [1, 4, 3, 5, 8, 6]
print(getMinMax(arr))
