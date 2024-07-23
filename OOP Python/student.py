class student:
    def __init__(self,rollno, name ):
        self.name = name
        self.rollno = rollno
    
    def __str__(self):
        return f"{self.name}{self.rollno}"

    def getData(self):
        print("My name is :- " + self.name +" and Roll No. :- " + str(self.rollno))

stud = student(1, "Punit")
stud.getData()

# we can modify the object
stud.name = "Jay"
stud.getData()

# delete the Object
del stud

#  class defination can't be empty so atleast use PASS keyword
class myClass:
    pass
