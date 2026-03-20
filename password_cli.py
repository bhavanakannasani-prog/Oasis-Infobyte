import random
import string

def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("🔐 Password Generator (CLI)")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("❌ Length must be positive.")
            return

        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_letters, use_digits, use_symbols)

        if password:
            print(f"\n✅ Generated Password: {password}")
        else:
            print("❌ Select at least one character type.")

    except ValueError:
        print("❌ Invalid input. Enter a number for length.")


if __name__ == "__main__":
    main()