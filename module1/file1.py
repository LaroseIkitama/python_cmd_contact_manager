"""This module contains all the functions of handling contact data.
    """


from utils.utils1 import indent
from utils.utils1 import clear_console
from utils.utils1 import is_numeric
from utils.utils1 import is_between_interval
from utils.utils1 import menu
from utils.utils1 import menu_modify_contact


contacts = []
contact_edit = {}
occurrences_contacts = []
position_contact_edit = 0


def array_contacts_is_empty():
    """This function checks whether the contacts array is empty.

    Returns:
        bool: True if the contacts array is empty, False otherwise.
    """

    if len(contacts) == 0:
        return True


def key_exist_in_contacts_array(key: int):
    """This function checks whether a key exists in the contacts array.

    Args:
        key (int): The key to be checked.

    Returns:
        bool: True if the key exists in the contacts array, False otherwise.
    """

    # Assuming `contacts` is defined outside of this function
    if key-1 in contacts:
        return True


def contact_already_exist_in_array_occurrence(contact_list: list):
    """This function checks whether a given contact list already exists in the occurrences_contacts array.

    Args:
        contact_list (list): The contact list to be checked.

    Returns:
        bool: True if the contact list already exists in the occurrences_contacts array, False otherwise.
    """

    # Assuming `occurrences_contacts` is defined outside of this function
    result = False

    for contact in occurrences_contacts:
        if contact_list == contact:
            result = True

    return result


def there_is_an_occurrence_in_values(search_str: str):
    """This function searches for a given string in the values of the contacts array, and adds any contacts
    with a match to the occurrences_contacts array.

    Args:
        search_str (str): The string to search for.
    """

    # Assuming `contacts` and `occurrences_contacts` are defined outside of this function
    global occurrences_contacts
    global occurrences_contacts

    for contact in contacts:
        for key, value in contact.items():
            if search_str in value:
                if not contact_already_exist_in_array_occurrence(contact):
                    occurrences_contacts.append(contact)


def display_occurrences(search_str: str):
    """This function displays the contacts that have a value containing the given search string.

    Args:
        search_str (str): The string to search for.
    """

    global occurrences_contacts
    there_is_an_occurrence_in_values(search_str)

    for contact in occurrences_contacts:
        print()

        for key, value in contact.items():
            print(indent(f"{key} : {value}", 32))

        print()

    occurrences_contacts = []


def add_contact():
    """This function prompts the user to enter contact information and stores it in a dictionary, 
    which is then added to a list of contacts.
    """

    contact = {}

    contact["Firstname"] = input(indent("Firstname :\t", 30))
    contact["Lastname"] = input(indent("Lastname :\t", 30))
    contact["Company"] = input(indent("Company :\t", 30))
    contact["Mobile"] = input(indent("Mobile :\t", 30))
    contact["Email"] = input(indent("Email :\t", 30))
    contact["Address"] = input(indent("Address :\t", 30))

    contacts.append(contact)

    print(
        "\n"
        + indent(" ***** The contact has been successfully registered ***** ", 30))


def display_contact():
    """Prompts the user to enter a search string and displays any contacts
    that match the search string.

    If there are no contacts in the `contacts` list, it prints a message 
    indicating that there are no contacts recorded.
    """

    if not array_contacts_is_empty():
        print()

        search_str = input(
            indent("Search...\t", 30))

        print()

        display_occurrences(search_str=search_str)
    else:
        print(
            "\n"
            + indent(" ********* No contact recorded ********* ", 38))


def show_all_contacts():
    """Displays a list of all saved contacts.
    """

    if not array_contacts_is_empty():
        clear_console()

        print(indent(
            f" _________________ List Of Contacts _________________ Total : {len(contacts)}", 30)+"\n")

        for index, contact in enumerate(contacts):
            print(indent(f"{index+1} ) ", 31)+"\n")

            for keys, values in contact.items():
                print(indent(f"{keys} : {values}", 32))

            print()
    else:
        print(
            "\n"
            + indent(" ********* No contact recorded ********* ", 38))


