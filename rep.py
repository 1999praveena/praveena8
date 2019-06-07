AM=input()
V=list(AM)
dict = {i:V.count(i) for i in V}
m = max(dict, key=dict.get)  
print(m)
