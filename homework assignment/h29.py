"Given an array arr[], find the minimum number of operations required to make the"
"sum of its elements less than or equal to half of the original sum. In one operation, you"
"may replace any element with half of its value (with floating-point precision)."

import heapq

def minOperations(arr):
    total = sum(arr)
    target = total / 2
    heap = [-x for x in arr]
    heapq.heapify(heap)

    ops = 0
    curr = total

    while curr > target:
        x = -heapq.heappop(heap)
        half = x / 2
        curr -= half
        heapq.heappush(heap, -half)
        ops += 1

    return ops