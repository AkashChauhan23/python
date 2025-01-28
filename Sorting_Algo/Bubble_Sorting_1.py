l = [9, 5, 2, 7, 4]
for i in range(len(l)):
    for j in range(0,len(l)-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
        print(f"-- {i} - {j}", l)
    print('============')
print("Sorted list is : ", l)