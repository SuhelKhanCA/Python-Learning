

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(args) for arg in args)
        kwargs_value = ', '.join(f'{key}={value}' for key, value in kwargs.items())
        print(f"Name of function : {func.__name__} with args : {args_value} and kwargs: {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper


@debug
def hello():
    print("Hello, World!")
hello()


@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Sonu", greeting="Hello")    