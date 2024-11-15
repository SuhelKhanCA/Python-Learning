# calculate the No of words and chars

file = open("file.txt", "r+")

new_list = []
lines = file.readlines() # this is list of lines from the file

print(lines)
str = ""
for i in lines:
   str = str + i
print(str)

# ls = str.split('\n')
ls = str.split()

print(ls)

print("Number of words : ", len(ls))
c_c = 0

for i in ls:
   c_c = c_c + len(i)

print("Numbers of chars: ", c_c)   