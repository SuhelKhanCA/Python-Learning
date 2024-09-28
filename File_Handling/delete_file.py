# Deleting a file in python

import os

if os.path.exists("C:\\Users\\suhel\\Desktop\\Pyhton-chai\\File_Handling\\file.txt"):
    os.remove("C:\\Users\\suhel\\Desktop\\Pyhton-chai\\File_Handling\\file.txt")

else:
    print("File does not exists !") 

# Deleting a folder
os.rmdir("C:\\Users\\suhel\\Desktop\\Pyhton-chai\\File_Handling\\del")