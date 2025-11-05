def is_palindrome(text):
    """
    Checks if a given string is a palindrome.
    It ignores spaces, punctuation, and capitalization.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    processed_text = "".join(filter(str.isalnum, text)).lower()
    return processed_text == processed_text[::-1]

if __name__ == "__main__":
    user_input = input("Enter a word or phrase: ")

    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome. Yes!")
    else:
        print(f"'{user_input}' is not a palindrome. No.")