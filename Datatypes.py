'''

keyword:
if,else,for,while,try,except,in,is

Variable:
it can store data of different types.
there are 7 types of datatypes.

1. Text type : str
2. Numeric type : int, float, complex
3. Sequence type : list, tuple, range
4. Mapping type : dict 
5. Set type : set, frozen set
6. Boolean type : true / false
7. Binary type : bytes, bytearray, memoryview

'''
# code
name= 'Python'
print(type(name))

name= 6.666j
print(type(name))

# sequence

# list : []
listval=[1,2.,3,'Hello']
print('listval: ',type(listval))

# tuple : ()
tupleval=(1,2,3,'Hello')
print('tupleval; ',(type(tupleval)))
 
# range 
rangeval= range(6)
print('rangeval: ',type(rangeval))

# dict= key and value mapping
dictval={'name':'Python'}
print('Dictval:',type(dictval))

# set : {}
setval={1,2,3}
print('setval:',type(setval))

# boolean : true/false
booleanval= bool(555)
print('boolbal:',type(booleanval))
