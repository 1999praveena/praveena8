s=str(input())
s.split(" ")
c=1
for i in s.split(" "):
     if c==1:
         print(i[0].upper()+""+i[1:len(i)], end=" ")
     else:
         print(i)
