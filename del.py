from itertools import combinations
z,a=map(int,input().split())
b=len(str(z))
x=list(combinations(str(z),b-a))
x=(sorted(x))
y="".join(x[0])
print(y)
