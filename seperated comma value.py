'''Write a program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
sample data:3, 5, 7, 23
List:['3','5','7','23']
Tuple:('3','5','7','23')'''
values=input("Input some comma seprated numbers:")
list=values.split(" , ")
tuple=tuple(ls)
print('List : ',list)
print('Tuple : ',tuple)

