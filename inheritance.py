'''Write a python program General class contain
Name of the student,roll,aadhar,mobile
second class name is Acadmic which contain CGP 10th and 12th the
third class contain library book issue,return date and fine .'''
class General:
    def fun1(self,name,roll_no,aadhar_no,mobile_no):
        self.name=name
        self.roll=roll_no
        self.aadhar=aadhar_no
        self.mobile=mobile_no
class Acadmeic(General):
    def fun2(self,tenth_cgp,twelfth_cgp):
        self.tenth=tenth_cgp
        self.twelfth=twelfth_cgp
class Library(General,Acadmeic):
    def fun3(self,return_book,issue_book,date,fine):
        self.retur=return_book
        self.issue=issue_book
        self.date=date
        self.fine=fine
d=Library(self)
d.fun3()
d.fun1()
d.fun2()
print("Name:",d.fun1(Anil),"Roll no:", d.fun1(12),"Aadhar no:",d.fun1(762810573092),"Mobile no:",d.fun1(8298897353))



