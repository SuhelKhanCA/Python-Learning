# subset 1 contains all the elements less than elements in the second subset 2

list = input("Enter even no of Distinct integers : ").split()

org_set = {x for x in list}

print("Original set: ", org_set)

list2 = sorted(list)

print(list)
subset_1 = set()

for i in range(0, len(list)//2):
    subset_1.add(list[i])

print("First subset: ", subset_1)



subset_2 = set()
for i in range(len(list2)//2, len(list2)):
    subset_2.add(list[i])


print("Second subset: ", subset_2)    