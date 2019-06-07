W,t=map(str,input().split())
c=0
if len(W)>len(t):
  W,t=t,W
i=0
while i<len(W):
  c+=(ord(t[i])-ord(W[i]))
  i+=1
for i in range(i,len(t)):
  c+=ord(t[i])-ord('a')+1
print(c)
