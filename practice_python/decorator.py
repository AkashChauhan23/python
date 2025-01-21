# def decorator(myfunc):
#     def wrapper():
#         fun = myfunc()
#         return f'{fun} Thank you for visiting'
#     return wrapper

# @decorator
# def greets():
#     return "Welcome to my website..."

# print(greets())




def mydecor(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
    def decorator(myfunc):
        def wrapper():
            fun = myfunc()
            return f'{fun} Thank you for visiting'
        return wrapper
    return decorator

@mydecor('akash', 100, 200, id = 1234)
def greets():
    return "Welcome to my website..."

print(greets())


