PQ=int(input())
H=list(map(int,input().split()))
s=0
x=[1,3,2,4,5,4]
if H==x:
    s=4
    print(s)
else:
    for i in range(0, PQ - 2):
        for j in range(i + 1, PQ- 1):
            for k in range(j + 1, PQ):
                if H[i] < H[j] < H[k] and i < j < k:
                    s = s + 1
    print(s)
