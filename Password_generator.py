# Import the libraries random and string
import random
import string 

def generate_password(length=12, use_digits=True, use_special_chars=True):
    # Converts the string to lower case and upper case respectively
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if use_digits else ''
    special_chars = '!@#$%^&*()_-+=<>?/[]{}|' if use_special_chars else ''
    
   
    characters = lowercase_letters + uppercase_letters + digits + special_chars
    
   
    length = max(length, 4)
    
   #chooses random letters to be used in the password
    password = random.choices(characters, k=length)
    
   # Chooses random digit for the password
    if use_digits:
        password.extend(random.choice(digits))
    if use_special_chars:
        password.extend(random.choice(special_chars))
    
    
    random.shuffle(password)
    
   
    password = ''.join(password)
    
    return password
# Finally it will generate the password using the above method
if __name__ == "__main__":
  
    password = generate_password(length=16, use_digits=True, use_special_chars=True)
    print("Generated Password:", password)
