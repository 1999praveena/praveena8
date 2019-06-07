u,v=input().split()
c=0
for i in range(len(u)):
    if u[i]==v[i]:
        continue
    else:
        c=c+1
if c==1:
    print("yes")
else:
    print("no")
