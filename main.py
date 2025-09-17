"""

Entry Point main
"""

from contact import Contact
from address_book import AddressBook
from os import system


def menu() -> int:
    while True:
        system("clear")
        print(f"\n{'*' * 10} MENU {'*' * 10}\n")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display all Contact")
        print("4. Quit")
        print()

        choice_str: str = input("Your choice (1,2,3,4) : ")

        try:
            choice = int(choice_str)
            if 1 <= choice <= 4:
                return choice
            else:
                print("Error: Your choice should be between 1 and 4")
        except ValueError:
            print("Error: Please enter a valid number (1-4)")
        
        system("sleep 1")


def main():
    list_contacts: list[Contact] = [
        Contact("Jean", "Bertrand", "jean.bertrand@gmail.com", "0488563321"),
        Contact("Marie", "Belle", "marie.belle@gmail.com", "04726363311"),
        Contact("Mohammed", "Bhargan", "mohammed.barghan@gmail.com", "046695021"),
        Contact("Antoine", "Van Potteghem", "antoine.pot@gmail.com", "0453967852"),
        #     Contact("Jean","Bertrand","jean.bertrand@gmail.com","0488563321"),
        #     Contact("Jean","Bertrand","jean.bertrand@gmail.com","0488563321"),
        #     Contact("Jean","Bertrand","jean.bertrand@gmail.com","0488563321"),
    ]

    address_book = AddressBook(list_contacts)

    while True:
        choice: int = menu()

        match choice:
            case 1:
                address_book.add_contact(Contact.create_contact())
                system("sleep 1")
                system("clear")
            case 2:
                address_book.remove_contact()
                system("sleep 1")
                system("clear")
            case 3:
                address_book.display_contact_list()
                system("sleep 4")
                system("clear")
            case 4:
                print("\nAu revoir et merci!\n")
                system("sleep 1")
                system("clear")
                break


if __name__ == "__main__":
    main()
