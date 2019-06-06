o=int(input())
q=list(map(int,input().split()))
q.sort(reverse=True)
for i in range(0,o):
  print(q[i],end="")
