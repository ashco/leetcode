def binarySearch(arr, val):
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


l1 = [3, 5, 7, 8, 12, 13, 23, 42]
print(binarySearch(l1, 14))
