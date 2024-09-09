def computeGCD(a, m):
    while m:
        a, m = m, a % m
    return abs(a)


def extendedEuclidean(a, m):
    if computeGCD(a, m) != 1:
        return None

    original_m = m
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while m:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return x0 % original_m

a = 3
m = 7
inverse = extendedEuclidean(a, m)

if inverse is not None:
    print(f"The modular multiplicative inverse of {a} modulo {m} is {inverse}")
else:
    print(f"No modular multiplicative inverse exists for {a} modulo {m}")
