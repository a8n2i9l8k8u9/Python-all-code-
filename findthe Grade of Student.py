math=int(input("Enter math marks:->"))
english=int(input("Enter english marks:->"))
phy=int(input("Enter phy marks:->"))
che=int(input("Enter che marks:->"))
hindi=int(input("Enter hidni marks:->"))
avg=(math+english+phy+che+hindi)/5
if(avg>=90):
    print("Grade O")
if(avg>=60)and (avg<90):
    print("Grade A")
if(avg>=50)and (avg<60):
    print("Grade B")
if(avg>=35)and (avg<50):
    print("Grade C")

else:
    print("Fail")

    
