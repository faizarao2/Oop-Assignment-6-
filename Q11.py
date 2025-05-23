# 11. Class Methods
# Assignment:
# # Create a class Book with a class variable total_books. Add a class method increment_book_count()
#  to increase the count when a new book is added.

class Book:
    total_books = 0

    def __init__(self , title :str , author :str , addition :int , price : float):
        self.title = title
        self.author = author 
        self.addition = addition
        self.price = price
        Book.increment_book_count()
        self.display_book()

    

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    def book_info(self):
        return  self.title , self.author , self.price , Book.total_books
      

    def display_book(self):
        print("Total Books in Library: ", Book.total_books)   
        print(f"Book {Book.total_books}:") 
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Addition: ", self.addition)
        print("Price: ", self.price)


book = Book("Python Programming" , "John Doe" , 1 , 29.99)


while True:
    try:
        new_book = input("Do you want to add a book? (yes/no): ")
        if new_book.lower() == "no":
            print("Exiting the program.")
            break

        elif new_book.lower() != "yes":
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
        new = input("Enter new Book Title:")
        Book_author = input("Enter new Book Author:")
        Book_addition = int(input("Enter new Book Addition:"))
        Book_price = float(input("Enter new Book Price:"))

        if not new.isalpha() or not Book_author.isalpha() or Book_addition < 0 or Book_price < 0:
            raise ValueError
        
    except ValueError:    
        print("Invalid input. Please enter a string.")
    else:
      new_book = Book(new_book , Book_author , Book_addition , Book_price)

        