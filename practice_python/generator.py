def generator(n):
    for i in range(n):
        yield i

obj = generator(10)
print([data for data in obj])

