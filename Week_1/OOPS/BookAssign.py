from abc import ABC, abstractmethod

class LibraryUser(ABC):

    def registerAccount(self):
        pass  
        
    def requestBook(self):
        pass

class KidUsers(LibraryUser):
    def __init__(self, age, bookType):
        self.age = age
        self.bookType = bookType

    def registerAccount(self):
        if self.age < 12:
            print("\nYou have successfully registered under a Kids Account")
        else:
            print("\nSorry, Age must be less than 12 to register as a kid")

    
    def requestBook(self):
        if self.bookType.lower() == "kids":
            print("\nBook Issued successfully, please return the book within 10 days")
        else:
            print("\nOops, you are allowed to take only kids books")

class AdultUser(LibraryUser):
    def __init__(self, age, bookType):
        self.age = age
        self.bookType = bookType

    def registerAccount(self):
        if self.age > 12:
            print("\nYou have successfully registered under an Adult Account")
        else:
            print("\nSorry, Age must be greater than 12 to register as an adult")

    def requestBook(self):
        if self.bookType.lower() == "Fiction":
            print("\nBook Issued successfully, please return the book within 7 days")
        else:
            print("\nOops, you are allowed to take only adult Fiction books")

if __name__ == "__main__":
    
    print("TEST CASE 1")
    print("--- Kid User ---")
    
    kid1 = KidUsers(10, "Kids")
    kid1.registerAccount()  
    kid1.requestBook()      
    
    kid1.age = 18
    kid1.bookType = "Fiction"
    kid1.registerAccount()  
    kid1.requestBook()          
    
    print("TEST CASE 2")
    print("--- Adult User ---")
    
    adult1 = AdultUser(5, "Kids")
    adult1.registerAccount()  
    adult1.requestBook()      
    
    adult1.age = 23
    adult1.bookType = "Fiction"
    adult1.registerAccount()  
    adult1.requestBook()      
