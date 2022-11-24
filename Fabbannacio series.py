n=int(input("Enter any number:->"))
t1=0
t2=1
for(int i=1;i<=n;i++)
t1=t2
t2=nextTerm
nextTerm=t1+t2
print("Fabbinaco series","=",nextTerm)
