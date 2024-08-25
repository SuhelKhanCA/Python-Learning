class Student:
    college_name = "ABC College"
    name = "Anonymous"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Karan", 97)
print(s1.name, s1.marks)
print(s1.college_name)

s2 = Student("Arjun", 92)
print(s2.name, s2.marks)
print(Student.college_name)                

s3 = Student("Shweta", 66)
print(s3.name)