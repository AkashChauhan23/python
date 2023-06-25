import traceback

print("Enter a string >>> ")
string = str(input())

def reverse_fn(string):
    try:
        return string[::-1]
    except Exception as e:
        return ("Exception occured >>> ", traceback.format_exc())

obj = reverse_fn(string)
print(obj)
