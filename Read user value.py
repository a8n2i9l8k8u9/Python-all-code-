#write a code to read the value from user without using for loop.
print("Enter the number:")
inp = tuple(map(int,input().split()))
c=0
for i in range(len(inp)):
    f=0
    for j in range(2,inp[i]):
        if(inp[i] % j==0):
            f=1;
            break;
    if(f==0):
        c=c+1
    if(c==2):
        break;
if(c==2):
    print("Index for second prime:",i)
