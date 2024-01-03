def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        posibleMatch = arr[middle]

        if target == posibleMatch:
            return middle
        elif target < posibleMatch:
            right = middle - 1
        else:
            left = middle + 1

    return -1


# Test:
# binarySearch([0, 1, 2, 8, 12, 23, 32, 33, 45, 56, 78, 87, 91, 99], 12)
# binarySearch([21, 22, 34, 44, 47, 67, 87, 89, 91, 92], 56)
# binarySearch([22, 34, 55, 65, 77, 87, 89, 99], 50)
# binarySearch([1, 3, 5, 7, 8, 9], 5)
# binarySearch([12, 45, 67, 87], 34)