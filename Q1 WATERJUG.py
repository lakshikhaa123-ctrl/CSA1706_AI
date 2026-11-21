
a = 0
b = 0

while b != 4:
    if a == 0:
        a = 5
    elif b < 8:
        b = b + a
        a = 0
        if b > 8:
            a = b - 8
            b = 8
    else:
        b = 0

    print(a, b)

print("4 litres obtained")
