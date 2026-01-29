"given an array find largest element and return it "

def largest_element(arr):
    max_value = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]

    return max_value

arr = [1,8,7,56,90]
print(largest_element(arr))