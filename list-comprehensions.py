# find out even number in list---
list = [23, 45, 76, 78, 35, 67, 34, 11, 33, 39, 49, 88]
even_list = [x for x in list if x % 2 == 0]
print(even_list)


# find out odd number in list---
list = [23, 45, 76, 78, 35, 67, 34, 11, 33, 39, 49, 88]
odd_list = [x for x in list if x % 2 != 0]
print(odd_list)
