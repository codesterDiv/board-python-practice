# Function to check if the number is positive or negative
def check_positive_negative(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"  # This case is ignored in the main logic

# Main program
def main():
    try:
        # Input a number from the user
        number = float(input("Enter a number: "))
        
        # Check if the number is positive or negative
        result = check_positive_negative(number)
        
        if result == "positive":
            print(f"The number {number} is positive.")
        elif result == "negative":
            print(f"The number {number} is negative.")
        else:
            print("Zero is neither positive nor negative, please enter a non-zero number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the main program
if __name__ == "__main__":
    main()
