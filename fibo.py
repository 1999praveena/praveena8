q=int(input())
n1 = 1
n2 = 1
c = 0


if q <= 0:
   print(" enter a positive integer")
elif q == 1:
   print("Fibonacci sequence upto",q,":")
   print(n1)
else:
   print("Fibonacci sequence upto",q,":")
   while c< :
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       c += 1
