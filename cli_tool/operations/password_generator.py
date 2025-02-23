import random
import string
import sys

def generate_password(length: int) -> str:
    '''Generate a random password of the specified length.'''
    
    if length < 4:
        print("Error: password length must be at least 4")
        sys.exit(1)
        
    # Define character sets for password generation    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Initialize password with one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Generate remaining characters randomly
    all_chars = uppercase + lowercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)
    
    # Shuffle the password to mix the characters    
    random.shuffle(password)
    
    return "".join(password)
    
