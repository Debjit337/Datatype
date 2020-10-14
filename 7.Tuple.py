'''
Python Tuple:
1. Tuple nonchange hai, aur list changeable hai. iska systax ()
2. Tuple me values na change kar pane ki wajah se isme is tarike ke koi bhi methods nahi milte hai.
3. Single value wale tuple me value ke sath ek comma dena jaruri hai otherwiese wo ek stirng ya int value hi hoga.
4. List ke jaise hi tuple me same to same slicing follow hota hai. Ye posstive and negative dono me hota hia.
Tuple me total 2 mehtods milte hain:
Note: Example tuple - newtuple = (11,22,33,33)
1. count(): Same list count() method jaisa hi hai. Is ke use se tuple me exist dublicate values ko count kiya jata hai. Example: newtuple.count(33)
2. index(): Same list index jaisa hi hai. Tuple me kisi bhi value ka index posstion find karne ke liye index method ka use kiya jata hai. Example: newtuple.index(33)
'''

# new tuple
mytuple = ('nikhil','debjit','sushil','debjit','python','debjit')
print('\nmytuple type: ', type(mytuple))
print('\nmytuple: ', mytuple)

# related mehtods
print('\nIndex of python: ', mytuple.index('python'))
print('\nCount debjit: ', mytuple.count('debjit'))

# slicing
print('\nget index vlaue: ', mytuple[2])
print('\nOnly start: ', mytuple[2:])

# find length
print('\nFind mytuple length: ', len(mytuple))
print('\nFInd nikhil length: ', len('nikhil'))

# convert tuple into list for change or update
getTupleDataInList = list(mytuple) 
print('\nType getTupleDataInList: ', type(getTupleDataInList))

# add 2 more canditates
getTupleDataInList.append('Raju')
getTupleDataInList.append('Reena')

# add bunch of students
newstudents = ['Hari','Ram','Seema','Pehu']
getTupleDataInList.extend(newstudents)

print('\ngetTupleDataInList: ', getTupleDataInList)
print('\nGet last index: ', getTupleDataInList[-1])

# change list into tuple again
mytuple = tuple(getTupleDataInList)
print('\nCheck type of mytuple: ', type(mytuple))

print('\nmytuple: ', mytuple[0])