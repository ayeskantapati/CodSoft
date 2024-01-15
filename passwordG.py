import random
import string

# Define character sets for password generation
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

def generate_password(length, include_letters=True, include_digits=True, include_symbols=True):
    """Generates a random password with the specified length and complexity."""

    # Build the character pool based on user preferences
    password_characters = []
    if include_letters:
        password_characters.extend(letters)
    if include_digits:
        password_characters.extend(digits)
    if include_symbols:
        password_characters.extend(symbols)

    # Shuffle the character pool for randomness
    random.shuffle(password_characters)

    # Generate the password by randomly choosing characters from the pool
    password = ''.join(random.choice(password_characters) for i in range(length))

    return password

# Get user input for password length
while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        if length >= 8:  # Enforce a minimum password length of 8
            break
        else:
            print("Password length must be at least 8 characters.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Get user preferences for password complexity
include_letters = input("Include letters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Generate and display the password
password = generate_password(length, include_letters, include_digits, include_symbols)
print("Your generated password is:",password)