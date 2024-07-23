
class Employee:
    
    increment = 1.5
    empno = 0
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.empno +=  1
    
    def getData(self):
        print(self.fname + " " + self.lname + " "+ str(self.salary))

    def incrementSalary(self):
        self.salary = int(self.increment * self.salary )

    # class Method take Class an an Argument
    @classmethod
    def changeIncrement(cls,amount):
        cls.increment = amount 
    
    @classmethod
    def fromString(cls,str):
        fname,lname,salary = str.split("-")
        salary = int(salary)
        return cls(fname,lname,salary)
    
    @staticmethod
    def isClose(day):
        if("Sunday" == day):
            print("yes")
        else:
            print("No")

    def __str__(self):
        return "Employee Class Is Impoerted"
    
    def __repr__(self):
        return "Employee Class Is Impoerted repr"
    
    def __call__(self):
        return "Are You Calling Employee"


class Devloper(Employee):
    def __init__(self, fname, lname, salary,progLang,exp):
        super().__init__(fname, lname, salary)
        self.progLang = progLang
        self.exp = exp

    def incrementSalary(self):
        self.salary = int(self.salary * (self.increment + 0.2))
    
    def getData(self):
        print(self.fname + " " + self.lname + " "+ str(self.salary))
        print("My exp " + str(self.exp) + " Lang " + self.progLang)

    def __len__(self):
        return ( len(self.fname) + len(self.lname) )

    def __str__(self):
        return "Devloper Class Is Impoerted"
    
    def __call__(self):
        return "Are You Calling Devloper"

if __name__== "__main__":
    # putin = Employee("Putin","Russiawala",3500)
    # putin.getData()
    # putin.incrementSalary()
    # putin.getData()
    # print(putin.empno)

    # print(putin.__dict__) 
    # # print(Employee.__dict__) 


    # #when i will create new Employee empno will increase 
    # punit = Employee("Punit", "Prajapati", 2500)
    # print(putin.empno)  

    # Employee.changeIncrement(1.1) 
    # punit.incrementSalary()
    # punit.getData()  

    # elvish = Employee.fromString("Elvish-Yadav-3500")
    # elvish.getData()
    # elvish.incrementSalary()
    # elvish.getData()


    # Employee.isClose("Sunday")
    # elvish.isClose("Sunday")
    # punit.isClose("Sunday")


    dev = Devloper("Dev","HEllo", 2500,"Python", 3)
    dev.getData()


    # learning Magic/Dunder Methods
    # called Magic methos cause :-  define as __len__ but invoke as len(object)
    print(len(dev))