# subset 1 contains all even elemnts and subset 2 contains all the odd elements

list = input("Enter even no of Distinct integers : ").split()

org_set = {x for x in list}

print("Original set: ", org_set)

list2 = sorted(list)

print("Sorted list: ", list2)

subset_1 = set()
subset_2 = set()

for i in list2:
    if int(i) % 2 == 0:
        subset_1.add(i)
    else:
        subset_2.add(i)

print("First subset: ", subset_1)

print("Second subset: ", subset_2)    