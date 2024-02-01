# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    @property
    def get_books(self,books):
        self.books.append(books)
        self.no_of_books=len(self.books)
     
    
    def show(self):
        print(self.no_of_books)
        for book in self.books:
            print(book)

l1 = Library("harrybhai")

l1.get_books("harray bhai")
l1.get_books("harray bhai")
l1.get_books("harray bhai")

l1.show()