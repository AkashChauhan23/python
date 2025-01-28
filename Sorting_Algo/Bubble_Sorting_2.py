# Identify Sorted Steps:
# What will the list look like after the second pass of Bubble Sort?
l = [10, 7, 3, 8, 5]
n = 2
for i in range(n):
    for j in range(0, len(l)-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print("The list after the second pass will be ", l)