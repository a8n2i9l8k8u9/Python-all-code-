#Write a python program to check weather a specified value is contained in a

ls=['1','3','5','4','55','44','66']
num=int(input("Enter a number which you want to search:"))
for i in range(len(ls)):
    if(num in ls):
        print("True")
    else:
        print("False")
