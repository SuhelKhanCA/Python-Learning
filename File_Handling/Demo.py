f = open("C:\\Users\\suhel\\Desktop\\Pyhton-chai\\File_Handling\\file.txt", 'a')

f.write("This is new added line")

f.close()

f = open("C:\\Users\\suhel\\Desktop\\Pyhton-chai\\File_Handling\\file.txt", 'r')

print(f.read())