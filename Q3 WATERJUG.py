
a = 8
b = 0
c = 0

print(a, b, c)

# Pour 8L into 5L
b = 5
a = a - 5
print(a, b, c)

# Pour 5L into 3L
c = 3
b = b - 3
print(a, b, c)

# Pour 3L into 8L
a = a + c
c = 0
print(a, b, c)

# Pour remaining 2L into 3L
c = b
b = 0
print(a, b, c)

# Fill 5L jug
b = 5
print(a, b, c)

# Pour 5L into 3L
c = 3
b = b - 3
print(a, b, c)

print("Water measurement completed")
