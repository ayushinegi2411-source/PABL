#Given two sorted arrays a[] and b[] of size n and m respectively,
#the task is to merge them in sorted order without using any extra space.
#Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.

import math

def merge(a, b):
    n = len(a)
    m = len(b)
    gap = math.ceil((n + m) / 2)

    while gap > 0:
        i = 0
        j = gap

        while j < n + m:
            if i < n and j < n:
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]

            elif i < n and j >= n:
                if a[i] > b[j - n]:
                    a[i], b[j - n] = b[j - n], a[i]

            else:
                if b[i - n] > b[j - n]:
                    b[i - n], b[j - n] = b[j - n], b[i - n]

            i += 1
            j += 1

        if gap == 1:
            gap = 0
        else:
            gap = math.ceil(gap / 2)

a = [2, 4, 7, 10]
b = [2, 3]
merge(a,b)
print (a)
print (b)