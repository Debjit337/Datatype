# stirng file 

name = 'Debjit'
print('\nYour name is', name, '. Welcome to Python.')

# use concatation '+' in stirng
info = 'Hi, ' + name
# print(info)
welcomeMessage = 'Welcome to Python Language.'
endMessage = 'Thanks for studing.'

# show welcome message
print(info + '\n' + welcomeMessage + '\n' + endMessage)

# double qoute stirng of single line
name = "\nDebjit"
print(name)

# multiline string ke liye tripal single (''') ya double (""") qoute ka use kar sakte hain.
data = '''
---------------------------------------------------
                    Data
---------------------------------------------------
Your data
Your data
Your data                    
---------------------------------------------------
'''

data = """
---------------------------------------------------
                    Data
---------------------------------------------------
Your data
Your data
Your data                    
---------------------------------------------------
"""
print(data)

# string methos
name = 'Hello Nikhil'
print('\nCheck N: ', name.index('N'))
print('\nCapatilze: ', name.capitalize())
print('\nUpper case: ', name.upper())
print('\nLower case: ', name.lower())

newdata = name.split(' ')
print('\nNew data: ', newdata)
