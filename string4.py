strn = input("Enter a string: ")

cleaned_string = strn.replace(" ", "").lower()

if cleaned_string == cleaned_string[::-1]:
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")
