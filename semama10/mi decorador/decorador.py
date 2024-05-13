from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args ,**kwars):
        print("nates de  llamar a la funcion")
        result =func(*args, **kwars)
        print("despues de llamara a la funcion")
        return result
    return wrapper

@my_decorator
def greet(name):
    """funcion para saludara aleguien"""
    return(f"hola , {name}¡")

greet("JUAN")

print(greet.__name__)
print(greet.__doc__)