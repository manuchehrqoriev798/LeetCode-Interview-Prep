def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test the function
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
