class add:
    def __init__(self,n):
        self.x=n
    def res(self):
        return self.x*123
a=int(input("Enter a number:"))
obj=add(a)
ans=obj.res()
print("Answer : " ,ans)





''' Using Class 
class add:
    def res(self,n):
        return(n*123)
a=int(input("Enter a number:"))
obj=add()
ans=obj.res(a)
print("Answer : ",ans)'''
