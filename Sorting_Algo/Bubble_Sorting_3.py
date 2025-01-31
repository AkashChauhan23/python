# Optimize Bubble Sort:
# If no swaps are made in a pass, Bubble Sort can stop early. Implement an optimized version for this input:
op = [1, 2, 3, 4, 5]

l = [2, 1, 3, 4, 5]
for i in range(len(l)):
    for j in range(0, len(l)-1):
        # If no swaps are made in a pass
        if l == op:
            break
        else:
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
            print('Counter')
    print("llll", l)
print("The list after the second pass will be ", l)