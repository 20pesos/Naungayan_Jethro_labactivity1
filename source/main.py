def check_odd_even(number):
    """Returns 'ODD' if the number is odd, and 'EVEN' if it is even."""
    if number % 2 != 0:
        return "ODD"
    else:
        return "EVEN"

if __name__ == "__main__":      # Ensures the code below only runs when the script is executed directly
    print("-------------- ODD & EVEN NUMBER CHECKER --------------")
    
    try:
        user_input = input("Enter a whole number: ")
        valid_number = int(user_input)       # This will trigger a ValueError if a letter or decimal is entered
    except ValueError:
        print("The value is incorrect. Letters and fractions are not allowed.")
        exit()
    
    result = check_odd_even(valid_number)    # Calls the function to check if the number is odd or even

    print(f"Result: {valid_number} is an {result} number.")