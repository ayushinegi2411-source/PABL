" Given an array arr, rotate the array by one position in clockwise direction. "
def rotatearray(arr):
    n = len(arr)
    last = arr[n - 1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last
    return arr


arr = [1, 2, 3, 4, 5]
print(rotatearray(arr))
