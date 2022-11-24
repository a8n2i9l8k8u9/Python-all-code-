#Counting the number of even and odd elements in an array.
list=[2,4,5,61,7]
even=0
odd=0
for i in list:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("Even: ",even , "\tODD: ",odd)
