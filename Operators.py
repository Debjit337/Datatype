'''
Operators=
1. Arithmatic Op (Math signs) + - / * // % **
2. Assigment Op (=)
3. Comparison Op (< > ! ==)
4. Logical Op (And Or Not)
5. Identity Op (is/is not)
6. Membership Op (in/not in)
7. Bitwise Op (True/False)

'''

# 1. Arithmatic Op (Math ke sare signs):

# a ye ek variabel hai. 10 ye value hai interger type jiko hamne a variable ke andar store kiya hia.
a = 10
b = 20

mysum = a + b

print('\nMysum: ', mysum)

print('\nSub: ', a - b)

print('\nMul: ', a * b)

print('\nDiv: ', b / a)

print('\nModules: ', a % b)

print('\nExponestial: ', 10 ** 2)

print('\nFloor: ', 20 // 2)


# 2. Assigment Op (=):

a = 10
b = 20

# b = b + a
b += a
print('\nb: ', b)

# 3. Comparison Op (< > ! ==):

a = 10
b = 20

print('\nequal to: ', a == b)
print('\nnot equal: ', a != b)
print('\ngreater: ', a > b)
print('\ngreaten equal to: ', a >= b)
print('\nlessten: ', a < b)
print('\nless then equal to: ', a <= b)


# 4. Logical Op (and or not):

print('\nand: ', a < b and not(a > b))
print('\nor: ', a < b or b < a)
print('\nnot: ', not(a > b))

# 5. Identity Op (is, is not):

c = 10
d = 10

print('\nEqual: ', c == d)
print('\nIs: ', c is d)
print('\nIs not: ', c is not d)

# 6. Membership Op (in, not in):

myclass = [1,2,3,4,5,6]

print('\nIn: ', 3 in myclass)
print('\nnot in: ', 31 not in myclass)
