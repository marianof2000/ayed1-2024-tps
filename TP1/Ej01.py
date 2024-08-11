def mayor_estricto(a, b, c):
    if a == b:
        if b >= c:
            return -1
    if b == c:
        if b >= a:
            return -1
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c


assert (-1 == mayor_estricto(3, 5, 5))
assert (7 == mayor_estricto(3, 5, 7))
assert (5 == mayor_estricto(3, 3, 5))
