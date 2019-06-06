p=int(input())
q=[int(q) for q in input().split()]
r=[]
for i in range(0,p-1):
  for jin range(j+1,p):
    if(q[i]==q[j]):
      r.append(q[i])
s=list(set(sorted(r)))
if len(s)==0:
    print("unique")
else:
    for i in range(0,len(s)):
        print(s[i],end=" ")
