
a = 12
b = 0
c = 0

print(a, b, c)

# 12L to 8L
b = 8
a = a - 8
print(a, b, c)

# 8L to 5L
c = 5
b = b - 5
print(a, b, c)

# 5L to 12L
a = a + c
c = 0
print(a, b, c)

# 8L to 5L
c = b
b = 0
print(a, b, c)

# 12L to 8L
b = 8
a = a - 8
print(a, b, c)

# 8L to 5L
c = 5
b = b - 5
print(a, b, c)

# 5L to 12L
a = a + c
c = 0
print(a, b, c)

print("6 litres obtained in two jugs")
