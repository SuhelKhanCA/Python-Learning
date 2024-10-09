# Classes in Python are dynammically typed

class Example:
    def __init__(self, value):
        self.value = value

object = Example(42) # value is an integer
print(object.value)
object = Example("Hello") # reassigned to a string
print(object.value)

