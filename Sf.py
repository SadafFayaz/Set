set=set()
a=int(input(""))

b=float(input(""))
set.add(a)
set.add(b)
tup=((int,a),(float,b))
set.add(tup)
print(set)