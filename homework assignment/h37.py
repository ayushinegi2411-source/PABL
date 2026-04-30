"Given a sorted array arr[] containing distinct non negative integers that has been"
"rotated at some unknown pivot, and a value x. Your task is to count the number of"
"elements in the array that are less than or equal to x."

def countLessEqual(arr, x):
    return sum(1 for i in arr if i <= x)