KB=input()
KB=int(KB)
YZ=[]
for j in range(0,KB):  
    n1=input()
    YZ.append(n1)
f1=[]
for j in zip(*YZ):
    if j.count(j[0])==len(j): 
        f1.append(j[0])
    else:
        break
print(''.join(f1))

