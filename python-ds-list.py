

# A = [121,23,1,21,21,2,12,12,12,1,2,12,1,2,12]
# B = A[:]

# print(A)
# B.sort()
# print(A)
# print(B)

# print([x**2 for x in range(10)])

# if 1 not in A:
#     print("1 is indeed in A")
# else:
#     print("You fool")

# print(A[:])
# print(A[3:-2])

# c = ["Vikas"] * 3
# print(c)

# d = A + c
# print(d)

A = [1,2,3,4,5]
A.insert(0,-1)
print(A)


A[2:2] = [-1,-2]
print(A)


del A[2]
del A[2]

print(A)

A = [1,2,3,4,5,5]

# nummber of time an element is present
print(A.count(5))
A.reverse()
print(A)

A.remove(5)
print(A)


c = A.pop(-1)
print(c)
print(A)






