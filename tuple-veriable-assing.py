# multiple variable set in tuple---
numbers = (23, 45, 56, 34, 78, 96, 59, 78)
n1, n2, n3, n4, n5, n6, n7, n8 = numbers
print(numbers, type(numbers))

result = n1, n2, n8
print(result, type(result))

result_2 = n5
print(n5, type(n5))
