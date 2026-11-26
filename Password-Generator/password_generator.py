import secrets
import string
# Available characters for password generation
characters = string.ascii_letters + string.digits + string.punctuation
# Validate password length
while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
        else:
            break

    except ValueError:
        print("Please enter a valid number.")
# Generate a secure random password
# Character categories
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# Guarantee at least one character from each category
password_list = [
    secrets.choice(uppercase),
    secrets.choice(lowercase),
    secrets.choice(digits),
    secrets.choice(symbols)
]

# Fill the remaining positions
for i in range(length - 4):
    password_list.append(secrets.choice(characters))

# Shuffle the characters securely
secrets.SystemRandom().shuffle(password_list)

# Convert the list into a string
password = "".join(password_list)

# Display the generated password
print("\n===== PASSWORD GENERATOR =====")
print("Your generated password:", password)
print("==============================")