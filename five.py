# Function to check if the number is positive
def check_positive(number):
    if number > 0:
        return True
    else:
        return False

# Main program
def main():
    try:
        # Input a number from the user
        number = float(input("Enter a number: "))
        
        # Check if the number is positive
        if check_positive(number):
            print(f"The number {number} is positive.")
        else:
            print(f"The number {number} is not positive.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the main program
if __name__ == "__main__":
    main()