mytuple= ('A','B','C','D','E')
print(mytuple[3])
print(mytuple[1:3])
print(mytuple[-3:-1])

Coming=('A','B','C')
Notcoming=('D','E','F')

Changes=list(Coming)
Changes.append('D')
Changes.append('E')
print(Changes)
Coming=tuple(Changes)
print(Coming)

Changes=list(Coming)
Changes.remove('C')
Changes.remove('B')
print(Changes)
Coming=tuple(Changes)
print(Coming)

invitationcard='''

--------------------------------------------
                  Coming
--------------------------------------------
1.{}
2.{}
3.{}
'''.format(mytuple[0],mytuple[3],mytuple[4])
print(invitationcard)

invitationcard='''

--------------------------------------------
                Not Coming 
--------------------------------------------
1.{}
2.{}
3.{}
'''.format(mytuple[1],mytuple[2],mytuple[3])
print(invitationcard)