# Same name for both local and global variables


a=1

def myfucntion():

    a = 2
    x = globals()['a'] # global variables are stored as dictionary in the globals()

    print("Global var a = ", x)
    print("Local var a = ", a)

myfucntion()
print("Global var a = ", a)    