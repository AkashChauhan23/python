def rangoli(n):
    lst1=list(map(chr,range(97,123)))
    x=lst1[n-1::-1]+lst1[1:n]
    width=len('-'.join(x))
    for i in range(1,n):
        print('-'.join(lst1[n-1:n-i:-1]+lst1[n-i:n]).center(width,'-'))
    for i in range(n,0,-1):
        print('-'.join(lst1[n-1:n-i:-1]+lst1[n-i:n]).center(width,'-'))
rangoli(5)