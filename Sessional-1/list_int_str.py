# Add all the integers value concatenate string from a list of str&int

list = ["Aligarh", 10, "Msulim", 54, 90, "University"]

sum = 0
new_str = ''

for i in list:
    if isinstance(i, int):
        sum += int(i)
    if isinstance(i, str):
        new_str += i

print("Sum is: ", sum)        
print("New string is: ", new_str)        