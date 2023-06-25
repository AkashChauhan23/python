print("Enter the starting value eg. 1 >>> ")
start = int(input())
print("Enter the last number eg. 7 >>> " )
n = int(input())

for i in range(start,start+n):
    for j in range(1,i-1):
        print(i, end=" ")
    print()
for i in range(start+n-1,start-1,-1):
    for k in range(i-1,1,-1):
        print(i, end=" ")
    print()