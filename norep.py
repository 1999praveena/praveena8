XY=int(input())
Z=[]
Z=input().split()
for i in range(len(Z)):
    if Z.count(Z[i])==1:
        print(Z[i])
        break

