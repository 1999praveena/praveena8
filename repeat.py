Q=int(input())
M=list(map(int,input().split()))
for i in M:
    if M.count(i)>1:
       print(i)
       break
else:
    print("unique")
