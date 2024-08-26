import sys

args = sys.argv[1:]

sum = 0 # sum of only even numbers given
for i in args:
    x = int(i)
    if x % 2 == 0:
        sum += x

print("Sum = : ", sum)        