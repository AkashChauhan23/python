# print([ data for data in generator(5) if data % 2 == 0])
print([ data if data % 2 == 0 else 'NA' for data in range(5) ])


print({ i:i*i for i in range(5) })