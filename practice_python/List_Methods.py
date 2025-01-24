lst = ['a', 'b', 'c', 'd', 'a', ['aa', 'bb'], 1, 2, 3, 9, ['aa', 'bb']]
print("Givan List >>>> ", lst)

lst.append('z')
print("List after appending z >>>> ", lst)

lst1 = lst.copy()
print("List1 copying from list >>>> ", lst1)

print("Return count of ['aa', 'bb'] from list >>>> ", lst.count(['aa', 'bb']))


lst2 = ['aaa', 'bbb', 'ccc']
lst.extend(lst2)
print("Return the Extended list >>>> ", lst)


print("List updated >>>> ", lst)


print("Return the index of element from list >>>> ", lst.index(['aa', 'bb']))


lst.insert(2, 2000)
print("List after insertion >>>>> ", lst)

lst.pop()
print("List after pop >>>>> ", lst)

lst.pop(-2)
print("List after pop >>>>> ", lst)

lst.remove(['aa', 'bb'])
print("List after remove >>>>> ", lst)

lst.reverse()
print("List reversed >>>>> ", lst)

lst.clear()
print("Cleared List >>>>> ", lst)

lst = [1,23423,42,1,34,34,221,13445,1323]
lst.sort()
print("Sorted List >>>>> ", lst)


