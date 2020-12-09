# list multiplication system--
list = [23, 35, 45 ,67, 37, 57, 59, 60]
multiplication = []

for n in list:
    multiplication.append(n * 2)

print(multiplication)

# list comprehensions ---
list = [23, 35, 45 ,67, 37, 57, 59, 60]
result = [2 * x for x in list]
print(result)