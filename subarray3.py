def max_subarray(arr):
    n = len(arr)
    max_sum = float("-inf")

    for i in range(n):
        for j in range(i, n):
            current_sum = 0
            for k in range(i, j + 1):
                current_sum += arr[k]
            max_sum = max(max_sum, current_sum)

    return max_sum


n = int(input("Enter n: "))
arr = list(map(int, input("Enter array: ").split()))

print("Maximum Subarray Sum:", max_subarray(arr))