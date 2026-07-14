def find_median(arr1, arr2):
    merged = sorted(arr1 + arr2)
    n = len(merged)

    if n % 2 == 1:
        return merged[n // 2]
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2


n1 = int(input("Enter size of first array: "))
arr1 = list(map(int, input("Enter first array elements: ").split()))

n2 = int(input("Enter size of second array: "))
arr2 = list(map(int, input("Enter second array elements: ").split()))

print("Median =", find_median(arr1, arr2))