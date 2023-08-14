from functools import reduce

lst = [1,2,9,-11,4,5]
# lst = [-10,-9,0,2,3,8]

sort = sorted(lst)
result1 = reduce(lambda x, y: x*y, sort[-3:])

res1 = reduce(lambda x, y: x*y, sort[:2])
result2 = res1*sort[-1]

if result1 > result2:
    print(result1)
else:
    print(result2)