def max_subarray(arr):
    n = len(arr)
    max_sum = float("-inf")

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)

    return max_sum


n = int(input("Enter n: "))
arr = list(map(int, input("Enter array: ").split()))

print("Maximum Subarray Sum:", max_subarray(arr))