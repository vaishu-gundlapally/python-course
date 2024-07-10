a1  =   [2,3,5,3]
def mul(a1):
    for i in range(len(a1)):
        a1[i]*=2
    return a1
print(mul(a1))

#using lambda for printing each values
b=lambda a1:[print((i*2) for i in a1)]
print(b)

# lambda function example:
a=lambda a,b:a*b
print(a(10,20))

# using map function:
b1=[1,2,3,4]
b1=list(map(lambda x:x*2,b1))
print(b1)

# if want to return list converting to integer:
a3=["1","2","3"]
l=list(map(int,a3))
print(l)

#reduce function

from functools import reduce
x1=[1,2,5,7]
p=reduce(lambda a,b:a+b,x1)
for i in range(len(p)):
    print(p[i])
print(p)

#filter function 

empno=[101,102,103]
ename=["abc","bcd","def","vai"]
emp=list(zip(empno,ename))
e=dict(zip(empno,ename))
print(emp)
print(e)