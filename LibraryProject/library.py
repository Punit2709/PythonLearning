
class Library:
    def __init__(self, listOfBooks) :
        self.book = listOfBooks
    def displayAvailbleBooks(self):
        print('The Books Present In This Library are :- ')
        for book in self.book :
            print(" * " + book)

    def borrowBook(self, name) :
        if(name in self.book):
            print( name + " is Borrowed by U")
            self.book.remove(name)
            return True
        else:
            print(name + " is Not Available, Check After Some Time.")
            return False
        
    def returnBook(self, name):
        self.book.append(name)
        print("Thanks For Returning Book.")

        

class Student:
    def request(self):
        self.book = input("Enter The Name :- ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter The Name :- ")
        return self.book

if __name__ == "__main__" :

    MJLibarary = Library(["Algo", "DSA","SelfHelp", "History", "Science", "Computer", "Commerce" ])
    student = Student()
    # MJLibarary.displayAvailbleBooks()
    # print()
    # MJLibarary.borrowBook("Algo")
    # MJLibarary.borrowBook("OS")
    # MJLibarary.displayAvailbleBooks()
    # print()
    # MJLibarary.returnBook("Algo")
    # MJLibarary.displayAvailbleBooks()
    # print()


    while(True):
        welcomeMsg = '''❤ ❤  You are Welcome In Library, Read and Grow ❤ ❤ \n
    Please Choose The Option :
    1. Check For Available Book
    2. request For Book
    3. Return The Book
    4. Exit The Book  
'''
        print(welcomeMsg)
        a = int( input("Enter The Choice :- "))
        
        if a == 1 :
            MJLibarary.displayAvailbleBooks()
            print("\n\n")
        
        elif a== 2 :
            MJLibarary.borrowBook(student.returnBook())
            print("\n\n")
        
        elif a == 3 :
            MJLibarary.returnBook(student.returnBook())
            print("\n\n")
        
        elif a == 4 : 
            print("Thanks For Visiting... Come Again")
            exit()
        
        else:
            print("This Choice is Not Available 👍 👍")
            print("\n\n")


        