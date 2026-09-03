#Project4
list=[]
class Book:
    def __init__(self,book_id=0,tittle="",aurther="",price=0):
        self.book_id=book_id
        self.tittle=tittle
        self.aurther=aurther
        self.price=price

    def Add(self):
        print("Book Details:")
        book_id=int(input("Enter a book id:"))
        tittle=str(input("Enter a book tittle:"))
        aurther=str(input("Enter a aurther name:"))
        price=int(input("Enter a price of book:"))
        book=Book(book_id,tittle,aurther,price)
        list.append(book)

    def View(self):
        for book in list:
            print(book.book_id,book.tittle,book.aurther,book.price)

    def Search(self):
        id=int(input("Enter book id to search:"))
        for book in list:
            if book.book_id==id:
                print(book.book_id,book.tittle,book.aurther,book.price)

    def Update(self):
         id=int(input("Enter book id to Updated:"))
         for book in list:
            if book.book_id==id:
                book.book_id=int(input("Enter a updated id:"))
                book.tittle=str(input("Enter a updated tittle:"))
                book.aurther=str(input("Enter a updated aurther:"))
                book.price=int(input("Enter a book price:"))
                print("Book Updated!")
            else:
             print("Book Not Found.")

    def Delete(self):
        id=int(input("Enter book id to Delete:"))
        for book in list:
            if book.book_id==id:
                list.remove(book)
                print("Book Deleted!")
            else:
             print("Book Not Found!")

class eBook(Book):
    def __init__(self, book_id=0, tittle="", aurther="", price=0,file_size=0):
        super().__init__(book_id, tittle, aurther, price)

        self.file_size=file_size

    def View(self):
     print("EBook Details:")
     print("Book ID:", self.book_id)
     print("Title:", self.tittle)
     print("Author:", self.aurther)
     print("Price:", self.price)
     print("File Size:", self.file_size)


def Display(obj):
    obj.View()

B=Book()
E=eBook()

while True:
    print("\n===================================")
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. View EBook")
    print("7. Polymorphism Test")
    print("8. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        B.Add()

    elif choice == 2:
        B.View()

    elif choice == 3:
        B.Search()

    elif choice == 4:
        B.Update()

    elif choice == 5:
        B.Delete()

    elif choice == 6:
        E.book_id = int(input("Enter EBook id: "))
        E.title = input("Enter EBook title: ")
        E.author = input("Enter author name: ")
        E.price = int(input("Enter EBook price: "))
        E.file_size = input("Enter file size: ")
        E.View()

    elif choice == 7:
        print("\n--- Polymorphism ---")
        Display(B)
        Display(E)

    elif choice == 8:
        print("Exit Program...")
        break

    else:
        print("Invalid Choice!")
