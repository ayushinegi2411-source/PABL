#Given an array of intervals where intervals[i] = [starti, endi], merge all 
#overlapping intervals, and return an array of the non-overlapping intervals that 
#cover all the intervals in the input.

def merge(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = []
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged.append([current_start, current_end])
            current_start, current_end = start, end

    merged.append([current_start, current_end])

    return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))