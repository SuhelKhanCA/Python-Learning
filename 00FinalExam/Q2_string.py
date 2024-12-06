# character having maximum instance

str1 = "This is aaa string"

d1 = {c:0 for c in str1}
d2 = {v:0 for v in "AEIOUaeiou"}

for ch in str1:
    if ch in d1:
        d1[ch] += 1
    if ch in d2:
        d2[ch] += 1


print(d1)
print(d2)

key = ""
val = -1

for i, j in d2.items():
    if d2[i] > val:
        key = i
        val = j

print(key, val)        

# Find the characters with the maximum frequency
max_chars = []
max_val = -1

for char, freq in d2.items():
    if freq > max_val:
        max_chars = [char]
        max_val = freq
    elif freq == max_val and freq > 0:
        max_chars.append(char)

print("Characters with maximum frequency:", max_chars)
print("Maximum frequency:", max_val)
