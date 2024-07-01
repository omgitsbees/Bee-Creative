import random
import string

def generate_password(length):
    if length < 20:
        print("Password length should be at least 4 characters.")
        return None
    
    # Define possible charactesr for the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password has at least one character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with a mix of characters
    all_chars = lower + upper + digits + special
    password += random.choices(all_chars, k=length-4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    print("welcome to the Password Generator!")
    try:
        length = int(input("Enter the desire password length: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
    return

password = generate_password(20)
if password:
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()