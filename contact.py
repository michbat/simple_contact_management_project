"""

Classe Contact

Attributes: firstname, lastname, email, phone
"""


class Contact:
    # Constructeur
    def __init__(
        self, firstname: str = "", lastname: str = "", email: str = "", phone: str = ""
    ) -> None:
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__phone = phone

    @property  # Propriété "firstname" -> getter
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter  # Setter
    def firstname(self, value: str) -> None:
        if isinstance(value, str) and value.strip():
            self.__firstname = value
        else:
            raise ValueError("Error: Firstname must be a non-empty string")

    @property  # Propriété "lastname" -> getter
    def lastname(self) -> str:
        return self.__lastname
 
    @lastname.setter # Setter
    def lastname(self, value: str) -> None:
        if isinstance(value, str) and value.strip():
            self.__lastname = value
        else:
            raise ValueError("Error: Lastname must be a non-empty string")

    @property  # Propriété "email" -> getter
    def email(self) -> str:
        return self.__email

    @email.setter # setter
    def email(self, value: str) -> None:
        if isinstance(value, str) and value.strip():
            self.__email = value
        else:
            raise ValueError("Error: Email must be a non-empty string")

    @property # Propriété "phone" -> getter
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, value: str) -> None:
        if isinstance(value, str) and value.strip():
            self.__phone = value
        else:
            raise ValueError("Error: Phone must be a non-empty string")

    # Méthode magique __str__ : l'équivalent plus ou moins de la méthode ToString en Java
    def __str__(self) -> str:
        return (
            f"First Name: {self.__firstname}\n"
            + f"Last Name: {self.__lastname}\n"
            + f"Email: {self.__email}\n"
            + f"Phone: {self.__phone}\n"
        )

    # Méthode statique utilitaire
    @staticmethod
    def get_valid_input(prompt: str, field_name: str) -> str:
        """Helper method to get valid non-empty input from user."""
        while True:
            value = input(prompt)
            if value.strip():
                return value
            else:
                print(f"Error: {field_name.capitalize()} cannot be empty!")

    # Méthode classe retournant un objet "Concact"
    @classmethod
    def create_contact(cls) -> "Contact":

        print(f"\n{'*' * 10} ADD CONTACT {'*' * 10}\n")

        contact = Contact()
        contact.firstname = (
            cls.get_valid_input("Enter Firstname: ", "firstname").lower().capitalize()
        )
        contact.lastname = (
            cls.get_valid_input("Enter Lastname: ", "lastname").lower().capitalize()
        )
        contact.email = cls.get_valid_input("Enter email: ", "email").lower()
        contact.phone = cls.get_valid_input("Enter Phone: ", "phone")

        return contact
