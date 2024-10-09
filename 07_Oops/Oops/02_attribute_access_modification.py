# we can add, modify or delete attibute even outside the class
class Person:
    pass

person = Person()

person.name = "Suhel" # adding attribute
print(person.name)
person.age = 24
print(person.age)

# Deleting the 'age' attribute from outside the class
del person.age

# Trying to access 'age' after deletion will raise an AttributeError
# print(person.age)  # This will raise an AttributeError: 'Person' object has no attribute 'age'