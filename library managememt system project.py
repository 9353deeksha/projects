from datetime import datetime,timedelta

class Library:
    def __init__(self):
        self.books = {}  
        self.issued_books = {}  
        self.fine_per_day = 50  

    def add_book(self):
        book_id = input("Enter BOOK ID: ")
        title = input("Enter BOOK Name: ")
        author = input("Enter Author name: ")
        self.books[book_id] = [title, author, "YES"]
        print('Data Entered Successfully for book id:', book_id)

    def delete_book(self):
        book_id = input("Enter BOOK ID: ")
        if book_id in self.books:
            del self.books[book_id]
            print("Book deleted successfully.")
        else:
            print("Book not found.")
        self.display_books()

    def issue_book(self):
        student_name = input("Enter your Name: ")
        student_id = input("Enter your USN: ")
        book_name = input("Enter Book name: ")
        issue_date = datetime.now() 

        for book_id, details in self.books.items():
            if details[0] == book_name and details[2] == "YES":
                self.books[book_id][2] = "NO"
                self.issued_books[student_id] = [student_name, book_id, issue_date]
                print(book_name, "book issued to", student_name, "on", issue_date)
                print("Please return the book within 30 days")
                return
        print("Book not available")

    def return_book(self):
        name = input("Enter your Name: ")
        book_id = input("Enter book id: ")
        return_date = datetime.now() + timedelta(days=40) 

        for student_id, details in self.issued_books.items():
            if details[1] == book_id:
                issue_date = details[2]
                fine = self.calculate_fine(issue_date, return_date)
                if fine > 0:
                    print(f"Late return! Your fine is ₹{fine}.")
                else:
                    print("Book returned on time. No fine.")

                self.books[book_id][2] = "YES"
                del self.issued_books[student_id]
                print("Book id:", book_id, "book returned by:", name)
                return
        print("No record found for this book issue.")

    def calculate_fine(self, issue_date, return_date):
       # issue_date = datetime.strptime(issue_date, "%d-%m-%Y")
        #return_date = datetime.strptime(return_date, "%d-%m-%Y")
        delay_days = (return_date - issue_date).days

        if delay_days > 30:
            fine = (delay_days - 30) * self.fine_per_day  
            return fine
        return 0

    def select_book(self):
        book = input('Enter the name of book: ')
        print("Book ID\tBook Title\tAuthor\tAvailable")
        found = False
        for book_id, details in self.books.items():
            if details[0] == book:
                print(book_id, "\t", details[0], "\t", details[1], "\t", details[2])
                found = True
        if not found:
            print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books available!")
            return
        print("Book ID\tBook Title\tAuthor\tAvailable")
        for book_id, details in self.books.items():
            print(book_id, "\t",  details[0], "\t",  details[1], "\t",  details[2])

    def display_issued_books(self):
        if not self.issued_books:
            print("No issued books.")
            return
        print("List of issued books:")
        print("Reg No\tStudent Name\tBook ID\tBook Name\tIssue Date")
        for student_id, details in self.issued_books.items():
            book_id = details[1]
            print(student_id, "\t",  details[0], "\t",  book_id, "\t",  self.books[book_id][0], "\t",  details[2])

    def run(self):
        Admin_name = input("Enter Library Admin name: ")
        password = input("Enter Password: ")
        if Admin_name == 'admin' and password == '1234':
            print('Login successful: Admin')
            while True:
                print("\nPycoders LIBRARY MANAGEMENT SYSTEM")
                print("1. Add book")
                print("2. Issue book")
                print("3. Return book")
                print("4. Display books")
                print("5. Delete book")
                print("6. Exit")
                ch = input("Enter your choice: ")

                if ch == '1':
                    self.add_book()
                elif ch == '2':
                    self.issue_book()
                elif ch == '3':
                    self.return_book()
                elif ch == '4':
                    self.display_books()
                elif ch == '5':
                    self.delete_book()
                elif ch == '6':
                    print("Thank you\nVisit again")
                    break
                else:
                    print("Invalid choice, try again.")
                    break
        else:
            print("Wrong username or Password, try again")

library = Library()
library.run()
