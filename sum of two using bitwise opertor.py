a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
while(b!=0):
    c=a & b
    a=a^b
    b=c<<1
print("The sum of two number : ",a)
