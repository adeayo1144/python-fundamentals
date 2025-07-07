: #/usr/bin/python3

def is_strong_password(password):
    # Check length
    if len(password) < 8:
        return False
    
    # Check for spaces
    if any(char.isspace() for char in password):
        return False
    
    # Check if contains at least one letter and one number
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)
    
    return has_letter and has_number

# Example tests
print(is_strong_password("abc12345"))   # True
print(is_strong_password("abc 12345"))  # False (space)
print(is_strong_password("abcdefgh"))   # False (no number)
print(is_strong_password("12345678"))   # False (no letter)
print(is_strong_password("a1"))         # False (too short)