def switch_edit_contact(choice: int):
    """This function contains a switch statement to edit a contact's details based on the user's selected choice. 

    Args:
        choice (int): an integer value representing the user's selected option, should be within the range of 1-8.
    """

    if is_between_interval(0, choice, 9):
        if choice == 1:
            contact_edit['Firstname'] = input(
                indent("Firstname :\t", 30))
        if choice == 2:
            contact_edit['Company'] = input(
                indent("Company :\t", 30))
        if choice == 3:
            contact_edit['Email'] = input(indent("Email :\t", 30))
        if choice == 5:
            contact_edit['Lastname'] = input(
                indent("Lastname :\t", 30))
        if choice == 6:
            contact_edit['Mobile'] = input(
                indent("Mobile :\t", 30))
        if choice == 7:
            contact_edit['Address'] = input(
                indent("Address :\t", 30))
    else:
        print(
            "\n"
            + indent(" ********* Select the number between 1 and 8 ********* ", 29))


def loop_of_menu_edit():
    """Is a loop that allows the user to edit a contact.
    """

    while True:

        clear_console()
        print()

        for key, value in contact_edit.items():
            print(indent(f"{key} : {value}", 32))
        print()

        menu_modify_contact()
        choice = input(indent("Your choice : \t ", 40))

        if is_numeric(value=choice):

            clear_console()
            switch_edit_contact(choice=int(choice))

            if int(choice) == 4:
                print(
                    "\n"
                    + indent(" ********* C A N C E L ********* ", 40))
                break

            if int(choice) == 8:
                contacts[position_contact_edit] = contact_edit
                print(
                    "\n"
                    + indent(" ********* D O N E ********* ", 40))
                break

        else:
            clear_console()
            print(
                "\n"
                + indent(" ********* Error please enter a number ********* ", 33))


def edit_contact():
    """Allows the user to choose a contact from the list of contacts and edit it.
    """

    if not array_contacts_is_empty():

        choice = input(
            indent("Which contact do you want to edit ? : \t", 30))

        if is_numeric(value=choice) and is_between_interval(0, int(choice), len(contacts)+1):
            choice = int(choice)
            global position_contact_edit
            global contact_edit
            position_contact_edit = choice-1
            contact_edit = contacts[position_contact_edit]

            clear_console()
            print()

            for key, value in contact_edit.items():
                print(indent(f"{key} : {value}", 32))
            print()

            loop_of_menu_edit()

        else:
            clear_console()
            print(
                "\n"
                + indent(" ***** Error please enter the position of the contact to be edit ***** ", 20))


def delete_contact():
    """This function implements the deletion of a contact from the contacts list.
    """

    if not array_contacts_is_empty():

        choice = input(
            indent("Which contact do you want to delete ? : \t", 30))

        if is_numeric(value=choice) and is_between_interval(0, int(choice), len(contacts)+1):
            choice = int(choice)
            contact_deleted = contacts.pop(choice-1)

            clear_console()
            print()

            for key, value in contact_deleted.items():
                print(indent(f"{key} : {value}", 32))
            print()

            print(
                "\n"
                + indent(" ********* This contact has been deleted ********* ", 30))

        else:
            clear_console()
            print(
                "\n"
                + indent(" ***** Error please enter the position of the contact to be deleted ***** ", 20))


def switch(choice: int):
    """Takes an integer choice as input and calls other functions based on the choice provided.

    Args:
        choice (int): _description_
    """

    clear_console()

    if is_between_interval(0, choice, 7):
        if choice == 1:
            add_contact()
        if choice == 2:
            show_all_contacts()
            edit_contact()
        if choice == 3:
            show_all_contacts()
            delete_contact()
        if choice == 4:
            display_contact()
        if choice == 5:
            show_all_contacts()
    else:
        print(
            "\n"
            + indent(" ********* Select the number between 1 and 6 ********* ", 29))
