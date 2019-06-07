I=int(input())
s=str(I)
q=0
for i in range(0,len(s)):
    if int(s[i:i+2])<26 and len(str(int(s[i:i+2])))==2:
        q+=1
if q==2:
    print(q+q//2)
else:
    print(q+q//2+1)
