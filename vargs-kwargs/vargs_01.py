# variable length arguments

def add(farg, *vargs):

    print("Formal argument: ", farg)

    sum = 0

    for i in vargs:
        sum += i
    print("Sum of all supplied numbers is: ", sum)

# call 
add(1, 2, 3)            
add(11, 2, 3, 44, 10)            