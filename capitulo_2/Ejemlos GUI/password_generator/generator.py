""" Module to generate secure password
"""

from random import choice

def generate_numbers()-> list:
    """Generate a list of numbers, from 0 to 9

    Returns:
        list: list of numbers from 0 to 9
    """
    numbers = []

    for i in range(0,10):
        numbers.append(str(i))

    return numbers

def generate_symbols(length=4)->str():
    password = ""
    symbols = "!\"#$%&/()=?¿¡'`+',.-_}{[]<>"

    while len(password) < length:
        password += choice( symbols )

    return password

def generate_password_numbers(length=4)-> str:
    """Generate a password with only numbers

    Args:
        length (int, optional): This is the long to be the password. Defaults to 4.

    Returns:
        str: Return the password with only numbers
    """
    password = ""
    numbers = generate_numbers()
    while len(password) < length:
        password += choice( numbers )

    return password

def generate_password_letters(length=4)-> str:
    """Generare a password with letter lowercase and uppercase

    Args:
        length (int, optional): The long to be the password. Defaults to 4.

    Returns:
        str: A password with only letters
    """
    password = ""
    letters_low = "abcdefghijklmnopqrtuvwxyz"
    letter_up = letters_low.upper()

    while len(password) < length:
        password += choice( letters_low + letter_up )

    return password

def generate_password(length=4)-> str:
    """Generate a password with symbols, number and letters

    Args:
        length (int, optional): Length for password. Defaults to 4.

    Returns:
        str: Password
    """
    password = ""
    while len(password) < length:
        password += choice( generate_password_letters(1) + generate_password_numbers(1) + generate_symbols(1))

    return password

def main():
    print(generate_password(20))

if __name__ == "__main__":
    main()
