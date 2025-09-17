"""


Class AddressBook
Attributes:

list[Contact]
"""

from contact import Contact
from os import system


class AddressBook:
    def __init__(self, contact_list: list[Contact]) -> None:
        self.__contact_list = contact_list

    # Le getter de la liste
    def display_contact_list(self) -> None:
        contacts: list[Contact] = self.__contact_list

        # Boucle d'affichage de contacts dans la liste
        print(f"\n{'*' * 10} CONTACTS {'*' * 10}\n")
        for i, contact in enumerate(contacts, 1):
            print(f"{'-' * 3} Contact {i} {'-' *3}\n")
            print(contact)

    def add_contact(self, contact: Contact) -> None:
        if isinstance(contact, Contact) and contact is not None:
            self.__contact_list.append(contact)
            print("\nContact added!\n")
        else:
            raise AssertionError("Error: You should add a contact!")

    def remove_contact(self) -> None:
        """Remove a contact from the address book."""
        if len(self.__contact_list) == 0:
            print("\nContact list is empty\n")
            return
        
        while True:
            system("clear")
            self.display_contact_list()
            print()
            
            choice_str = input(
                f"Enter the contact number to remove (1 to {len(self.__contact_list)}). 0 to cancel: "
            )
            
            try:
                choice = int(choice_str)
                if choice == 0:
                    print("\nOperation cancelled\n")
                    return
                
                if 1 <= choice <= len(self.__contact_list):
                    self.__contact_list.pop(choice - 1)
                    print("\nContact removed\n")
                    return
                else:
                    print(f"Error: Number must be between 1 and {len(self.__contact_list)}")
                    
            except ValueError:
                print("Error: Please enter a valid number")
            
            system("sleep 1")
