# local variable in a function

def myfunction():
    a=1
    a+=1
    print(a)


# a check for exp

print(type(myfunction))

myfunction()

#print(a) # this will cause an error --> NameError: name 'a' is not defined