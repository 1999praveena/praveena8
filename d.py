QR=int(input())
P=[int(i) for i in input().split()]
s=0
for i in range(QR):
	for j in range(i):
		if P[j]<P[i]:
			s+=P[j]
print(s)
