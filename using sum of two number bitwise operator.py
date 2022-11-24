n=2
z=6
while(z!=0):
    n1=n&z
    n=n^z
    z=n1<<1
print("The sum of two number : ",n1)
