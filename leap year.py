n=int(input("Enter the number:->"))
if(n%4!=0):
    print("Given number is not leap year.")
elif(n%4==0)and(n%100!=0):
    print("Given number is  leap year.")
elif(n%4==0)and(n%100==0)and(n%400==0):
    print("Given number is leap year.")
else:
    print("Given number is not leap year.")
###Logic:
# if a year is not divisible by 4, its not a leap year.
# If a year is divisible by 4 and not divisible by 100, it’s a leap year.
# If a year is divisible by 4 and 100 then it should be divisible by 400
#to be a leap year
