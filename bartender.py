def ask_age(): # Removed input() from here, as input() is used inside the function
    """Asks the user for their age and returns it as an integer."""
    while True: # Loop to ensure valid integer input
        try:
            age_str = input("What is your age? ")
            age = int(age_str)
            return age
        except ValueError:
            print("Invalid input. Please enter a number for your age.")

def check_age(age):
    """Checks the age and prints an appropriate message."""
    if age < 18:
        print("You are a minor, here's a soda.")
    elif 18 <= age < 21:
        print("You are between 18 and 21. You can order a non-alcoholic beverage.")
    else:
        print("You are an adult and can order a drink.")

# --- Program Execution ---
user_age = ask_age() # Call ask_age to get the age and store it
check_age(user_age) # Pass the stored age to check_age