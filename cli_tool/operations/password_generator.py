import random
import string
import sys

def generate_password(length: int) -> str:
    
    if length < 4:
        print("Error: password length must be at least 4")
        sys.exit(1)
        
        
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation
    
    
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    
    all_chars = uppercase + lowercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)
    
        
    random.shuffle(password)
    
    return "".join(password)
    
