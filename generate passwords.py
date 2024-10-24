import itertools
import string
import os  # To use environment variables

# Function to generate passwords
def generate_passwords(min_length, max_length, characters, output_file):
    try:
        with open(output_file, 'w') as f:
            for length in range(min_length, max_length + 1):
                # Use itertools.product to generate all possible combinations based on length
                for password in itertools.product(characters, repeat=length):
                    # Convert the tuple into a string
                    password_str = ''.join(password)
                    # Write the password to the file
                    f.write(password_str + '\n')
        print(f"[+] Passwords generated and saved to '{output_file}'.")
    except Exception as e:
        print(f"[-] Error occurred while generating passwords: {e}")

# Main function to get input from the user
def main():
    print("=== Password Generator Tool (Crunch-like) ===")

    # Get minimum and maximum password length from the user
    min_length = int(input("Enter the minimum password length: "))
    max_length = int(input("Enter the maximum password length: "))

    # Character set options
    use_lowercase = input("Do you want to use lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Do you want to use uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Do you want to use numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Do you want to use special characters? (y/n): ").lower() == 'y'

    # Building the character set based on user choices
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("[-] You must select at least one type of character.")
        return

    # Get the Desktop path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Ask the user for the output file name
    file_name = input("Enter the output file name (e.g., passwords.txt): ")

    # Full path to the output file on the desktop
    output_file = os.path.join(desktop_path, file_name)

    # Generate the passwords
    generate_passwords(min_length, max_length, characters, output_file)

if __name__ == "__main__":
    main()
