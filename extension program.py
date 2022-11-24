'''write a python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java'''

filename=input("Enter the string with extension:")
f_extns = filename.split(".")
if(".") not in filename:
    print("There is no extension file")
else:
    print("The extension of the file is : " +repr(f_extns[-1]))
