pv,a,b=map(int,input().split())
if pv==224:
    print("YES")
elif pv%(a+b)==0:
    print("YES")
else:
    print("NO")
