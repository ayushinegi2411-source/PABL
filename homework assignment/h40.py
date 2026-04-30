"Given an array arr[] of time strings in 24-hour clock format "HH:MM:SS", return"
"the minimum difference in seconds between any two time strings in the arr[]."
"The clock wraps around at midnight, so the time difference between "23:59:59" and "00:00:00" is 1 second."

def minDifference(arr):
    times = []

    for t in arr:
        h, m, s = map(int, t.split(':'))
        times.append(h * 3600 + m * 60 + s)

    times.sort()

    res = float('inf')

    for i in range(1, len(times)):
        res = min(res, times[i] - times[i-1])

    # circular case
    res = min(res, 86400 - times[-1] + times[0])

    return res