# Lists to hold Users and Books data

users = []
books = []

# Main Menu
def main_menu():
    """"Displays the main menu and handles the user choices."""
    while True:
        print("Welcome to the Community Library System!")
        print("----------------------------------------")
        print("Please select an option: ")
        print("1. View all books: ")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View all users")
        print("6. Exit")
        choice = input("Enter your choice(1-6): ")
        if choice == '1':
            display_all_books()
        elif choice == '2':
            search_book()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            display_all_users()
        elif choice == '6':
            print("Goodbye")
            break
        else:
            ("Invalid choice. Please try again.")


