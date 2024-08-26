list = [2, 6, 9, 4, 13, 14, 19]

index = 3

i = index

while i < len(list) - 1:
    list[i] = list[i + 1]
    i += 1

print(len(list))
print(list)    
list.pop()

print(len(list))
print(list)