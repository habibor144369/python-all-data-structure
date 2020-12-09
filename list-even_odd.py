# find out even number and odd number in list----

list = [11, 45, 41, 60, 66, 10, 20, 13, 14, 26]

even_list = []
odd_list = []
for even in list:
    if even % 2 == 0:
        even_list.append(even)
    else:
        odd_list.append(even)

print(even_list)
print(odd_list)