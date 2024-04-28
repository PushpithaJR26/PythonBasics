def is_palindrome(s):
    
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())

    return s == s[::-1]


string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
