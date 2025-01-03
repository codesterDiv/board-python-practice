# Function to check if the number is odd
def check_odd(number):
    return number % 2 != 0  # Returns True if the number is odd

# Main program
def main():
    try:
        # Input a number from the user
        number = int(input("Enter a number: "))
        
        # Check if the number is odd
        if check_odd(number):
            print(f"The number {number} is odd.")
        else:
            print(f"The number {number} is even.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Run the main program
if __name__ == "__main__":
    main()