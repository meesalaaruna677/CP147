def divide(x, y):
    if y == 0:
        return "Division by zero is not possible"

    # Handle sign
    sign = -1 if (x < 0) ^ (y < 0) else 1
    x = abs(x)
    y = abs(y)

    low = 0
    high = max(1, x)
    precision = 0.000001

    while high - low > precision:
        mid = (low + high) / 2

        if abs(y * mid - x) < precision:
            result = mid
            break
        elif y * mid < x:
            low = mid
        else:
            high = mid
    else:
        result = (low + high) / 2

    return sign * result


# User Input
x = float(input("Enter dividend (x): "))
y = float(input("Enter divisor (y): "))

result = divide(x, y)

if isinstance(result, str):
    print(result)
else:
    print("Quotient =", round(result, 6))