"Sort an array of strings according to string lengths"

def sortByLength(arr):
    return sorted(arr, key=lambda x: len(x))