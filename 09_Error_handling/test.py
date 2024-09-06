file = open('youtube.txt', 'w')

try:
    file.write("Chair aur code")
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write("Chair aur python")