"""This module contains useful functions of checking values,manipulating and display strings, etc...
"""
import os


def indent(string: str, spaces: int):
    """This function indents the given string by the specified number of spaces.

    Args:
        string (str): The string to be indented.
        spaces (int): The number of spaces by which the string should be indented.

    Returns:
        str: The indented string.
    """

    indentation = " " * spaces

    return indentation+string


def clear_console():
    """This function clears the console screen.
    """

    os.system('cls' if os.name == 'nt' else 'clear')


def is_numeric(value: str):
    """This function checks whether the given string is numeric or not.

    Args:
        value (str): The string to be checked.

    Returns:
        bool: True if the string is numeric, False otherwise.
    """

    if value.isnumeric():
        return True


def is_between_interval(lower_value: int, value: int, higher_value: int):
    """This function checks whether a value is within a specified interval.

    Args:
        lower_value (int): The lower bound of the interval.
        value (int): The value to be checked.
        higher_value (int): The upper bound of the interval.

    Returns:
        bool: True if the value is within the interval, False otherwise.
    """

    if value > lower_value and value < higher_value:
        return True


def menu():
    """This function displays the menu options for the contact manager program.
    """

    print("\n" + indent("___________________ Contact Manager ___________________", 30)+"\n")
    print(indent("1 - Add a contact\t\t\t4 - Display a contact", 30)+"\n")
    print(indent("2 - Edit a contact\t\t5 - Show all contacts", 30)+"\n")
    print(indent("3 - Delete a contact\t\t6 - Exit", 30)+"\n")


def menu_modify_contact():
    """This function displays the options available when modifying a contact.
    """

    print("\n" + indent("_________________ What do you want to change? _________________", 30)+"\n")
    print(indent("1 - Firstname\t\t\t5 - Lastname", 39)+"\n")
    print(indent("2 - Company\t\t\t6 - Mobile", 39)+"\n")
    print(indent("3 - Email\t\t\t7 - Address", 39)+"\n")
    print(indent("4 - Cancel\t\t\t8 - Done", 39)+"\n")
