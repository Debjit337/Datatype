Data={'name' : 'Debjit','mobile' : '789456123','course' : 'Python','address' : 'Kalna'}

profile=''' 
-------------------------------
        {name}'s Profile
-------------------------------
Name: {name}
Mobile: {mobile}
Course: {course}
Address: {address}
-------------------------------
'''.format(name=Data['name'],mobile=Data['mobile'],course=Data['course'],address=Data['address'])
print(profile)
data = {
    'nikhil' : {
        'name' : 'Nikhil',
        'mobile' : 987987987,
        'course' : 'Python',
        'address': 'Delhi'
    },
    'debjit' : {
        'name' : 'Debjit',
        'mobile' : 9987987979,
        'course' : 'Python',
        'address': 'Kalna'
    }
}
print(data)
print('\nName:',data['debjit'] ['name'])
print('\nMobile:',data['debjit'] ['mobile'])
print('\nCourse:',data['debjit'] ['course'])
print('\nAddress:',data['debjit'] ['address'])

#fromkeys
x=('A','B','C','D')
y=5
Thisdict=dict.fromkeys(x,y)
print(Thisdict)
