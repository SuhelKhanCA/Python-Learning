# to calculate relative prime of user supplied integer

num = int(input("Enter an integer: "))


def gcd(num1, num2):

    while num1 != 0:        
        r = num2 % num1
        num2 = num1
        num1 = r
        
    return num2

for i in range(1, num):

    if gcd(i, num) == 1:
        print(i, end=" ")        