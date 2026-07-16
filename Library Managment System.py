class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True


class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.persons = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Name: ")
        book = Book(book_id, title)
        self.books.append(book)
        print("Book Added")

    def register_person(self):
        person_id = input("Enter Person ID: ")
        name = input("Enter Person Name: ")
        person = Person(person_id, name)
        self.persons.append(person)
        print("Person Registered")

    def issue_book(self):
        book_id = input("Enter Book ID: ")
        person_id = input("Enter Person ID: ")

        for book in self.books:
            if book.book_id == book_id and book.available:
                for person in self.persons:
                    if person.person_id == person_id:
                        if book.title in person.borrowed_books:
                            book.available = False
                            person.borrowed_books.append(book.title)
                            print("Book Issued Successfully!")
                            return

        print("Book not available or Person not found!")

    def return_book(self):
        book_id = input("Enter Book ID: ")
        person_id = input("Enter person ID: ")

        for book in self.books:
            if book.book_id == book_id:
                for person in self.persons:
                    if person.person_id == person_id:
                        if book.title in person.borrowed_books:
                            book.available = True
                            person.borrowed_books.remove(book.title)
                            print("Book Returned")
                            return

        print("Book or person not found!")


library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register person")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.register_person()
    elif choice == "3":
        library.issue_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")