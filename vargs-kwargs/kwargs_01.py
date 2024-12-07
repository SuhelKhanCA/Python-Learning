# Demo example for keyword arguments

def display(farg, **kwargs):

    print("Formal argument: ", farg)

    for key, val in kwargs.items():
        print("key : {} and value : {}".format(key, val))


display(5, rno=10)

display(10, rno=10, name="Prakash")