# Creating dynamic class and object
MyClass = type("MyClass", (), {"attribute1": 1}) # type() creates class at runtime
obj = MyClass()

print(obj.attribute1)