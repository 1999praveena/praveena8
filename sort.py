a=list(input())
t=0
for i in range(0,len(a)):
  for j in range(i+1,len(a)):
    if a[i]>a[j]:
      t=a[i]
      a[i]=a[j]
      a[j]=t
  print(a[i],end="")
