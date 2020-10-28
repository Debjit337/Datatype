'''
Lambda Function ke bare me:
1. Ye ek anonymous function hai.
2. Lambda function me hum multiple arguemts de sakte hain. But iss fucntion ke andar kewal single expression diya ja sakta hai.
Lambda fucntion Syntax:
lambda numberOfArguments : your expression
'''

# user define function
def add2numbers(a, b):
    return a + b
    
# fucntion call
add = add2numbers(30, 50)
print('\nUser define add funciton: ', add)


# lambda function define
lambda_add = lambda a, b : a + b

# call lambda function
answer = lambda_add(30, 40)
print('\nLambda function answer: ', answer)

# lambada in function
def abc(a, b):
    return lambda c, d : a + b + c + d

# user define fucntion call
myvalues = abc(10, 20)

# myvlaues lambda arguemt pass kar raha hai
myanswer = myvalues(50, 100)
print('\nmyanswer: ', myanswer)
