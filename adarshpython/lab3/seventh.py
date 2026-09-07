# Base class
class LibraryItem:
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self.issued = False

    def issue_item(self):
        if not self.issued:
            self.issued = True
            print(f"'{self.title}' has been issued.")
        else:
            print(f"'{self.title}' is already issued.")

    def return_item(self):
        if self.issued:
            self.issued = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not issued.")

    def display_details(self):
        raise NotImplementedError("Subclass must implement display_details()")


# Derived class: Book
class Book(LibraryItem):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.author = author

    def display_details(self):
        status = "Issued" if self.issued else "Available"
        print(
            f"Book | ID: {self.item_id} | "
            f"Title: {self.title} | "
            f"Author: {self.author} | Status: {status}"
        )


# Derived class: Magazine
class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue_number):
        super().__init__(item_id, title)
        self.issue_number = issue_number

    def display_details(self):
        status = "Issued" if self.issued else "Available"
        print(
            f"Magazine | ID: {self.item_id} | "
            f"Title: {self.title} | "
            f"Issue No: {self.issue_number} | Status: {status}"
        )


# Derived class: Journal
class Journal(LibraryItem):
    def __init__(self, item_id, title, publisher):
        super().__init__(item_id, title)
        self.publisher = publisher

    def display_details(self):
        status = "Issued" if self.issued else "Available"
        print(
            f"Journal | ID: {self.item_id} | "
            f"Title: {self.title} | "
            f"Publisher: {self.publisher} | Status: {status}"
        )


# Library Management System
class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_all_items(self):
        print("\n--- Library Items ---")
        for item in self.items:
            # Polymorphism
            item.display_details()

    def issue_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                item.issue_item()
                return

        print(f"Item with ID {item_id} not found.")

    def return_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                item.return_item()
                return

        print(f"Item with ID {item_id} not found.")


# Main program
library = Library()

# Creating objects
book = Book(101, "Python Programming", "Guido van Rossum")
magazine = Magazine(102, "Technology Today", 25)
journal = Journal(103, "Computer Science Journal", "Springer")

# Adding items
library.add_item(book)
library.add_item(magazine)
library.add_item(journal)

# Display all items
library.display_all_items()

# Issue items
print("\n--- Issue Operations ---")
library.issue_item(101)
library.issue_item(102)

# Try issuing the same book again
library.issue_item(101)

# Display updated status
library.display_all_items()

# Return items
print("\n--- Return Operations ---")
library.return_item(101)
library.return_item(102)

# Try returning an item that wasn't issued
library.return_item(103)

# Final status
library.display_all_items()      