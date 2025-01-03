# Function to check if the number is positive, negative, or zero
def check_number(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

# Main program
def main():
    try:
        # Input a number from the user
        number = float(input("Enter a number: "))
        
        # Check if the number is positive, negative, or zero
        result = check_number(number)
        
        if result == "positive":
            print(f"The number {number} is positive.")
        elif result == "negative":
            print(f"The number {number} is negative.")
        else:
            print(f"The number {number} is zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the main program
if __name__ == "__main__":
    main()