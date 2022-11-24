#Write a program to give a discount of
#10% if the total bill amount exceeds 1000.
num=int(input("Enter the bill you have consume:"))
if(num>1000):
    s=10/100*num
    print("you have to pay:",s)
    num=num-s
else:
    print("you have not allowed to benifite")
