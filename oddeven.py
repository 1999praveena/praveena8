PQ=int(input())
a = [int(x) for x in input().split()]
for i in range(0,PQ):
    if i<PQ-1:
        k=' '
    else:
        k=''
    if i%2==0:
        if a[i]%2!=0:
            print(a[i],end=k)
    elif i%2!=0:
        if a[i]%2==0:
            print(a[i],end=k)
