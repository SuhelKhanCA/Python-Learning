list = [2, 6, 9, 7]

index = 3

target = 33

list.append(None)
print(list)

i = len(list) -1
while i >=index:
    list[i] = list[i-1]
    i -= 1
list[index] = target
print(list)    