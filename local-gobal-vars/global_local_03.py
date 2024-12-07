# Use of 'global' keywords

a=1

def myfunction():

    global a

    print("Global a = ", a)

    a=2 # this will change the var 'a'
    print("local a = ", a)

myfunction()

print("a = ", a)