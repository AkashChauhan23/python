inp={"set1":['1','67','93','58'],
    "set2":['6','671','83','587'],
    "set3":['-1','6766','873','5845'],
    "set4":['8','6787','8365','58549'],
    "set5":['90','67900','83434','5832'],
    "set6":['45','675656','8312','58312']
}

l = len(inp['set1'])
lst = []
for i in range(l):
    temp = 0
    for k, v in inp.items():
        temp+=int(inp[k][i])
    lst.append(temp)
print(max(lst))
