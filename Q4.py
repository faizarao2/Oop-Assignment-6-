# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) 
# that allows changing the bank name. Show that it affects all instances.




class Bank:
    bank_name = "Meezan Bank"   #class variable
    
    def __init__(self ):
        Bank.bank_name = Bank.bank_name   
        print("Bank Name : ", Bank.bank_name)   
        try:
            new_name = input("Enter new bank_name: ")
            if not new_name.isalpha():
                raise ValueError
        except ValueError:    
            print("Invalid input. Please enter a string.")
        else:
           Bank.change_bank_name(new_name)


    @classmethod    #class method
    def change_bank_name(cls , name):
        cls.bank_name = name
        print("Bank Name Changed to : ", cls.bank_name)



new_bank_name = Bank()