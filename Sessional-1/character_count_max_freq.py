# Program to count characters frequency and max frq

my_string = input("Enter a String: ")

my_dict = dict()

for ch in my_string:
    if ch in my_dict:
        my_dict[ch] += 1
    elif ch != ' ':
        my_dict[ch] = 1

print(my_dict)


ans = -1
val = ''
for key in my_dict:
    if my_dict[key] > ans:
        ans = my_dict[key]
        val = key

print(f"Character with max frequency is: {val} and frequency is {ans}")
