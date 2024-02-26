def main():
    library = {
        "Harry Potter and the Sorcerer's Stone": 5,
        "Lord of the Rings: The Fellowship of the Ring": 3,
        "Lord of the Rings: The Two Towers": 2,
        "Lord of the Rings: The Return of the King": 1,
        "Dune": 4,
        "Foundation": 3,
        "Dune Messiah": 2,
        "Children of Dune": 1,
    }
    while True:
        choice = input("Please type O to check a book out, I to check a book in, V to view the current inventory or Q to quit the program: ")
        if choice == "O":
            user_book_out = input("Please choose a book to checkout: ")
            check_out(user_book_out, library)
            
        elif choice == "I":
            user_book_in = input("Please choose a book to checkin: ")
            check_in(user_book_in, library)
            print(f"{user_book_in} has been checked in successfully!")

        elif choice == "V":
            for key, value in print_inv(library).items():
                print(key, value)
        
        elif choice == "Q":
            print("Program quitting....")
            break

def check_out(user_book_out, library):
    for book in library:
        if library[book] == 0:
            print(f"Sorry no more copies of {book} left!")
        if book == user_book_out:
            library[book] -= 1
            print(f"{user_book_out} has been checked out successfully!")
    return library


def check_in(user_book_in, library):
    for book in library:
        if book == user_book_in:
            library[book] += 1
    return library

def print_inv(library):
    return library

if __name__ == "__main__":
    main()
