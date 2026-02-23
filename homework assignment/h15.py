#Given an array arr[] of positive integers. Return true if all the array elements are
#palindrome otherwise, return false.

def all_palindromes(arr):
    for num in arr:
        if str(num) != str(num)[::-1]:
            return False
    return True
arr = [111, 222, 333, 444, 555]

print(all_palindromes(arr))