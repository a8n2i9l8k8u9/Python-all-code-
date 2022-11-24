#write a code to count total +ve and -ve enteries from a
# a) List b)Tuple

l=[2,-4,9,7,-6,3,-2,10,99,-89,-10]
pos=0
neg=0
for i in l:
    if i>0:
        pos=pos+1
    else:
        neg=neg+1
print("Total number of +ve is",pos,"and -ve is ",neg)
