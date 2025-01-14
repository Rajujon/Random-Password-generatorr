import random
import string

def generate_password(length, use_special_chars):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    
    # Characters to use in the password
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ""
    
    all_chars = letters + digits + special_chars
    
    # Ensure at least one character from each required set
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars) if use_special_chars else random.choice(letters),
    ]
    
    # Fill the rest of the password
    password += random.choices(all_chars, k=length - len(password))
    
    # Shuffle the password to make it unpredictable
    random.shuffle(password)
    
    return ''.join(password)

# Get user input
try:
    length = int(input("Enter the desired password length: "))
    use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    
    generated_password = generate_password(length, use_special_chars)
    if generated_password:
        print("Your generated password is:", generated_password)
except ValueError:
    print("Please enter a valid number for the password length.")
