n = int(input())

arr = list(map(int, input().split()))

arr.sort()

p1 = arr[0] * arr[1] * arr[-1]

p2 = arr[-1] * arr[-2] * arr[-3]

if p1 > p2:
    print(arr[0], arr[1], arr[-1])
else:
    print(arr[-3], arr[-2], arr[-1])