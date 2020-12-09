# set intersection--
A = {1, 2, 3, 4, 5, 6}
B = {2, 4, 5, 8, 10, 7}
C = A & B
print(C)

# set union--
A = {1, 2, 3, 4, 5, 6}
B = {2, 4, 5, 8, 10, 7}
D = A | B
print(D)

# A or B uncommon element find out--
A = {1, 2, 3, 4, 5, 6}
B = {2, 4, 5, 8, 10, 7}
F = A ^ B
print(F)

# only uncommon element of A
A = {1, 2, 3, 4, 5, 6}
B = {2, 4, 5, 8, 10, 7}
E = A - B
print(E)

# only uncommon element of B
A = {1, 2, 3, 4, 5, 6}
B = {2, 4, 5, 8, 10, 7}
G = B - A
print(G)
