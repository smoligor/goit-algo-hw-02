from collections import deque

def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome using deque.
    The string is case-insensitive and ignores spaces (and other non-alphanumeric characters).
    """
    formatted_s = ''.join(filter(str.isalnum, s)).lower()
    # If after cleaning the string is empty or has 1 character, it is a palindrome
    if len(formatted_s) <= 1:
        return True
        
    # 2. Create a double-ended queue
    char_deque = deque(formatted_s)
    
    # 3. Compare characters from both ends
    while len(char_deque) > 1:
        first_char = char_deque.popleft()
        last_char = char_deque.pop()
        
        if first_char != last_char:
            return False # If characters do not match, it's not a palindrome
            
    return True # If the loop finished, all characters matched

print("\n--- Task 2: Palindrome Check ---")
test_strings = [
    "Racecar",
    "A man, a plan, a canal: Panama",
    "Hello World",
    "Was it a car or a cat I saw?",
    "No lemon, no melon.",
    "Кіт утік", # In Ukrainian
    "Madam",
    "12321",
    " ", # Only space
    "a", # One character
    ""   # Empty string
]

for ts in test_strings:
    if is_palindrome(ts):
        print(f"'{ts}' -> is a palindrome.")
    else:
        print(f"'{ts}' -> is NOT a palindrome.")